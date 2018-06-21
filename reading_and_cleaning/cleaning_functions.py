import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import re
import datetime as dt
import time

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

def xml_to_df(filename):
	e = ET.parse(filename).getroot()
	ns = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}
	titles = []
	dates = []
	durations = []
	descriptions = []
	for item in e.iter('item'):
		for d in item.findall('itunes:duration', ns):
			if(d.text=='00.58.48'):
				dur = '00:58:48'
			else:
				dur = d.text.split('.')[0]
		durations.append(dur)
		titles.append(item.find('title').text)
		dates.append(item.find('pubDate').text)
		#descriptions.append(item.find('description').text)
		#print(durr)
			
	df = pd.DataFrame()
	df['title'] = titles
	df['date'] = dates

	df['duration'] = [sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(time.split(":")))) for time in durations]

	df.drop_duplicates(inplace=True)

	return df

def xml_to_df_desc(filename):
	e = ET.parse(filename).getroot()
	ns = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}
	titles = []
	dates = []
	durations = []
	descriptions = []
	for item in e.iter('item'):
		if(item.find('description')==None):
			continue
		titles.append(item.find('title').text)
		dates.append(item.find('pubDate').text)
		for d in item.findall('itunes:duration', ns):
			durations.append(d.text.split('.')[0])
		descriptions.append(item.find('description').text)
			
	df = pd.DataFrame()
	df['title'] = titles
	df['date'] = dates
	df['duration'] = [sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(time.split(":")))) for time in durations]
	df['description'] = descriptions
	df.drop_duplicates(inplace=True)
	return df

def xml_to_df_subt(filename):
	e = ET.parse(filename).getroot()
	ns = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}
	titles = []
	dates = []
	durations = []
	subtitles = []
	for item in e.iter('item'):
		titles.append(item.find('title').text)
		dates.append(item.find('pubDate').text)
		for d in item.findall('itunes:duration', ns):
			durations.append(d.text.split('.')[0])
		for d in item.findall('itunes:subtitle', ns):
			subtitles.append(d.text)
			
	df = pd.DataFrame()
	df['title'] = titles
	df['date'] = dates
	df['duration'] = [sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(time.split(":")))) for time in durations]
	df['subtitle'] = subtitles
	df.drop_duplicates(inplace=True)
	return df

def xml_to_df_summ(filename):
	e = ET.parse(filename).getroot()
	ns = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}
	titles = []
	dates = []
	durations = []
	summary = []
	for item in e.iter('item'):
		titles.append(item.find('title').text)
		dates.append(item.find('pubDate').text)
		for d in item.findall('itunes:duration', ns):
			durations.append(d.text.split('.')[0])
		for d in item.findall('itunes:summary', ns):
			summ = d.text
		summary.append(summ)
			
	df = pd.DataFrame()
	df['title'] = titles
	df['date'] = dates
	df['duration'] = [sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(time.split(":")))) for time in durations]
	df['summary'] = summary
	df.drop_duplicates(inplace=True)
	return df

def replace(whatis, whatshouldbe, df):
	for index, row in df.iterrows():
		if(pd.notnull(row['guests'])):
			if(whatis == row['guests']):
				df.at[index, 'guests'] = whatshouldbe
				
def guest_split(spl, df):
	for index, row in df.iterrows():
		if(pd.notnull(row['guests'])):
			if(spl in row['guests']):
				df.at[index, 'guests'] = row['guests'].split(spl)[0]

def guest_split_last(spl, df):
	for index, row in df.iterrows():
		if(pd.notnull(row['guests'])):
			if(spl in row['guests']):
				df.at[index, 'guests'] = row['guests'].split(spl)[-1]

def date_parser(df):
	excl = '(\s\+0000|\s\-0000|\sGMT|\sEST|\s\-0[78]00|\s\-0600|\s\-0[45]00|\sP[SD]T|\sE[DS]T|\s\+0100)$'
	dates_no_zeros =[]
	for d in df['date']:
		dates_no_zeros.append(re.sub(excl, '', str(d), flags=re.IGNORECASE))
	df['date'] = [dt.datetime.strptime(d, '%a, %d %b %Y %H:%M:%S') for d in dates_no_zeros]


def remove_nickname(df):
	nickname = re.compile('[\w\s]+\"[\w\s]+\"[\w\s]+')
	for index, row in df.iterrows():
		if(pd.notnull(row['guests'])):
			name1 = row['guests']
			if(nickname.search(name1)):
				name2 = re.sub(r'\".*\" ', "", row['guests']).strip()
				if(name1!=name2):
					print(name1, name2)
					df.at[index, 'guests'] = name2

