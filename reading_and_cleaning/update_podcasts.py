import pandas as pd
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import ast
from cleaners import *

def get_desc(filename):
    e = ET.parse(filename).getroot()
    for channel in e.iter('channel'):
        return(channel.find('description').text)

podcast_info = pd.read_csv('meta_podcast_info.csv', sep='\t', index_col=0)
podcast_info['description'] = ''


df = pd.DataFrame()
for index, row in podcast_info.iterrows():
    print(row['cleaner'], row['feedURL'])
    # if(row['cleaner']!='clean_joe_rogan'):
    #     continue
    if(row['cleaner']=='clean_kill_tony'):
        continue
    if(row['cleaner']=='clean_rap_radar'):
        continue
    # if(row['cleaner']==r'(clean_chris_kresser|clean_new_books_econ)'):
    req = Request(row['feedURL'], headers={'User-Agent': 'Mozilla/5.0'})
    row['description'] = get_desc(urlopen(req, timeout=100))

    df1 = locals()[row['cleaner']](urlopen(req, timeout=100))
    # else:
    #     df1 = locals()[row['cleaner']](urlopen(row['feedURL']))
    hosts = ast.literal_eval(row['Hosts'])
    host_list = ''
    for host in hosts:
        host_list += host + ', '
    host_list = host_list.rstrip(', ')
    #print(host_list)
    df1['hosts'] = host_list
    df1['podcast'] = row['Podcast Name']
    df1['podcast_id']=index-1
    
    df = pd.concat([df, df1], ignore_index=True)


df['guests'] = [g.rstrip() for g in df['guests']]
df['guests'] = [g.lstrip() for g in df['guests']]

df['guests'] = [g.rstrip(' ') for g in df['guests']]
df['guests'] = [g.lstrip(' ') for g in df['guests']]

# df = pd.read_csv('cleaned_podcasts.csv', sep='\t', index_col=0)

remove_nickname(df)

guest_split_last('Dr. ', df)
guest_split_last('Dr ', df)

replace('Drew', 'Dr. Drew', df)
replace('Oz', 'Dr. Oz', df)


# df.to_csv('cleaned_podcasts.csv', sep='\t')


df0 = pd.read_csv('cleaned_podcasts.csv', sep='\t', index_col=0)

df_combine = pd.concat([df, df0], ignore_index=True)



df_combine.drop_duplicates(subset=['podcast', 'guests', 'duration', 'title'],inplace=True)
df_combine.reset_index(inplace=True, drop=True)

df_combine.to_csv('cleaned_podcasts.csv', sep='\t')

podcast_info.to_csv('meta_podcast_info.csv', sep='\t')

