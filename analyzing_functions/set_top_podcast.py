import pandas as pd
import networkx as nx
import pickle
import ast

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)
split_hosts = pd.read_csv('../reading_and_cleaning/split_hosts.csv', sep='\t', index_col=0)
guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)
G2 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())

podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)
host_list = []
for index1, row1 in podcast_info.iterrows():
    hosts = ast.literal_eval(row1['Hosts'])
    for host in hosts:
        host_list.append(host)

host_list = set(host_list)


top_host_podcast = {}
top_guest_podcast = {}

host_podcasts = {}
guest_podcasts = {}

for node in G2.nodes():
    if node in host_list:
        #print(node)
        df = split_hosts[split_hosts['hosts']==node]
        host_durations = df.groupby(['podcast'])['duration'].sum()
        host_durations = host_durations.reset_index()
        host_durations = host_durations.sort_values(by='duration', ascending=False)
        #print(host_durations['podcast'])
        #top_podcast = host_durations['podcast'][0]
        top_host_podcast[node] = host_durations['podcast'][0]
        host_podcasts[node] = host_durations['podcast'].values
        #print(host_durations['podcast'].values)
        # for index, row in podcast_info.iterrows():
        #     if(row['Podcast Name']==top_podcast):
        #         top_cat = ast.literal_eval(row['categories'])[0]
        #         top_category[node] = top_cat
                #print(node, top_cat)

    df = df1[df1['guests']==node]
    guest_durations = df.groupby(['podcast'])['duration'].sum()
    guest_durations = guest_durations.reset_index()
    guest_durations = guest_durations.sort_values(by='duration', ascending=False)
    #top_podcast = guest_durations['podcast'][0]
    if(len(guest_durations)==0):
        continue
    top_guest_podcast[node] = guest_durations['podcast'].iloc[0]
    guest_podcasts[node] = guest_durations['podcast'].values
        # for index, row in podcast_info.iterrows():
        #     if(row['Podcast Name']==top_podcast):
        #         top_cat = ast.literal_eval(row['categories'])[0]
        #         top_category[node] = top_cat

save_obj(top_host_podcast, 'top_host_podcast')
save_obj(top_guest_podcast, 'top_guest_podcast')

save_obj(host_podcasts, 'host_podcasts')
save_obj(guest_podcasts, 'guest_podcasts')

