import numpy as np
import pandas as pd
import networkx as nx

df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)

df1['attr'] = 'guest'

G3 = nx.from_pandas_dataframe(df1, 'guests', 'podcast', edge_attr=['date', 'duration', 'attr'], create_using=nx.Graph())

podcast_info_split = splitDataFrameList(podcast_info, 'Hosts', ', ')
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.rstrip("'") for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.rstrip('"') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.rstrip(']') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.rstrip("'") for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.lstrip('"') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.lstrip('[') for g in podcast_info_split['Hosts']]
podcast_info_split['Hosts'] = podcast_info_split['Hosts'] = [g.lstrip("'") for g in podcast_info_split['Hosts']]

podcast_info_split['attr'] = 'host'
G4 = nx.from_pandas_dataframe(podcast_info_split, 'Podcast Name', 'Hosts', edge_attr=['attr'], create_using=nx.Graph())

G3.add_edges_from(G4.edges(data=True))

def six_degrees(node1, node2):
    path = nx.shortest_path(G3, node1, node2)
    path_length = nx.shortest_path_length(G3, node1, node2)
    message = node1
    #message = '<a target="_blank" href="">' + node1 + '</a>'
    
    for step in range(path_length+1):
        print(step, path[step])
        if(step==0):
            continue
        if(step==1):
            if(G3[node1][path[1]]['attr'] == 'host'):
                message += ' is a host of '
            else:
                message += ' was a guest on '
            
            message += path[1]
            #message += '<a target="_blank" href="">' + path[1] + '</a>'
            continue
        if(step % 2 == 0):
            if(G3[path[step-1]][path[step]]['attr']=='guest'):
                if(step==2):
                    message += ', who had as a guest ' + path[step]
                    #message += ', who had as a guest ' + '<a target="_blank" href="">' + path[step] + '</a>'
                else:
                    message += ', who also had as a guest ' + path[step]
                    #message += ', who also had as a guest ' + '<a target="_blank" href="">' + path[step] + '</a>'
            if(G3[path[step-1]][path[step]]['attr']=='host'):
                message += ', which is hosted by ' + path[step]
                #message += ', which is hosted by ' + '<a target="_blank" href="">' + path[step] + '</a>'
        if(step % 2 == 1):
            message += ', who was a guest on ' + path[step]
            #message += ', who was a guest on ' + '<a target="_blank" href="">' + path[step] + '</a>'

    return message


