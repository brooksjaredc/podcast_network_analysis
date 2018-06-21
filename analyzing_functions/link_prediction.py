import pandas as pd
import numpy as np
import networkx as nx
import pickle
import ast
from datetime import datetime as dt


def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

# node_values = pd.read_csv('node_values.csv', sep='\t', index_col=0)
# edge_values = pd.read_csv('edge_values.csv', sep='\t', index_col=0)

# edge_values['node1 pr'] = ''
# edge_values['node1 auth'] = ''
# edge_values['node1 hub'] = ''
# edge_values['node1 ecc'] = ''
# edge_values['node1 close'] = ''
# edge_values['node1 between'] = ''
# edge_values['node1 deg'] = ''
# edge_values['node1 eigen'] = ''

# edge_values['node2 pr'] = ''
# edge_values['node2 auth'] = ''
# edge_values['node2 hub'] = ''
# edge_values['node2 ecc'] = ''
# edge_values['node2 close'] = ''
# edge_values['node2 between'] = ''
# edge_values['node2 deg'] = ''
# edge_values['node2 eigen'] = ''



# for index1, row1 in edge_values.iterrows():
# 	for index2, row2 in node_values.iterrows():
# 		if(row1['node1']==index2):
# 			row1['node1 pr'] = row2['pr']
# 			row1['node1 auth'] = row2['auth']
# 			row1['node1 hub'] = row2['hub']
# 			row1['node1 ecc'] = row2['eccentricity']
# 			row1['node1 close'] = row2['closeness']
# 			row1['node1 between'] = row2['betweenness']
# 			row1['node1 deg'] = row2['degree_cen']
# 			row1['node1 eigen'] = row2['eigen']
# 		if(row1['node2']==index2):
# 			row1['node2 pr'] = row2['pr']
# 			row1['node2 auth'] = row2['auth']
# 			row1['node2 hub'] = row2['hub']
# 			row1['node2 ecc'] = row2['eccentricity']
# 			row1['node2 close'] = row2['closeness']
# 			row1['node2 between'] = row2['betweenness']
# 			row1['node2 deg'] = row2['degree_cen']
# 			row1['node2 eigen'] = row2['eigen']

# edge_values.to_csv('link_prediction_small.csv', sep='\t')

# df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)

# df1['attr'] = 'guest'

guest_durations_podcast = pd.read_csv('../reading_and_cleaning/guest_durations_podcast.csv', sep='\t', index_col=0)

df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)

start = dt(2017, 1, 1)
end = dt(2018, 1, 1)

df1['date'] = pd.to_datetime(df1['date'])
df1.sort_values(by='date', inplace=True)
df1.reset_index(inplace=True, drop=True)
dates = [x for x in df1['date']]

valid_dates_start = [(d < start) for d in dates]
start_df = df1[valid_dates_start]
start_df.reset_index(inplace=True, drop=True)

valid_dates_end = [(d < end) for d in dates]
end_df = df1[valid_dates_end]
end_df.reset_index(inplace=True, drop=True)

guest_durations_start = start_df.groupby(['podcast', 'guests'])['duration'].sum()
guest_durations_start = guest_durations_start.reset_index()


guest_durations_end = end_df.groupby(['podcast', 'guests'])['duration'].sum()
guest_durations_end = guest_durations_end.reset_index()

G_train = nx.from_pandas_dataframe(guest_durations_start, 'guests', 'podcast', edge_attr=['duration'], create_using=nx.Graph())
G_test = nx.from_pandas_dataframe(guest_durations_end, 'guests', 'podcast', edge_attr=['duration'], create_using=nx.Graph())
train_edges = G_train.edges()
true_edges = G_test.edges()

# i=0
# for edge in true_edges:
# 	if(edge not in train_edges):
# 		# print(edge)
# 		i+=1
# print('num new edges', i)

p_info = pd.read_csv('p_info.csv', sep='\t', index_col=0)
p_close = load_obj('p_close')
p_bt = load_obj('p_bt')
p_degree = load_obj('p_degree')

# guest_durations_podcast = pd.read_csv('../reading_and_cleaning/guest_durations_podcast.csv', sep='\t', index_col=0)
top_cat_dict = load_obj('top_categories')
g_pr = load_obj('g_pr')
g_hubs = load_obj('g_hubs')
g_auths = load_obj('g_auths')
g_close = load_obj('g_close')
g_bt = load_obj('g_bt')
g_degree = load_obj('g_degree')

people = set(start_df['guests'])
print(len(people))
podcasts = set(start_df['podcast'])
print(len(podcasts))

top_cat = load_obj('top_categories')

train_nodes = G_train.nodes()
top_cat_train = {}
for node in train_nodes:
	if(node in people):
		top_cat_train[node] = top_cat[node]

nx.set_node_attributes(G_train, 'cat', top_cat_train)

top_cat_pod = {}
for index, row in p_info.iterrows():
	cats = ast.literal_eval(row['categories'])
	if(row['name'] in podcasts):
		top_cat_pod[row['name']] = cats[0]


nx.set_node_attributes(G_train, 'cat', top_cat_pod)

link_pred_data = pd.DataFrame(columns=['podcast', 'guest', 'num_guests', 'percent_unique', 'avg_day_diff', 'same_cat', 
										'cat_bias', 'p_close', 'p_bt', 'p_degree',
										'g_pr', 'g_hubs', 'g_auths', 'g_close', 'g_bt', 'g_degree',
										'ra', 'ja', 'ad', 'pa', 'cn_sh', 'ra_sh', 'wic',
										'guest_dur', 'host_dur',
										'future_link'])
i=0
for index, row in p_info.iterrows():
	if(not row['active']):
		continue
	# if(row['name']!='The Joe Rogan Experience'):
	# 	break
	print(row['name'])
	podcast_df = guest_durations_start[guest_durations_start['podcast']==row['name']].copy()
	cats = ast.literal_eval(row['categories'])
	hosts = ast.literal_eval(row['hosts'])
	top_cat_podcast = cats[0]
	for person in people:
		if(person not in list(podcast_df['guests'])):
			link_pred_data.at[i, 'podcast']=row['name']
			link_pred_data.at[i, 'guest']=person
			link_pred_data.at[i, 'num_guests']=row['num_guests']
			link_pred_data.at[i, 'percent_unique']=row['percent_unique']
			link_pred_data.at[i, 'avg_day_diff']=row['avg_day_diff']
			link_pred_data.at[i, 'cat_bias']=row['cat_bias']
			link_pred_data.at[i, 'p_close']=p_close[row['name']]
			link_pred_data.at[i, 'p_bt']=p_bt[row['name']]
			link_pred_data.at[i, 'p_degree']=p_degree[row['name']]

			if(top_cat_podcast==top_cat_dict[person]):
				link_pred_data.at[i, 'same_cat']=1
			else:
				link_pred_data.at[i, 'same_cat']=0

			link_pred_data.at[i, 'g_pr']=g_pr[person]
			link_pred_data.at[i, 'g_hubs']=g_hubs[person]
			link_pred_data.at[i, 'g_auths']=g_auths[person]
			link_pred_data.at[i, 'g_close']=g_close[person]
			link_pred_data.at[i, 'g_bt']=g_bt[person]
			link_pred_data.at[i, 'g_degree']=g_degree[person]

			ra = 0.0
			ja = 0.0
			ad = 0.0
			pa = 0.0

			cn_sh = 0.0
			ra_sh = 0.0
			wic = 0.0

			guest_dur = 0.0
			host_dur = 0.0
			for person1 in list(podcast_df['guests']):
				# print(list(nx.resource_allocation_index(G_train, [(person, person1)])))
				ra += list(nx.resource_allocation_index(G_train, [(person, person1)]))[0][2]
				ja += list(nx.jaccard_coefficient(G_train, [(person, person1)]))[0][2]
				ad += list(nx.adamic_adar_index(G_train, [(person, person1)]))[0][2]
				pa += list(nx.preferential_attachment(G_train, [(person, person1)]))[0][2]

				cn_sh += list(nx.cn_soundarajan_hopcroft(G_train, [(person, person1)], community='cat'))[0][2]
				ra_sh += list(nx.ra_index_soundarajan_hopcroft(G_train, [(person, person1)], community='cat'))[0][2]
				wic += list(nx.within_inter_cluster(G_train, [(person, person1)], community='cat'))[0][2]
				for podcast in list(nx.common_neighbors(G_train, person, person1)):
					guest_dur += G_train[person][podcast]['duration']*G_train[person1][podcast]['duration']
			for host in hosts:
				if(host in people):
					for podcast in list(nx.common_neighbors(G_train, person, host)):
						host_dur +=  G_train[person][podcast]['duration']*G_train[host][podcast]['duration']

			link_pred_data.at[i, 'ra'] = ra
			link_pred_data.at[i, 'ja'] = ja
			link_pred_data.at[i, 'ad'] = ad
			link_pred_data.at[i, 'pa'] = pa
			link_pred_data.at[i, 'cn_sh'] = cn_sh
			link_pred_data.at[i, 'ra_sh'] = ra_sh
			link_pred_data.at[i, 'wic'] = wic

			link_pred_data.at[i, 'guest_dur'] = guest_dur
			link_pred_data.at[i, 'host_dur'] = host_dur


			if(((row['name'], person) in true_edges) or ((person, row['name']) in true_edges)):
				link_pred_data.at[i, 'future_link'] = 1
				print(row['name'], person)
			else:
				link_pred_data.at[i, 'future_link'] = 0

			i+=1
			if(np.mod(i,1000)==0):
				print(i, wic)


		# else:
		# 	print(person)




link_pred_data.to_csv('link_pred_data.csv', sep='\t')




