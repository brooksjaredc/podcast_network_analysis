import pandas as pd
import numpy as np

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


def split_hosts():

	df = pd.read_csv('../reading_and_cleaning/cleaned_podcasts.csv', sep='\t', index_col=0)
	df = df.replace(r'', np.nan, regex=True)
	df = df[pd.notnull(df['guests'])]
	split_hosts = splitDataFrameList(df, 'hosts', ', ')
	
	for index, row in split_hosts.iterrows():
	    if(row['hosts'] == row['guests']):
	        split_hosts.drop(index=index, inplace=True)
	
	# guest_durations = split_hosts.groupby(['hosts', 'guests'])['duration'].sum()
	# guest_durations = guest_durations.reset_index()

	return split_hosts

# split_hosts = split_hosts()

# split_hosts.to_csv('split_hosts.csv', sep='\t')