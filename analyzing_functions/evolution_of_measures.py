import pandas as pd
import networkx as nx
import operator
from datetime import datetime as dt


#guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)
split_hosts = pd.read_csv('../reading_and_cleaning/split_hosts.csv', sep='\t', index_col=0)


date_list = [dt(int(2010+(x/12)-(x%12)/12), x%12+1, 1) for x in range(0, 101)]

dates = [(dt.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in split_hosts['date']]

measures = pd.DataFrame(columns=['avg_clust', 'transitivity', 'avg_path', 'density', 'dates'])
measures['dates'] = date_list


i=0
for date in date_list:
    valid_dates = [(d < date) for d in dates]
    df1 = split_hosts[valid_dates]
    guest_durations1 = df1.groupby(['hosts', 'guests'])['duration'].sum()
    guest_durations1 = guest_durations1.reset_index()
    # G1_1 = nx.from_pandas_dataframe(guest_durations1, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())
    # pr1 = nx.pagerank(G1_1, weight='duration')

    G2_1 = nx.from_pandas_dataframe(guest_durations1, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())

    if(nx.is_connected(G2_1)):
        measures['avg_clust'].iloc[i] = nx.average_clustering(G2_1)
        measures['transitivity'].iloc[i] = nx.transitivity(G2_1)
        measures['avg_path'].iloc[i] = nx.average_shortest_path_length(G2_1)
        measures['density'].iloc[i] = nx.density(G2_1)
    else:
        largest_cc = max(nx.connected_component_subgraphs(G2_1), key=len)

        measures['avg_clust'].iloc[i] = nx.average_clustering(largest_cc)
        measures['transitivity'].iloc[i] = nx.transitivity(largest_cc)
        measures['avg_path'].iloc[i] = nx.average_shortest_path_length(largest_cc)
        measures['density'].iloc[i] = nx.density(largest_cc)

    # for index, row in top_ten_pr.iterrows():
    # 	if(date > row['dates']):
    # 		pr_evol[row['names']].iloc[i] = pr1[row['names']]
    # 		close_evol[row['names']].iloc[i] = close1[row['names']]
    # 	else:
    # 		pr_evol[row['names']].iloc[i] = 0
    # 		close_evol[row['names']].iloc[i] = 0
    i+=1



measures.to_csv('evolution_of_measures.csv', sep='\t')