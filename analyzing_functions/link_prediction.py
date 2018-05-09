import pandas as pd

node_values = pd.read_csv('node_values.csv', sep='\t', index_col=0)
edge_values = pd.read_csv('edge_values.csv', sep='\t', index_col=0)

edge_values['node1 pr'] = ''
edge_values['node1 auth'] = ''
edge_values['node1 hub'] = ''
edge_values['node1 ecc'] = ''
edge_values['node1 close'] = ''
edge_values['node1 between'] = ''
edge_values['node1 deg'] = ''
edge_values['node1 eigen'] = ''

edge_values['node2 pr'] = ''
edge_values['node2 auth'] = ''
edge_values['node2 hub'] = ''
edge_values['node2 ecc'] = ''
edge_values['node2 close'] = ''
edge_values['node2 between'] = ''
edge_values['node2 deg'] = ''
edge_values['node2 eigen'] = ''



for index1, row1 in edge_values.iterrows():
	for index2, row2 in node_values.iterrows():
		if(row1['node1']==index2):
			row1['node1 pr'] = row2['pr']
			row1['node1 auth'] = row2['auth']
			row1['node1 hub'] = row2['hub']
			row1['node1 ecc'] = row2['eccentricity']
			row1['node1 close'] = row2['closeness']
			row1['node1 between'] = row2['betweenness']
			row1['node1 deg'] = row2['degree_cen']
			row1['node1 eigen'] = row2['eigen']
		if(row1['node2']==index2):
			row1['node2 pr'] = row2['pr']
			row1['node2 auth'] = row2['auth']
			row1['node2 hub'] = row2['hub']
			row1['node2 ecc'] = row2['eccentricity']
			row1['node2 close'] = row2['closeness']
			row1['node2 between'] = row2['betweenness']
			row1['node2 deg'] = row2['degree_cen']
			row1['node2 eigen'] = row2['eigen']

edge_values.to_csv('link_prediction_small.csv', sep='\t')