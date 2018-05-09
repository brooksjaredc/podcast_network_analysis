import pandas as pd
from urllib.request import Request, urlopen
import ast

podcast_info = pd.read_csv('meta_podcast_info.csv', sep='\t', index_col=0)

df = pd.DataFrame()
for index, row in podcast_info.iterrows():
    #print(row['cleaner'], row['feedURL'])
    if(row['cleaner']=='clean_chris_kresser'):
        req = Request(row['feedURL'], headers={'User-Agent': 'Mozilla/5.0'})
        df1 = locals()[row['cleaner']](urlopen(req))
    else:
        df1 = locals()[row['cleaner']](urlopen(row['feedURL']))
        
    hosts = ast.literal_eval(row['Hosts'])
    host_list = ''
    for host in hosts:
        host_list += host + ', '
    host_list = host_list.rstrip(', ')
    #print(host_list)
    df1['hosts'] = host_list
    df1['podcast'] = row['Podcast Name']
    df1['podcast_id']=index
    
    df = pd.concat([df, df1])


df0 = pd.read_csv('cleaned_podcasts.csv', sep='\t', index_col=0)

df_combine = pd.concat([df, df0], ignore_index=True)
df_combine.drop_duplicates(subset=['podcast', 'guests', 'duration', 'title'],inplace=True)

df_combine.to_csv('updated_cleaned_podcasts.csv', sep='\t')


