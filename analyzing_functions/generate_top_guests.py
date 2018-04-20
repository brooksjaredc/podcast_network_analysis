import numpy as np
import pandas as pd
import ast

df = pd.read_csv('../reading_and_cleaning/cleaned_podcasts.csv', sep='\t', index_col=0)
podcast_info = pd.read_csv('../reading_and_cleaning/meta_podcast_info.csv', sep='\t', index_col=0)
df = df.replace(r'', np.nan, regex=True)
df = df[pd.notnull(df['guests'])]

for index1, row1 in podcast_info.iterrows():
    df1 = df[df['podcast'] == row1['Podcast Name']].copy()
    #print(df1.is_copy)
    hosts = ast.literal_eval(row1['Hosts'])
    #print(hosts[0])
    for host in hosts:
        #print(host)
        for index2, row2 in df1.iterrows():
            if(row2['guests'] == host):
                df1.drop(index=index2, inplace=True)
                #print('dropping', row2['guests'])
        #print(host)
    guest_durations1 = df1.groupby(['guests'])['duration'].sum()
    guest_durations1.sort_values(ascending=False, inplace=True)
    filename = 'top_guests/' + row1['Podcast Name'] + '.csv'
    guest_durations1.to_csv(filename)
    #print(row1['Podcast Name'], ' - ', guest_durations1.index[0], guest_durations1.values[0])