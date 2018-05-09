import pandas as pd
import networkx as nx


# def splitDataFrameList(df,target_column,separator):
# 	''' df = dataframe to split,
# 	target_column = the column containing the values to split
# 	separator = the symbol used to perform the split
# 	returns: a dataframe with each entry for the target column separated, with each element moved into a new row. 
# 	The values in the other columns are duplicated across the newly divided rows.
# 	'''
# 	def splitListToRows(row,row_accumulator,target_column,separator):
# 		split_row = row[target_column].split(separator)
# 		for s in split_row:
# 			new_row = row.to_dict()
# 			new_row[target_column] = s
# 			row_accumulator.append(new_row)
# 	new_rows = []
# 	df.apply(splitListToRows,axis=1,args = (new_rows,target_column,separator))
# 	new_df = pd.DataFrame(new_rows)
# 	return new_df



# df = pd.read_csv('../reading_and_cleaning/cleaned_podcasts.csv', sep='\t', index_col=0)
# df = df.replace(r'', np.nan, regex=True)
# df = df[pd.notnull(df['guests'])]
# split_hosts = splitDataFrameList(df, 'hosts', ', ')

#G1 = nx.from_pandas_dataframe(split_hosts, 'guests', 'hosts', edge_attr=['date', 'duration', 'podcast'], create_using=nx.MultiDiGraph())

# for index, row in split_hosts.iterrows():
#     if(row['hosts'] == row['guests']):
#         split_hosts.drop(index=index, inplace=True)

# guest_durations = split_hosts.groupby(['hosts', 'guests'])['duration'].sum()
# guest_durations = guest_durations.reset_index()

guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)

G1 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.DiGraph())


G2 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())

##################################################################################################################################

remove = [node for node,degree in G2.degree().items() if degree < 3]
G2.remove_nodes_from(remove)
#print(nx.number_of_nodes(G2))

remove = [node for node,degree in G1.degree().items() if degree < 3]
G1.remove_nodes_from(remove)
#print(nx.number_of_nodes(G1))

##################################################################################################################################

pr = nx.pagerank(G1, weight='duration')
hubs, authorities = nx.hits(G1)

nodes_df = pd.DataFrame.from_dict(pr, orient='index')
nodes_df.rename(columns = {0:'pr'}, inplace = True)
nodes_df['hub'] = hubs.values()
nodes_df['auth'] = authorities.values()

#print(len(nodes_df), len(nx.eccentricity(G2).values()))

nodes_df['eccentricity'] = nx.eccentricity(G2).values()
nodes_df['closeness'] = nx.closeness_centrality(G2).values()
nodes_df['betweenness'] = nx.betweenness_centrality(G2).values()
nodes_df['degree_cen'] = nx.degree_centrality(G2).values()
nodes_df['eigen'] = nx.eigenvector_centrality(G2).values()


nodes_df.to_csv('node_values.csv', sep='\t')
