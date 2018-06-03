import numpy as np
import pandas as pd
import networkx as nx
import pickle
import json
import operator
import csv
import ast
from datetime import timedelta
from datetime import datetime as dt

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def splitDataFrameList(df,target_column,separator):
    ''' df = dataframe to split,
    target_column = the column containing the values to split
    separator = the symbol used to perform the split
    returns: a dataframe with each entry for the target column separated, with each element moved into a new row. 
    The values in the other columns are duplicated across the newly divided rows.
    '''
    def splitListToRows(row,row_accumulator,target_column,separator):
        split_row = row[target_column].split(separator)
        for s in split_row:
            new_row = row.to_dict()
            new_row[target_column] = s
            row_accumulator.append(new_row)
    new_rows = []
    df.apply(splitListToRows,axis=1,args = (new_rows,target_column,separator))
    new_df = pd.DataFrame(new_rows)
    return new_df

def sec_to_hours(seconds):
    sec = timedelta(seconds=seconds)
    d = dt(1,1,1) + sec
    return("%02d:%02d:%02d" % (d.hour, d.minute, d.second))
    # if (seconds == 2702145):
    #     return ('31:6:35:45')
    # else:
    #     return("%02d:%02d:%02d:%02d" % (d.day-1, d.hour, d.minute, d.second))

#################################################################################################

podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)

podcast_info['percent_unique'] = 0.0
podcast_info['num_guests'] = 0
podcast_info['num_unique'] = 0
guest_durations_podcast = pd.read_csv('../reading_and_cleaning/guest_durations_podcast.csv', sep='\t', index_col=0)


for index, row in podcast_info.iterrows():
    podcast_df = guest_durations_podcast[guest_durations_podcast['podcast']==row['Podcast Name']].copy()
    num_guests = len(podcast_df)
    num_unique = 0
    for index1, row1 in podcast_df.iterrows():
        guest_df = guest_durations_podcast[guest_durations_podcast['guests']==row1['guests']].copy()
        if(len(guest_df)==1):
            num_unique+=1
    frac_unique = num_unique/num_guests
    podcast_info.at[index, 'percent_unique'] = np.round(100*frac_unique,1)
    podcast_info.at[index, 'num_guests'] = num_guests
    podcast_info.at[index, 'num_unique'] = num_unique


guest_host = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)
guest_host['date'] = pd.to_datetime(guest_host['date'])
guest_host.sort_values(by='date', inplace=True)
guest_host.reset_index(inplace=True, drop=True)
most_recent_date = guest_host['date'].iloc[-1]



podcast_info['avg_day_diff'] = 0.0
podcast_info['active'] = False
podcast_info['premier'] = ''
podcast_info['avg_ep_lengths'] = ''

for index, row in podcast_info.iterrows():
    podcast_df = guest_host[guest_host['podcast']==row['Podcast Name']].copy()
    podcast_df.reset_index(inplace=True, drop=True)
    podcast_info.at[index, 'premier'] = str(podcast_df['date'].iloc[0])
    day_diffs = []
    ep_lengths = []
    for index1, row1 in podcast_df.iterrows():
        ep_lengths.append(row1['duration'])
        if(index1>0):
            day_diffs.append(((podcast_df['date'][index1]-podcast_df['date'][index1-1]).total_seconds()/86400))
    most_recent_ep_date = podcast_df['date'].iloc[-1]
    days_since_most_recent = (most_recent_date-most_recent_ep_date).total_seconds()/86400
    active = True
    if(days_since_most_recent > 5*np.mean(day_diffs)):
        active = False
    podcast_info.at[index, 'avg_day_diff'] = np.round(np.mean(day_diffs),1)
    podcast_info.at[index, 'active'] = active
    podcast_info.at[index, 'avg_ep_lengths'] = sec_to_hours(np.round(np.mean(ep_lengths),0))


similarities = pd.read_csv('podcast_similarities.csv', sep='\t', index_col=0)
similarities = similarities[similarities['score']>0]

G1 = nx.from_pandas_dataframe(similarities, 'podcast1', 'podcast2', edge_attr=['score'], create_using=nx.Graph())

sorted_close = sorted(nx.closeness_centrality(G1).items(), key=operator.itemgetter(1), reverse=True)
df_sorted_close = pd.DataFrame(sorted_close)
sorted_close_dict = {}
for index, row in df_sorted_close.iterrows():
    sorted_close_dict[row[0]] = index+1
print("Closeness Centrality Done")

sorted_bt = sorted(nx.betweenness_centrality(G1).items(), key=operator.itemgetter(1), reverse=True)
df_sorted_bt = pd.DataFrame(sorted_bt)
print("Betweenness Centrality Done")
sorted_bt_dict = {}
for index, row in df_sorted_bt.iterrows():
    sorted_bt_dict[row[0]] = index+1

sorted_degree = sorted(nx.degree_centrality(G1).items(), key=operator.itemgetter(1), reverse=True)
df_sorted_degree = pd.DataFrame(sorted_degree)
sorted_degree_dict = {}
for index, row in df_sorted_degree.iterrows():
    sorted_degree_dict[row[0]] = index+1

podcast_info['close_rank'] = 0
podcast_info['bt_rank'] = 0
podcast_info['degree_rank'] = 0

p_info  = podcast_info.drop(['feedURL', 'keywords', 'cleaner'], axis=1)
p_info.columns=['name', 'hosts', 'imgurl', 'categories', 'description', 
                'percent_unique', 'num_guests', 'num_unique', 'avg_day_diff', 
                'active', 'premier', 'avg_ep_lengths', 
                'close_rank', 'bt_rank', 'degree_rank']

for index, row in p_info.iterrows():
    p_info.at[index, 'degree_rank'] = sorted_degree_dict[row['name']]
    p_info.at[index, 'close_rank'] = sorted_close_dict[row['name']]
    p_info.at[index, 'bt_rank'] = sorted_bt_dict[row['name']]


p_info['podcast_id'] = podcast_info.index-1

dict_list = p_info.to_dict(orient='records')

dj_podcasts=[]
for i in range(len(p_info)):
    d={}
    d['model'] = 'podcasts.Podcasts'
    d['pk'] = i
    d['fields'] = dict_list[i]
    dj_podcasts.append(d)
    
dj_podcasts

import json
with open('podcast_info.json', 'w') as outfile:
    json.dump(dj_podcasts, outfile)



#################################################################################################

podcast_similarities = pd.read_csv('podcast_similarities.csv', sep='\t', index_col=0)
podcast_similarities.sort_values(by='score', ascending=False, inplace=True)
podcast_similarities = podcast_similarities[podcast_similarities['score']>0]
podcast_similarities

similarities = pd.DataFrame(columns=['podcast1', 'podcast2', 'podcast2_id', 'score'])

num = len(podcast_info)
index=0
for index2, row2 in podcast_info.iterrows():
    df1 = podcast_similarities[podcast_similarities['podcast1']==row2['Podcast Name']].copy()
    df2 = podcast_similarities[podcast_similarities['podcast2']==row2['Podcast Name']].copy()
    df = pd.concat([df1, df2], ignore_index=True)
    df.sort_values(by='score', ascending=False, inplace=True)
    df.reset_index(inplace=True)
    for index1, row1 in df.iterrows():
        if(index1>8):
            continue
        if(row1['podcast1']==row2['Podcast Name']):
            podcast2 = row1['podcast2']
            
        else:
            podcast2 = row1['podcast1']
        for index3, row3 in podcast_info.iterrows():
            if(row3['Podcast Name']==podcast2):
                podcast2_id = index3-1
        index+=1
        if(row1['score']>0):
            similarities.loc[index] = [row2['Podcast Name'], podcast2, podcast2_id, row1['score']]


dict_list = similarities.to_dict(orient='records')


sim_dj=[]
for i in range(len(dict_list)):
    d = {}
    d['model'] = 'podcasts.Similar'
    d['pk'] = i
    d['fields'] = dict_list[i]
    sim_dj.append(d)

    
sim_dj


import json
with open('similarities.json', 'w') as outfile:
    json.dump(sim_dj, outfile)


#################################################################################################

guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)
G1 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())

pr = nx.pagerank(G1, weight='duration')
sorted_pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
df_sorted_pr = pd.DataFrame(sorted_pr)
sorted_pr_dict = {}
for index, row in df_sorted_pr.iterrows():
    sorted_pr_dict[row[0]] = index+1

save_obj(sorted_pr_dict, 'sorted_pr_dict')

hubs, authorities = nx.hits(G1)

sorted_hubs = sorted(hubs.items(), key=operator.itemgetter(1), reverse=True)
df_sorted_hubs = pd.DataFrame(sorted_hubs)
sorted_hubs_dict = {}
for index, row in df_sorted_hubs.iterrows():
    sorted_hubs_dict[row[0]] = index+1

sorted_authorities = sorted(authorities.items(), key=operator.itemgetter(1), reverse=True)
df_sorted_authorities = pd.DataFrame(sorted_authorities)
sorted_auths_dict = {}
for index, row in df_sorted_authorities.iterrows():
    sorted_auths_dict[row[0]] = index+1

G2 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())

sorted_close = sorted(nx.closeness_centrality(G2).items(), key=operator.itemgetter(1), reverse=True)
df_sorted_close = pd.DataFrame(sorted_close)
sorted_close_dict = {}
for index, row in df_sorted_close.iterrows():
    sorted_close_dict[row[0]] = index+1
print("Closeness Centrality Done")

sorted_bt = sorted(nx.betweenness_centrality(G2).items(), key=operator.itemgetter(1), reverse=True)
df_sorted_bt = pd.DataFrame(sorted_bt)
print("Betweenness Centrality Done")
sorted_bt_dict = {}
for index, row in df_sorted_bt.iterrows():
    sorted_bt_dict[row[0]] = index+1

sorted_degree = sorted(nx.degree_centrality(G2).items(), key=operator.itemgetter(1), reverse=True)
df_sorted_degree = pd.DataFrame(sorted_degree)
sorted_degree_dict = {}
for index, row in df_sorted_degree.iterrows():
    sorted_degree_dict[row[0]] = index+1

host_list = []
for index1, row1 in podcast_info.iterrows():
    hosts = ast.literal_eval(row1['Hosts'])
    for host in hosts:
        host_list.append(host)

host_list = set(host_list)
print("length of host list", len(host_list))

top_host_podcast = load_obj('top_host_podcast')
top_guest_podcast = load_obj('top_guest_podcast')

host_podcasts = load_obj('host_podcasts')
guest_podcasts = load_obj('guest_podcasts')

guest_list = list(top_guest_podcast.keys())

# top_ten_pr = [i[0] for i in sorted_pr][0:10]
# top_fifty_pr = [i[0] for i in sorted_pr][0:50]



# top_ten = pd.DataFrame(columns=['name', 'host_bool', 'host_podcast', 'guest_podcast'])
# top_ten['name'] = top_ten_pr

# top_fifty = pd.DataFrame(columns=['name', 'host_podcast', 'host_podcasts', 
#                                   'guest_podcast', 'guest_podcasts', 
#                                   'pr_rank', 'hub_rank', 'auth_rank',
#                                   'degree_rank', 'bt_rank', 'close_rank'])
# top_fifty['name'] = top_fifty_pr



all_people = pd.DataFrame(columns=['name', 'person_id', 'host_podcast', 'host_podcasts', 
                                  'guest_podcast', 'guest_podcasts', 
                                  'pr_rank', 'hub_rank', 'auth_rank',
                                  'degree_rank', 'bt_rank', 'close_rank'])
all_people['name'] = list(G2.nodes())

for index, row in all_people.iterrows():
    row['person_id'] = sorted_pr_dict[row['name']]-1
    row['pr_rank'] = sorted_pr_dict[row['name']]
    row['hub_rank'] = sorted_hubs_dict[row['name']]
    row['auth_rank'] = sorted_auths_dict[row['name']]
    row['degree_rank'] = sorted_degree_dict[row['name']]
    row['close_rank'] = sorted_close_dict[row['name']]
    row['bt_rank'] = sorted_bt_dict[row['name']]

    # for index1, value1 in df_sorted_hubs[0].iteritems():
    #     if(value1==row['name']):
    #         row['hub_rank'] = index1+1
    #         break
    # for index1, value1 in df_sorted_authorities[0].iteritems():
    #     if(value1==row['name']):
    #         row['auth_rank'] = index1+1
    #         break
    # for index1, value1 in df_sorted_degree[0].iteritems():
    #     if(value1==row['name']):
    #         row['degree_rank'] = index1+1
    #         break
    # for index1, value1 in df_sorted_close[0].iteritems():
    #     if(value1==row['name']):
    #         row['close_rank'] = index1+1
    #         break
    # for index1, value1 in df_sorted_bt[0].iteritems():
    #     if(value1==row['name']):
    #         row['bt_rank'] = index1+1
    #         break



    if(row['name'] in host_list):
        row['host_podcast'] = top_host_podcast[row['name']]
        row['host_podcasts'] = list(host_podcasts[row['name']])
    else:
        row['host_podcast'] = ''
        row['host_podcasts'] = ''
    if(row['name'] in guest_list):
        row['guest_podcast'] = top_guest_podcast[row['name']]
        row['guest_podcasts'] = list(guest_podcasts[row['name']])
    else:
        row['guest_podcast'] = ''
        row['guest_podcasts'] = ''


all_people.sort_values(by='pr_rank', inplace=True)


dict_list = all_people.to_dict(orient='records')
dict_list[1]

dj_list=[]
for i in range(len(all_people)):
    d = {}
    d['model'] = 'rankings.People'
    d['pk'] = i
    d['fields'] = dict_list[i]
    dj_list.append(d)

with open('all_people.json', 'w') as outfile:
    json.dump(dj_list, outfile)



# pr_top_hundred = [i[0] for i in sorted_pr][0:100]
# pr_top_hundred = pd.DataFrame(data=pr_top_hundred, columns=['name'])
# hub_top_hundred = [i[0] for i in sorted_hubs][0:100]
# hub_top_hundred = pd.DataFrame(data=hub_top_hundred, columns=['name'])
# auth_top_hundred = [i[0] for i in sorted_authorities][0:100]
# auth_top_hundred = pd.DataFrame(data=auth_top_hundred, columns=['name'])
# deg_top_hundred = [i[0] for i in sorted_degree][0:100]
# deg_top_hundred = pd.DataFrame(data=deg_top_hundred, columns=['name'])
# close_top_hundred = [i[0] for i in sorted_close][0:100]
# close_top_hundred = pd.DataFrame(data=close_top_hundred, columns=['name'])
# bt_top_hundred = [i[0] for i in sorted_bt][0:100]
# bt_top_hundred = pd.DataFrame(data=bt_top_hundred, columns=['name'])




# dict_list = pr_top_hundred.to_dict(orient='records')
# dict_list[1]

# dj_list=[]
# for i in range(len(pr_top_hundred)):
#     d = {}
#     d['model'] = 'rankings.Pr'
#     d['pk'] = i
#     d['fields'] = dict_list[i]
#     dj_list.append(d)

# with open('pr_top_hundred.json', 'w') as outfile:
#     json.dump(dj_list, outfile)




# dict_list = hub_top_hundred.to_dict(orient='records')
# dict_list[1]

# dj_list=[]
# for i in range(len(hub_top_hundred)):
#     d = {}
#     d['model'] = 'rankings.Hub'
#     d['pk'] = i
#     d['fields'] = dict_list[i]
#     dj_list.append(d)

# with open('hub_top_hundred.json', 'w') as outfile:
#     json.dump(dj_list, outfile)



# dict_list = auth_top_hundred.to_dict(orient='records')
# dict_list[1]

# dj_list=[]
# for i in range(len(auth_top_hundred)):
#     d = {}
#     d['model'] = 'rankings.Auth'
#     d['pk'] = i
#     d['fields'] = dict_list[i]
#     dj_list.append(d)

# with open('auth_top_hundred.json', 'w') as outfile:
#     json.dump(dj_list, outfile)





# dict_list = deg_top_hundred.to_dict(orient='records')
# dict_list[1]

# dj_list=[]
# for i in range(len(deg_top_hundred)):
#     d = {}
#     d['model'] = 'rankings.Deg'
#     d['pk'] = i
#     d['fields'] = dict_list[i]
#     dj_list.append(d)

# with open('deg_top_hundred.json', 'w') as outfile:
#     json.dump(dj_list, outfile)





# dict_list = close_top_hundred.to_dict(orient='records')
# dict_list[1]

# dj_list=[]
# for i in range(len(close_top_hundred)):
#     d = {}
#     d['model'] = 'rankings.Close'
#     d['pk'] = i
#     d['fields'] = dict_list[i]
#     dj_list.append(d)

# with open('close_top_hundred.json', 'w') as outfile:
#     json.dump(dj_list, outfile)




# dict_list = bt_top_hundred.to_dict(orient='records')
# dict_list[1]

# dj_list=[]
# for i in range(len(bt_top_hundred)):
#     d = {}
#     d['model'] = 'rankings.Bt'
#     d['pk'] = i
#     d['fields'] = dict_list[i]
#     dj_list.append(d)

# with open('bt_top_hundred.json', 'w') as outfile:
#     json.dump(dj_list, outfile)


#################################################################################################

def sec_to_hours(seconds):
    sec = timedelta(seconds=seconds)
    d = dt(1,1,1) + sec
    
    if (seconds == 2702145):
        return ('31:6:35:45')
    else:
        return("%02d:%02d:%02d:%02d" % (d.day-1, d.hour, d.minute, d.second))

guest_durations_podcast = pd.read_csv('../reading_and_cleaning/guest_durations_podcast.csv', sep='\t', index_col=0)

guest_durations_podcast['hours'] = ''
for index, row in guest_durations_podcast.iterrows():
    guest_durations_podcast.at[index, 'hours'] = sec_to_hours(row['duration'])

now = dt.now()

df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)

dates = [(dt.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in df1['date']]
sec_delta = [(now-date).total_seconds() for date in dates]
sec_delta
df1['sec_delta'] = sec_delta

guest_recent_date = df1.groupby(['podcast', 'podcast_id', 'guests']).agg({'sec_delta':['min', 'count'], 'date':'first'})
guest_recent_date = guest_recent_date.reset_index()

guest_durations_podcast['recent'] = guest_recent_date['date']
guest_durations_podcast['count'] = guest_recent_date['sec_delta']['count']

guest_durations_podcast['person_id'] = np.nan
for index, row in guest_durations_podcast.iterrows():
    guest_durations_podcast.at[index, 'person_id'] = sorted_pr_dict[row['guests']]-1


guest_durations_podcast.sort_values(by='duration', ascending=False, inplace=True)
guest_durations_podcast.drop(columns='duration', inplace=True)

dict_list = guest_durations_podcast.to_dict(orient='records')


gdp_dj=[]
for i in range(len(guest_durations_podcast)):
    d = {}
    d['model'] = 'rankings.Durations'
    d['pk'] = i
    d['fields'] = dict_list[i]
    gdp_dj.append(d)


import json
with open('guest_duration_podcast.json', 'w') as outfile:
    json.dump(gdp_dj, outfile)


#################################################################################################


podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)
df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)

d = {}
for index, row in podcast_info.iterrows():
    d[row['Podcast Name']]=index-1

save_obj(d, 'podcast_id')

df1['attr'] = 'guest'

G3 = nx.from_pandas_dataframe(df1, 'guests', 'podcast', edge_attr=['date', 'duration', 'attr'], create_using=nx.Graph())

podcast_info_split = splitDataFrameList(podcast_info, 'Hosts', ', ')
podcast_info_split['Hosts'] = [g.rstrip("'") for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = [g.rstrip('"') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = [g.rstrip(']') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = [g.rstrip("'") for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = [g.lstrip('"') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = [g.lstrip('[') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = [g.lstrip("'") for g in podcast_info_split['Hosts']]

podcast_info_split['attr'] = 'host'

G4 = nx.from_pandas_dataframe(podcast_info_split, 'Podcast Name', 'Hosts', edge_attr=['attr'], create_using=nx.Graph())

G3.add_edges_from(G4.edges(data=True))


nx.write_edgelist(G3, "six_degrees.edgelist", delimiter='\t')

correct_spellings = list(G1.nodes())

cr = pd.DataFrame(correct_spellings)
cr.to_csv('correct_spellings.csv', index=False)






