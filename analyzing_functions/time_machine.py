import pandas as pd
import networkx as nx
import operator
import ast
import pickle
from datetime import datetime as dt
# from split_hosts_guest_durations import split_hosts

podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)
host_list = []
for index1, row1 in podcast_info.iterrows():
    hosts = ast.literal_eval(row1['Hosts'])
    for host in hosts:
        host_list.append(host)

host_list = set(host_list)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

top_guest_podcast = load_obj('top_guest_podcast')
guest_list = list(top_guest_podcast.keys())

split_hosts = pd.read_csv('../reading_and_cleaning/split_hosts.csv', sep='\t', index_col=0)
split_hosts['date'] = pd.to_datetime(split_hosts['date'])
split_hosts.sort_values(by='date', inplace=True)


guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)
G1 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())
pr = nx.pagerank(G1, weight='duration')
sorted_pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
hubs, authorities = nx.hits(G1)
sorted_hub = sorted(hubs.items(), key=operator.itemgetter(1), reverse=True)
sorted_authorities = sorted(authorities.items(), key=operator.itemgetter(1), reverse=True)

G2 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())
# close = nx.closeness_centrality(G2)
# sorted_close = sorted(close.items(), key=operator.itemgetter(1), reverse=True)

# bt = nx.betweenness_centrality(G2)
# sorted_bt = sorted(bt.items(), key=operator.itemgetter(1), reverse=True)

top_ten_pr = [i[0] for i in sorted_pr][0:10]
top_ten_hub = [i[0] for i in sorted_hub][0:10]
top_ten_auth = [i[0] for i in sorted_authorities][0:10]
# top_ten_close = [i[0] for i in sorted_close][0:10]
# top_ten_bt = [i[0] for i in sorted_bt][0:10]
top_ten_close = []
top_ten_bt = []

print(top_ten_pr)

centralities = ['pr', 'hub', 'auth', 'close', 'bt']
top_ten_lists = [top_ten_pr, top_ten_hub, top_ten_auth, top_ten_close, top_ten_bt]
print(top_ten_lists[0][0])
# j=0
# for ten in top_ten_lists:
for j in range(5):
    print(top_ten_lists[j], centralities[j], j)
    top_ten = top_ten_lists[j]
    first_dates = []
    for i in top_ten:
        # host_first = dt.strptime(split_hosts[split_hosts['hosts']==i]['date'].iloc[-1], '%Y-%m-%d %H:%M:%S')
        # guest_first = dt.strptime(split_hosts[split_hosts['guests']==i]['date'].iloc[-1], '%Y-%m-%d %H:%M:%S')
        not_guest = False
        if(i in guest_list):
            guest_first = split_hosts[split_hosts['guests']==i]['date'].iloc[0]
        else:
            not_guest = True
        if(i in host_list):
            host_first = split_hosts[split_hosts['hosts']==i]['date'].iloc[0]
            if(not_guest):
                first_dates.append(host_first)
            elif(guest_first < host_first):
                first_dates.append(guest_first)
            else:
                first_dates.append(host_first)
        else:
            first_dates.append(guest_first)

    print(first_dates)
    
    top_ten_df = pd.DataFrame()
    top_ten_df['names'] = top_ten
    #first_dates = [(dt.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in first_dates]
    top_ten_df['dates'] = first_dates
    
    date_list = [dt(int(2010+(x/12)-(x%12)/12), x%12+1, 1) for x in range(0, 101)]
    
    # dates = [(dt.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in split_hosts['date']]
    dates = [x for x in split_hosts['date']]
    
    cols = top_ten + ['dates']
    evol = pd.DataFrame(columns=cols)
    evol['dates'] = date_list
    
    # close_evol = pd.DataFrame(columns=cols)
    # close_evol['dates'] = date_list
    
    i=0
    for date in date_list:
        valid_dates = [(d < date) for d in dates]
        df1 = split_hosts[valid_dates]
        guest_durations1 = df1.groupby(['hosts', 'guests'])['duration'].sum()
        guest_durations1 = guest_durations1.reset_index()

        if(j==0 or j==1 or j==2):
            G1_1 = nx.from_pandas_dataframe(guest_durations1, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())
            if(j==0):
                pr1 = nx.pagerank(G1_1, weight='duration')
                scores = pr1
            else:
                hubs1, auths1 = nx.hits(G1_1, max_iter=500)
                if(j==1):
                    scores = hubs1
                if(j==2):
                    scores = auths1
        if(j==3 or j==4):
            G2_1 = nx.from_pandas_dataframe(guest_durations1, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())
            if(j==3):
                close1 = nx.closeness_centrality(G2_1)
                scores = close1
            if(j==4):
                bt1 = nx.betweenness_centrality(G2_1)
                scores = bt1
        for index, row in top_ten_df.iterrows():
            if(date > row['dates']):
                evol[row['names']].iloc[i] = scores[row['names']]
            else:
                evol[row['names']].iloc[i] = 0
        i+=1
    
    filename = centralities[j] + '_evol.csv'
    print(filename)
    evol.to_csv(filename, sep='\t')
    # j+=1

# close_evol.to_csv('pr_evol.csv', sep='\t')
