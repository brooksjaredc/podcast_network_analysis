import pandas as pd
import networkx as nx
import operator
import ast
from datetime import datetime as dt
# from split_hosts_guest_durations import split_hosts

podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)
host_list = []
for index1, row1 in podcast_info.iterrows():
    hosts = ast.literal_eval(row1['Hosts'])
    for host in hosts:
        host_list.append(host)

host_list = set(host_list)

split_hosts = pd.read_csv('../reading_and_cleaning/split_hosts.csv', sep='\t', index_col=0)
split_hosts['date'] = pd.to_datetime(split_hosts['date'])
split_hosts.sort_values(by='date', inplace=True)
# guest_durations = split_hosts.groupby(['hosts', 'guests'])['duration'].sum()
# guest_durations = guest_durations.reset_index()

guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)
G1 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())
# pr = nx.pagerank(G1, weight='duration')
# sorted_pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
hubs, authorities = nx.hits(G1)
sorted_authorities = sorted(authorities.items(), key=operator.itemgetter(1), reverse=True)

# G2 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())
# close = nx.closeness_centrality(G2)
# sorted_close = sorted(close.items(), key=operator.itemgetter(1), reverse=True)

top_ten = [i[0] for i in sorted_authorities][0:10]
# top_ten = [i[0] for i in sorted_close][0:10]

first_dates = []
for i in top_ten:
    # host_first = dt.strptime(split_hosts[split_hosts['hosts']==i]['date'].iloc[-1], '%Y-%m-%d %H:%M:%S')
    # guest_first = dt.strptime(split_hosts[split_hosts['guests']==i]['date'].iloc[-1], '%Y-%m-%d %H:%M:%S')
    guest_first = split_hosts[split_hosts['guests']==i]['date'].iloc[0]
    if(i in host_list):
        host_first = split_hosts[split_hosts['hosts']==i]['date'].iloc[0]
        if(guest_first < host_first):
            first_dates.append(guest_first)
        else:
            first_dates.append(host_first)
    else:
        first_dates.append(guest_first)

print(first_dates)

top_ten_pr = pd.DataFrame()
top_ten_pr['names'] = top_ten
#first_dates = [(dt.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in first_dates]
top_ten_pr['dates'] = first_dates

date_list = [dt(int(2010+(x/12)-(x%12)/12), x%12+1, 1) for x in range(0, 101)]

# dates = [(dt.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in split_hosts['date']]
dates = [x for x in split_hosts['date']]

cols = top_ten + ['dates']
pr_evol = pd.DataFrame(columns=cols)
pr_evol['dates'] = date_list

# close_evol = pd.DataFrame(columns=cols)
# close_evol['dates'] = date_list

i=0
for date in date_list:
    valid_dates = [(d < date) for d in dates]
    df1 = split_hosts[valid_dates]
    guest_durations1 = df1.groupby(['hosts', 'guests'])['duration'].sum()
    guest_durations1 = guest_durations1.reset_index()
    G1_1 = nx.from_pandas_dataframe(guest_durations1, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())
    # pr1 = nx.pagerank(G1_1, weight='duration')
    hubs1, auths1 = nx.hits(G1_1, max_iter=500)

    # G2_1 = nx.from_pandas_dataframe(guest_durations1, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())
    # close1 = nx.closeness_centrality(G2_1)
    for index, row in top_ten_pr.iterrows():
    	if(date > row['dates']):
    		pr_evol[row['names']].iloc[i] = auths1[row['names']]
    		# close_evol[row['names']].iloc[i] = close1[row['names']]
    	else:
    		pr_evol[row['names']].iloc[i] = 0
    		# close_evol[row['names']].iloc[i] = 0
    i+=1


pr_evol.to_csv('auths_evol.csv', sep='\t')

# close_evol.to_csv('pr_evol.csv', sep='\t')
