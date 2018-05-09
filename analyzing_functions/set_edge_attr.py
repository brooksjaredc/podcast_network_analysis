import pandas as pd
import networkx as nx
import pickle

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)



guest_durations = pd.read_csv('../reading_and_cleaning/guest_durations.csv', sep='\t', index_col=0)

G2 = nx.from_pandas_dataframe(guest_durations, 'guests', 'hosts', edge_attr=['duration'], create_using=nx.Graph())

##################################################################################################################################

remove = [node for node,degree in G2.degree().items() if degree < 3]
G2.remove_nodes_from(remove)
print(nx.number_of_nodes(G2))

##################################################################################################################################

top_cat = load_obj('top_categories')
top_cat_num = pd.DataFrame.from_dict(top_cat, orient='index')
top_cat_num = top_cat_num[0].astype('category').cat.codes.to_dict()



# #nx.set_node_attributes(G2, 'cat', top_cat)
nx.set_node_attributes(G2, 'cat', '')



for node in G2.nodes():
    #print(top_cat[node])
    G2.node[node]['cat'] = top_cat[node]


print(nx.number_of_nodes(G2))

edges_df = pd.DataFrame(columns=['node1', 'node2', 'resource', 'jaccard', 'adamic', 'preferential', 'jaccard', 'cn_sh', 'ra_sh', 'within'])

resource = list(nx.resource_allocation_index(G2))

edges_df['node1'] = [x[0] for x in resource]
edges_df['node2'] = [x[1] for x in resource]

edges_df['resource'] = [x[2] for x in resource]
edges_df['jaccard'] = [x[2] for x in nx.jaccard_coefficient(G2)]
edges_df['adamic'] = [x[2] for x in nx.adamic_adar_index(G2)]
edges_df['preferential'] = [x[2] for x in nx.preferential_attachment(G2)]
edges_df['jaccard'] = [x[2] for x in nx.jaccard_coefficient(G2)]

edges_df['cn_sh'] = [x[2] for x in nx.cn_soundarajan_hopcroft(G2, community='cat')]
edges_df['ra_sh'] = [x[2] for x in nx.ra_index_soundarajan_hopcroft(G2, community='cat')]
edges_df['within'] = [x[2] for x in nx.within_inter_cluster(G2, community='cat')]

edges_df.to_csv('edge_values.csv', sep='\t')
