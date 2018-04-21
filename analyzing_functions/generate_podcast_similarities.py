import pandas as pd


podcast_similarities = pd.DataFrame(columns=['podcast1', 'podcast2', 'score'])

for index1, row1 in podcast_info.iterrows():
    summ=0
    df1 = df[df['podcast'] == row1['Podcast Name']]
    guest_durations1 = df1.groupby(['guests'])['duration'].sum()
    guest_durations1 = guest_durations1.reset_index()
    for index2, row2 in podcast_info.iterrows():
        summ=0
        if(index1 >= index2):
            continue
        df2 = df[df['podcast'] == row2['Podcast Name']]
        guest_durations2 = df2.groupby(['guests'])['duration'].sum()
        guest_durations2 = guest_durations2.reset_index()
        for index3, row3 in guest_durations1.iterrows():
            for index4, row4 in guest_durations2.iterrows():
                if(row3['guests'] == row4['guests']):
                    summ += row3['duration']*row4['duration']
        print(row1['Podcast Name'], row2['Podcast Name'], summ)
        index3 = index1+index2
        podcast_similarities.loc[index3] = [row1['Podcast Name'], row2['Podcast Name'], summ]


podcast_similarities.to_csv('podcast_similarities.csv', sep='\t')
