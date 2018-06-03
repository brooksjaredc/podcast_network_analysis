import numpy as np
import pandas as pd
import ast

from cleaning_functions import splitDataFrameList

df = pd.read_csv('cleaned_podcasts.csv', sep='\t', index_col=0)
podcast_info = pd.read_csv('meta_podcast_info.csv', sep='\t', index_col=0)
df = df.replace(r'', np.nan, regex=True)
df = df[pd.notnull(df['guests'])]


df1 = df
for index1, row1 in podcast_info.iterrows():
    #df1 = df[df['podcast'] == row1['Podcast Name']].copy()
    #print(df1.is_copy)
    hosts = ast.literal_eval(row1['Hosts'])
    #print(hosts[0])
    for host in hosts:
        print(host)
        for index2, row2 in df1.iterrows():
            if(row2['podcast'] == row1['Podcast Name'] and row2['guests'] == host):
                df1.drop(index=index2, inplace=True)


df1.to_csv('guest_host_cleaned_podcasts.csv', sep='\t')






split_hosts = splitDataFrameList(df1, 'hosts', ', ')

for index, row in split_hosts.iterrows():
    if(row['hosts'] == row['guests']):
        split_hosts.drop(index=index, inplace=True)

split_hosts.to_csv('split_hosts.csv', sep='\t')



guest_durations_podcast = df1.groupby(['podcast', 'guests']).agg({'duration':'sum', 'podcast_id':'first'})
guest_durations_podcast = guest_durations_podcast.reset_index()

# guest_recent_date = df1.groupby(['podcast', 'podcast_id', 'guests'])['duration'].sum()
# guest_recent_date = guest_recent_date.reset_index()

guest_durations = split_hosts.groupby(['hosts', 'guests'])['duration'].sum()
guest_durations = guest_durations.reset_index()

guest_durations.to_csv('guest_durations.csv', sep='\t')
guest_durations_podcast.to_csv('guest_durations_podcast.csv', sep='\t')