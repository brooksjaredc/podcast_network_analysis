import numpy as np
import pandas as pd
import networkx as nx
from nltk import jaccard_distance
import pickle

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

def ngrams_split(lst, n):
    counts = dict()
    grams = [''.join(lst[i:i+n]) for i in range(len(lst)-n+1)]
    for gram in grams:
        if gram not in counts:
            counts[gram] = 1
        else:
            counts[gram] += 1
    return set(grams)

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def word_search(target, words):
    low_score = 100
    prediction = ''
    words = [w for w in words if w[0]==target[0]]
    for i in range(len(words)):
        #test_word = list(words[i])
        score = jaccard_distance(ngrams_split(target,3), ngrams_split(words[i],3))   #levenshtein(target, words[i])
        if score<low_score:
            low_score=score
            #print(low_score)
            prediction = words[i]
            #print(words[i])
    return prediction#, low_score





podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)
df1 = pd.read_csv('../reading_and_cleaning/guest_host_cleaned_podcasts.csv', sep='\t', index_col=0)

d = {}
for index, row in podcast_info.iterrows():
    d[row['Podcast Name']]=index-1

save_obj(d, 'podcast_id')

df1['attr'] = 'guest'

# df1['link'] = ''

# for index1, row1 in df1.iterrows():
    # df1.at[index1, 'link']= '<a href="/podcasts/' + str(d[row1['podcast']]) + '/">' + row1['podcast'] + "</a>"

G3 = nx.from_pandas_dataframe(df1, 'guests', 'podcast', edge_attr=['date', 'duration', 'attr'], create_using=nx.Graph())



# podcast_info['link'] = '<a href="/podcasts/' + str(podcast_info.index - 1) + '/">' + podcast_info['Podcast Name'] + "</a>"

# podcast_info['link'] = ''
# for index1, row1 in podcast_info.iterrows():
#     podcast_info.at[index1, 'link']='<a href="/podcasts/' + str(index1 - 1) + '/">' + row1['Podcast Name'] + "</a>"

# print(podcast_info['link'][1])

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

import csv

G3 = nx.read_edgelist("six_degrees.edgelist", delimiter='\t')

correct_spellings = []
with open("correct_spellings.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter='\t')
    for row in reader:
        correct_spellings.append(row[0])

# print(correct_spellings)

#print(G3.nodes()[0],G3.nodes()[1])

def six_degrees(node1, node2):
    
    if(node1 not in correct_spellings):
        suggestion = word_search(node1, correct_spellings)
        message = "Sorry, we couldn't find " + node1 + " in our database. Did you mean " + suggestion + "?"
    elif (node2 not in correct_spellings):
        suggestion = word_search(node2, correct_spellings)
        message = "Sorry, we couldn't find " + node2 + " in our database. Did you mean " + suggestion + "?"
    else:
    
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

print(six_degrees('Steve-O', 'Ari Shaffir'))
