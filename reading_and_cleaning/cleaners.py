import numpy as np
import pandas as pd
import re
import datetime as dt
import time
from cleaning_functions import *


def clean_joe_rogan(joe_rogan):

    joe_rogan = xml_to_df(joe_rogan)

    ## Remove Fight shows
    
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('MMA Show') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Fight Companion') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Recap') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Breakdown') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Twitter') == False]
    
    ## Extract episode number and guests
    
    joe_rogan['episode'] = joe_rogan.title.str.extract(r'\#(\d+)',expand=True)
    joe_rogan['guests'] = joe_rogan.title.str.extract(r'\#\d+\s-\s([\w\s.,&\'\-\"]+)',expand=True)
    
    ## Clean guest list
    
    replace('Lewis, from Unbox Therapy', 'Lewis from Unbox Therapy', joe_rogan)
    replace('Lewis, form Unbox Therapy', 'Lewis from Unbox Therapy', joe_rogan)

    replace('Chris & Mark Bell', 'Chris Bell & Mark Bell', joe_rogan)
    replace('Alex & Allyson Grey', 'Alex Grey & Allyson Grey', joe_rogan)
    replace('Vince & Emily Horn', 'Vince Horn & Emily Horn', joe_rogan)
    
    joe_rogan = joe_rogan[pd.notnull(joe_rogan['guests'])]
    joe_rogan = splitDataFrameList(joe_rogan, 'guests', ', ')
    joe_rogan = joe_rogan[joe_rogan.guests.str.contains('Jr.') == False]
    joe_rogan = splitDataFrameList(joe_rogan, 'guests', ' & ')
    
    guests = [g.rstrip() for g in joe_rogan['guests']]
    joe_rogan['guests'] = guests
    
    guests = [g.lstrip() for g in joe_rogan['guests']]
    joe_rogan['guests'] = guests
    
    for index, row in joe_rogan.iterrows():
        if(pd.notnull(row['guests'])):
            joe_rogan.at[index, 'guests'] = row['guests'].title()
            
    replace('Chris Ryan', 'Christopher Ryan', joe_rogan)
    replace('Christina P', 'Christina Pazsitzky', joe_rogan)
    replace('Brian Redban - Date', 'Brian Redban', joe_rogan)
    replace('Brian Reichle', 'Brian Redban', joe_rogan)
    replace('Ces Review With Young Jamie', 'Young Jamie', joe_rogan)
    replace('Iliza Schlesinger', 'Iliza Shlesinger', joe_rogan)
    replace('Kill Tony Cast - Tony Hinchcliffe', 'Tony Hinchcliffe', joe_rogan)
    replace('W Kamau Bell', 'W. Kamau Bell', joe_rogan)
    replace('Honeyhoney', 'Honey Honey', joe_rogan)
    replace('Wheeler Walker', 'Wheeler Walker Jr', joe_rogan)
    replace('Joey "Coco" Diaz', 'Joey Diaz', joe_rogan)
    replace('London Real', 'Brian Rose', joe_rogan)
    replace('""Big"" Jay Oakerson"', 'Big Jay Oakerson', joe_rogan)
    replace('"Big" Jay Oakerson', 'Big Jay Oakerson', joe_rogan)
    replace('Legion Of Skanks', 'Big Jay Oakerson, Luis J. Gomez, Dave Smith', joe_rogan)
    replace('Wheeler Walker Jr', 'Wheeler Walker Jr.', joe_rogan)
    replace('Donald "Cowboy" Cerrone', 'Donald Cerrone', joe_rogan)
    replace('Neil Degrasse Tyson', 'Neil deGrasse Tyson', joe_rogan)
    

    guest_split_last('Cmdr. ', joe_rogan)

    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('From ')]
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('Live ')]
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('Ph.D')]
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('Phd')]

    date_parser(joe_rogan)

    joe_rogan = splitDataFrameList(joe_rogan, 'guests', ', ')
    joe_rogan = splitDataFrameList(joe_rogan, 'guests', ' & ')
    
    joe_rogan_output = joe_rogan

    return joe_rogan_output


def clean_duncan_trussel(duncan_trussel):
    
    duncan_trussel = xml_to_df(duncan_trussel)

    ## Set Episode numbers
    
    duncan_trussel['episode'] = len(duncan_trussel) - duncan_trussel.index

    date_parser(duncan_trussel)
    
    ### Manual cleaning, goddammit duncan
    
    for index, row in duncan_trussel.iterrows():
        if(pd.notnull(row['title'])):
            duncan_trussel.at[index, 'title'] = row['title'].title()
        
    duncan_trussel['guests'] = duncan_trussel['title']
        
    for index, row in duncan_trussel.iterrows():
        if('With ' in row['guests']):
            split = row['guests'].split('With ')[-1]
            duncan_trussel.at[index, 'guests'] = split

    
    guest_split(' In', duncan_trussel)
    guest_split(' Part', duncan_trussel)
    guest_split('!', duncan_trussel)
    guest_split(' Returns', duncan_trussel)
    guest_split(' Is', duncan_trussel)
    guest_split(' Are', duncan_trussel)
    guest_split(' (', duncan_trussel)
    guest_split('-', duncan_trussel)
    guest_split('...', duncan_trussel)
    guest_split(' Live', duncan_trussel)
    guest_split(' From', duncan_trussel)
            
    for index, row in duncan_trussel.iterrows():
        if(row['episode']==14):
            duncan_trussel.at[index, 'guests'] = 'Andy Kindler'
        if(row['episode']==27):
            duncan_trussel.at[index, 'guests'] = 'Joe Rogan'
        if(row['episode']==3):
            duncan_trussel.at[index, 'guests'] = 'Chris Hardwick, Natasha Leggero'
        if(row['episode']==5):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==4):
            duncan_trussel.at[index, 'guests'] = 'Tim Heidecker, Marilyn Heidecker'
        if(row['episode']==6):
            duncan_trussel.at[index, 'guests'] = 'Joe Randazzo, Natasha Leggero'
        if(row['episode']==7):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==8):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero, Jen Kirkman, Neil Cambell'
        if(row['episode']==9):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==10):
            duncan_trussel.at[index, 'guests'] = 'Derek Waters, Natasha Leggero'
        if(row['episode']==11):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==12):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==13):
            duncan_trussel.at[index, 'guests'] = 'Oscar Nunez, Natasha Leggero'
        if(row['episode']==15):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==16):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==17):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==18):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==21):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==22):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==23):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==24):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==25):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==26):
            duncan_trussel.at[index, 'guests'] = 'Emil Amos'
        if(row['episode']==28):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==29):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==30):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==33):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==34):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==35):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==36):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==37):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==38):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==39):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==41):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==43):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==44):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==45):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==46):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==47):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==48):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==49):
            duncan_trussel.at[index, 'guests'] = 'Emil Amos'
        if(row['episode']==51):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==52):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==53):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==54):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==55):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==56):
            duncan_trussel.at[index, 'guests'] = 'Greg Turkington, Simone Turkington'
        if(row['episode']==57):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==59):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==60):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==61):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==62):
            duncan_trussel.at[index, 'guests'] = 'Joe Mande'
        if(row['episode']==64):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==65):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==67):
            duncan_trussel.at[index, 'guests'] = 'Natasha Leggero'
        if(row['episode']==68):
            duncan_trussel.at[index, 'guests'] = 'Little Esther'
        if(row['episode']==74):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==75):
            duncan_trussel.at[index, 'guests'] = 'Derek Waters'
        if(row['episode']==88):
            duncan_trussel.at[index, 'guests'] = 'Bert Kreischer'
        if(row['episode']==94):
            duncan_trussel.at[index, 'guests'] = 'Chris Ryan'
        if(row['episode']==96):
            duncan_trussel.at[index, 'guests'] = 'Pete Holmes'
        if(row['episode']==108):
            duncan_trussel.at[index, 'guests'] = 'Chris Ryan'
        if(row['episode']==113):
            duncan_trussel.at[index, 'guests'] = 'Tim Heidecker'
        if(row['episode']==115):
            duncan_trussel.at[index, 'guests'] = 'Joey Greco'
        if(row['episode']==129):
            duncan_trussel.at[index, 'guests'] = 'Johnny Pemberton'
        if(row['episode']==133):
            duncan_trussel.at[index, 'guests'] = 'Daniele Bolelli'
        if(row['episode']==149):
            duncan_trussel.at[index, 'guests'] = 'Derek Waters'
        if(row['episode']==150):
            duncan_trussel.at[index, 'guests'] = 'Chris Ryan'
        if(row['episode']==152):
            duncan_trussel.at[index, 'guests'] = 'Keith Malley And Chemda Khalili'
        if(row['episode']==153):
            duncan_trussel.at[index, 'guests'] = 'Emil Amos'
        if(row['episode']==154):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==159):
            duncan_trussel.at[index, 'guests'] = 'Erin Mcgathy'
        if(row['episode']==169):
            duncan_trussel.at[index, 'guests'] = 'Sam Tripoli'
        if(row['episode']==175):
            duncan_trussel.at[index, 'guests'] = np.nan
        if(row['episode']==190):
            duncan_trussel.at[index, 'guests'] = 'Johnny Pemberton'
        if(row['episode']==205):
            duncan_trussel.at[index, 'guests'] = 'Johnny Pemberton'
        if(row['episode']==222):
            duncan_trussel.at[index, 'guests'] = 'Alex Grey, Allyson Grey, Emil Amos'
        if(row['episode']==246):
            duncan_trussel.at[index, 'guests'] = 'Raghu Markus'
        if(row['episode']==262):
            duncan_trussel.at[index, 'guests'] = 'Mikey Kampmann'
        if(row['episode']==263):
            duncan_trussel.at[index, 'guests'] = 'Alex Grey, Allyson Grey'
        if(row['episode']==268):
            duncan_trussel.at[index, 'guests'] = 'Tim Heidecker'
        if(row['episode']==289):
            duncan_trussel.at[index, 'guests'] = 'Jesse Moynihan'
        if(row['episode']==298):
            duncan_trussel.at[index, 'guests'] = 'Abby Martin'
        if(row['episode']==327):
            duncan_trussel.at[index, 'guests'] = 'Johnny Pembert And Brendon Walsh'
        if(row['episode']==330):
            duncan_trussel.at[index, 'guests'] = 'Derek Waters And Jody Waters'
        if(row['episode']==332):
            duncan_trussel.at[index, 'guests'] = 'Alex Grey, Allyson Grey'
        if(row['episode']==343):
            duncan_trussel.at[index, 'guests'] = 'Johnny Pemberton'
            
    ## Split Guests
    replace('Allyson and Alex Grey', 'Allyson Grey and Alex Grey', duncan_trussel)
    replace('Alex And Allyson Grey', 'Allyson Grey and Alex Grey', duncan_trussel)
    
    duncan_trussel = duncan_trussel[pd.notnull(duncan_trussel['guests'])]
    duncan_trussel = splitDataFrameList(duncan_trussel, 'guests', ', ')
    duncan_trussel = splitDataFrameList(duncan_trussel, 'guests', ' & ')
    duncan_trussel = splitDataFrameList(duncan_trussel, 'guests', ' And ')
    
    ## Fix Names

    
    duncan_trussel['guests'] = [g.lstrip() for g in duncan_trussel['guests']]
            
    replace('Chris Ryan', 'Christopher Ryan', duncan_trussel)
    replace('Daniel Bolelli', 'Daniele Bolelli', duncan_trussel)
    replace('Daniele Bolleli', 'Daniele Bolelli', duncan_trussel)
    replace('Danielle Bolleli', 'Daniele Bolelli', duncan_trussel)
    replace('Danielle Bolelli', 'Daniele Bolelli', duncan_trussel)
    replace('Paul F Tompkins', 'Paul F. Tompkins', duncan_trussel)
    replace('Allison Rosen', 'Alison Rosen', duncan_trussel)
    replace('Dr Drew', 'Dr. Drew', duncan_trussel)
    replace('Allyson and Alex Grey', 'Allyson Grey and Alex Grey', duncan_trussel)
    
    #sum(duncan_trussel['guests'].str.contains('Christopher Ryan')==True)
    
    duncan_trussel_output = duncan_trussel
    
    return duncan_trussel_output  #'hello'  #duncan_trussel_output[duncan_trussel['guests']=='Paul F Tompkins'] 


pd.options.mode.chained_assignment = None  # default='warn'



def clean_bert_kreischer(bert_kreischer):

    bert_kreischer = xml_to_df(bert_kreischer)
    
    bert_kreischer = bert_kreischer.loc[bert_kreischer.title.str.contains('Call In Sick To Work Show') == False]

    ## Set Episode numbers
    
    bert_kreischer['episode'] = bert_kreischer.title.str.extract(r'\#\s?([\d.]+)',expand=True)

    date_parser(bert_kreischer)
    
    ## Set guest list
    
    for index, row in bert_kreischer.iterrows():
        if(pd.notnull(row['title'])):
            bert_kreischer.at[index, 'title'] = row['title'].title()
    
    bert_kreischer['guests'] = bert_kreischer.title.str.extract(r'\#[\s-]?[\d\.-]+\s(?:[-\s]+)?(?:\([\w\s]+\))?([\w\s\.\,&/\'\-"]+)',expand=True)
    
    for index, row in bert_kreischer.iterrows():
        if(pd.isnull(row['guests'])):
            bert_kreischer.at[index, 'guests'] = row['title']
    
    guests_no_me =[]
    for g in bert_kreischer['guests']:
        #guests_no_me.append(re.sub('[\s&|,\sand] ME', '', str(g), flags=re.IGNORECASE))
        guests_no_me.append(re.sub('(, and ME|, & ME| & ME|...AND ME|ME, & )', '', str(g), flags=re.IGNORECASE))
        
    bert_kreischer['guests'] = guests_no_me
    
    for index, row in bert_kreischer.iterrows():
        if(row['title']=='Jon Heffron, Jon Moore, & Me'):
            bert_kreischer.at[index, 'episode'] = '4'
            bert_kreischer.at[index, 'guests'] = 'Jon Heffron, Jon Moore'
        if(row['episode']=='1'):  
            bert_kreischer.at[index, 'guests'] = 'Joey Diaz, Tom Segura, My Dad'

    bert_kreischer['guests'] = [g.rstrip() for g in bert_kreischer['guests']]
    bert_kreischer['guests'] = [g.rstrip(r'\.') for g in bert_kreischer['guests']]
    bert_kreischer['guests'] = [g.lstrip() for g in bert_kreischer['guests']]
            
    guest_split_last('W/ ', bert_kreischer)
    guest_split_last("'S ", bert_kreischer)
    guest_split_last("Guest ", bert_kreischer)
    guest_split_last("The Complete ", bert_kreischer)
    guest_split_last("Creator ", bert_kreischer)
    guest_split_last("By ", bert_kreischer)
            
    guest_split(' In', bert_kreischer)
    guest_split(' - ', bert_kreischer)
            
    replace('The Jeffs', 'Jeff Johnson & Jeff Hinman', bert_kreischer)
    replace('Redban', 'Brian Redban', bert_kreischer)
    replace('Push', 'Christina Pazsitzky', bert_kreischer)
    replace('The Chive', 'Mac Faulkner', bert_kreischer)
    replace('Sam', 'Sam Roberts', bert_kreischer)
    replace('Fitness Special W', 'Chris Tye Walker', bert_kreischer)
    replace('Sunday Special... A Chiropractor, His Hot Chic, John Bush', 'John Bush', bert_kreischer)
    replace('Mick Foley W', 'Mick Foley, Sam Roberts', bert_kreischer)
    replace('Kevin Heffernan, Steve LemMe', 'Kevin Heffernan, Steve Lemme', bert_kreischer)
    #replace('Just Me', np.nan, bert_kreischer)
    replace('Josh Wolf The Last 10 Minutes', 'Josh Wolf', bert_kreischer)
    
    guest_split(' From', bert_kreischer)
    
    replace('The Rolling Stone Magazine Article "The Undergraduate"', np.nan, bert_kreischer)
    replace('The End Of The Undergraduate', np.nan, bert_kreischer)
    replace('#146 – Book Club Crash – So You’ve Been Publicly Shamed, by Jon Ronson', 'Jon Ronson', bert_kreischer)
    #replace('Co', 'Jonathan Steinberg', bert_kreischer)
    replace('Joey "Coco" Diaz', 'Joey Diaz', bert_kreischer)
    replace('Doug Loves Bert', 'Doug Benson', bert_kreischer)
    replace('Annie Lederman& Me', 'Annie Lederman', bert_kreischer)
    replace('Live', 'Doug Stanhope', bert_kreischer)
    replace('Danish & O', 'Danish & O’Neill', bert_kreischer)
    replace('Ari Shaffir ', 'Ari Shaffir', bert_kreischer)
    replace("Todd & Tyler", 'Mike Tyler and Todd Brandt', bert_kreischer)

    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('Daddy ') == False]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('Best Of ') == False]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('Special') == False]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('My ') == False]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('On An ') == False]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('Adventurecast') == False]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains('Dreamcast') == False]
    
    ## Split Guests
    
    bert_kreischer = bert_kreischer[pd.notnull(bert_kreischer['guests'])]
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ', and ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ', And ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ', & ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ', ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ',')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ' & ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ' And ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ' and ')
    
    replace('Wheeler Walker Jr', 'Wheeler Walker Jr.', bert_kreischer)
    replace('Joey Coco Diaz', 'Joey Diaz', bert_kreischer)
    replace('Sam "Primetime" Roberts', 'Sam Roberts', bert_kreischer)
    replace('Me', np.nan, bert_kreischer)
    replace('Just Me', np.nan, bert_kreischer)
    replace('Redban', 'Brian Redban', bert_kreischer)
    replace('A Little Leeann', 'Leeann Kreischer', bert_kreischer)
    replace('Leeann', 'Leeann Kreischer', bert_kreischer)
    replace('Danish', 'Jeff Danis', bert_kreischer)
    replace('O’Neill', 'Ryan O’Neill', bert_kreischer)
    replace("O'Neill", 'Ryan O’Neill', bert_kreischer)
    replace("O'Neil", 'Ryan O’Neill', bert_kreischer)
    replace("Dr. Drew Pinsky", 'Dr. Drew', bert_kreischer)

    
    bert_kreischer = bert_kreischer[bert_kreischer['guests'].str.len() < 22]
    bert_kreischer = bert_kreischer[bert_kreischer.guests.str.contains(r'The ') == False]

    bert_kreischer.replace('', np.nan, inplace=True)
    bert_kreischer = bert_kreischer[pd.notnull(bert_kreischer['guests'])]
    
    return bert_kreischer


def clean_tfatk(tfatk):

    tfatk = xml_to_df(tfatk)

    ## Set Episode numbers
    
    tfatk['episode'] = tfatk.title.str.extract(r'\#\s?([\d.]+)',expand=True)

    date_parser(tfatk)
    
    ### Manual cleaning
    
    tfatk['guests'] = tfatk.title.str.extract(r'(?:(?:VIDEO HIGHLIGHTS: )?(?:TFATK )?Episode \d+)?(?:\s-\s)?(?::\s)?([\w\s\.\,&/\'\-"]+)?',expand=True)
        
    guest_split(' joins', tfatk)
        
    for index, row in tfatk.iterrows():
        if(pd.notnull(row['guests'])):
            if('Brendan' in row['guests']):
                tfatk.at[index, 'guests'] = np.nan 
                
    replace('Navy SEAL Andy Stumpf', 'Andy Stumpf', tfatk)
    replace("Big Brown's UFC farewell", np.nan, tfatk)
    replace('100th Episode Extravaganza', np.nan, tfatk)
    replace('Range 15', np.nan, tfatk)
    replace("Donald 'Cowboy' Cerrone", 'Donald Cerrone', tfatk)
    replace('Epiosde 201', 'Chael Sonnen', tfatk)
    replace('Randy & Jason Sklar ', 'Randy Sklar & Jason Sklar', tfatk)
    replace("It's 2018", np.nan, tfatk)
    
    tfatk = tfatk[pd.notnull(tfatk['guests'])]
    tfatk = splitDataFrameList(tfatk, 'guests', ', ')
    tfatk = splitDataFrameList(tfatk, 'guests', ' & ')
    tfatk = splitDataFrameList(tfatk, 'guests', ' And ')
    tfatk = splitDataFrameList(tfatk, 'guests', ' and ')
    
    tfatk = tfatk[~tfatk['guests'].str.startswith('FATK')]
    tfatk = tfatk[~tfatk['guests'].str.startswith('Big Brown Breakdown')]
    tfatk = tfatk[~tfatk['guests'].str.startswith('GOTY winner announced')]
    tfatk = tfatk[~tfatk['guests'].str.startswith('BEST OF')]
    tfatk = tfatk[~tfatk['guests'].str.endswith('Special')]

    tfatk_output = tfatk
    
    return tfatk_output


def clean_ari_shaffir(ari_shaffir):

    ari_shaffir = xml_to_df(ari_shaffir)

    ## Set Episode numbers
    
    ari_shaffir['episode'] = ari_shaffir.title.str.extract(r'\#:?([\d.\w]+)',expand=True)
    
    date_parser(ari_shaffir)
    
    ari_shaffir['guests'] = ari_shaffir.title.str.extract(r'\#(?:[\d.\w]+):?\s(?:[\w\s,\.\;\:\'\"\&-\/\#]+)\(([^)]+)',expand=True)

    guest_split_last('with ', ari_shaffir)
            
    ### Manual cleaning
    
    replace('a crapload of comics', 'Rich Vos, Big Jay Oakerson, Chris Distefano, Sam Morril, Tracy Morgan, Des Bishop, Joe Machi, Bonnie McFarlane, Cipha Sounds, Yannis Pappas, and Jared Freid', ari_shaffir)
    replace('the gayer part', np.nan, ari_shaffir)
    
    
    ari_shaffir = ari_shaffir[pd.notnull(ari_shaffir['guests'])]
    ari_shaffir = splitDataFrameList(ari_shaffir, 'guests', ', ')
    ari_shaffir = splitDataFrameList(ari_shaffir, 'guests', ' & ')
    ari_shaffir = splitDataFrameList(ari_shaffir, 'guests', ' And ')
    ari_shaffir = splitDataFrameList(ari_shaffir, 'guests', ' and ')

    replace('Ms Pat', 'Ms. Pat', ari_shaffir)
    
    twitter_guests = []
    for d in ari_shaffir['guests']:
        if(d.startswith('@')):
            #twitter_guests.append(re.sub(r'(\@)',r"",d,re.MULTILINE).strip().replace("  "," "))
            twitter_guests.append(re.sub(r'(?:\@)([A-Z])',r" \1",d,re.MULTILINE).strip().replace("  "," "))
        else:
            twitter_guests.append(d)

    twitter_guests2 = []
    for d in twitter_guests:
        twitter_guests2.append(re.sub(r'(\_)',r" ",d,re.MULTILINE).strip().replace("  "," "))
            
    twitter_guests3 = []
    for d in twitter_guests2:
        twitter_guests3.append(re.sub(r'([A-Z])',r" \1",d,re.MULTILINE).strip().replace("  "," "))
        
    twitter_guests4 = []
    for d in twitter_guests3:
        twitter_guests4.append(re.sub(r'([\d\&\@]|and\s|Comic|Comedy)',r"",d,re.MULTILINE).strip().replace("  "," "))

    ari_shaffir['guests'] = twitter_guests4
    
    for index, row in ari_shaffir.iterrows():
        if('The ' in row['guests']):
            split = row['guests'].split('The ')[-1]
            ari_shaffir.at[index, 'guests'] = split
            
    guest_split(' Live', ari_shaffir)
    
    ## Individual name fixes
    
    replace('Chris Ryan Ph D', 'Christopher Ryan', ari_shaffir)
    replace('Mike Ward @ Mike Ward C A', 'Mike Ward', ari_shaffir)
    replace('@ Tom Rhodes', 'Tom Rhodes', ari_shaffir)
    replace('Cort Mc Cown', 'Cort McCown', ari_shaffir)
    replace('@1 Glitter Goddess', 'Glitter Goddess', ari_shaffir)
    replace('Mr Sean Patton', 'Sean Patton', ari_shaffir)
    replace('Comic Dave Smith', 'Dave Smith', ari_shaffir)
    replace('J Fod Comedy', "John F O'Donnell", ari_shaffir)
    replace('Paul Morrissey My Next Door Neighbor Ari Shaffir', 'Paul Morrissey', ari_shaffir)
    replace('Kathleen Mc Gee', 'Kathleen McGee', ari_shaffir)
    replace('Danish And Oneill', 'Danish & O’Neill', ari_shaffir)
    replace('Joe Derosa Comedy', 'Joe Derosa', ari_shaffir)
    replace('Funny Brad', 'Brad Williams', ari_shaffir)
    replace('Brick Stone News', 'Dave Sirus', ari_shaffir)
    replace('Attell', 'Dave Attell', ari_shaffir)
    replace('Jeff Scott101', 'Jeff Scott', ari_shaffir)
    replace('Jason23 Nash', 'Jason Nash', ari_shaffir)
    replace('Brody Is Me Friend', 'Brody Stevens', ari_shaffir)
    replace('Sheng Wang Time', 'Sheng Wang', ari_shaffir)
    replace('Comedienne Ms Pat', 'Ms Pat', ari_shaffir)
    replace('This David Taylor', 'David Taylor', ari_shaffir)
    replace('Escariot', 'Pete Johannson', ari_shaffir)
    replace('Teeb', 'Jayson Thibault', ari_shaffir)
    replace('Godfrey Comedian', 'Godfrey', ari_shaffir)
    replace('Ali Speaks', 'Ali Siddiq', ari_shaffir)
    #replace('The Mike Lawrence', 'Mike Lawrence', ari_shaffir)
    #replace('Ian Edwards Comic', 'Ian Edwards', ari_shaffir)
    replace('Moosefu*ker', 'Craig Campbell', ari_shaffir)
    replace('Moose Fucker', 'Craig Campbell', ari_shaffir)
    replace('Hebert', 'Sean Hebert', ari_shaffir)
    replace('J M Scomedy', 'Jessica Michelle Singleton', ari_shaffir)
    replace('Mike Black Attack', 'Mike Black', ari_shaffir)
    replace('Shane', 'Shane Mauss', ari_shaffir)
    replace('Luisa Diez Nuts', 'Luisa Diez', ari_shaffir)
    replace('Not Hormones', 'Hormoz Rashidi', ari_shaffir)
    replace('Not Alexis', 'Alexis Guerreros', ari_shaffir)
    replace('Fire', 'Rob Bernstein', ari_shaffir)
    replace('Real Jeffrey Ross', 'Jeffrey Ross', ari_shaffir)
    replace('Stollemcache', 'Sarah Tollemache', ari_shaffir)
    replace('Milo', 'Milo McCabe', ari_shaffir)
    replace('Aiapalucci', 'Adrian Iapalucci', ari_shaffir)
    replace('Milo', 'Milo McCabe', ari_shaffir)
    replace('AmberSmelson', 'Amber Nelson', ari_shaffir)
    replace('Seanytime', 'Sean Donnelly', ari_shaffir)
    replace('Mark Norm', 'Mark Normand', ari_shaffir)
    replace('Stav', 'Stavros Halkios', ari_shaffir)
    replace('Hey Its Chili', 'William Childress', ari_shaffir)
    replace('Funny Lynne', 'Lynne Koplitz', ari_shaffir)
    replace('Colin Is My Name', 'Colin Wright', ari_shaffir)
    replace('Monroe Martin I I I', 'Monroe Martin', ari_shaffir)
    replace('Tim Crockett Row Atlantic', 'Tim Crockett', ari_shaffir)
    replace('Christina P', 'Christina Pazsitzky', ari_shaffir)
    replace('Ryan " Danish And Oneill" Oneill', 'Danish & O’Neill', ari_shaffir)
    replace('Bonnie Mc Farlane', 'Bonnie McFarlane', ari_shaffir)
    replace('Mad Flavor', 'Joey Diaz', ari_shaffir)
    replace('Big Jay Oakerson Ari Shaffir', 'Big Jay Oakerson', ari_shaffir)
    replace('Steven Brody Stevens', 'Brody Stevens', ari_shaffir)
    
    ari_shaffir = ari_shaffir[ari_shaffir.guests.str.contains('Ruby') == False]
    
    return ari_shaffir


def clean_russell_brand(russell_brand):

    russell_brand = xml_to_df(russell_brand)

    russell_brand.replace(u"\u00A0", " ", regex=True, inplace=True)

    ## Set Episode numbers
    
    russell_brand['episode'] = russell_brand.title.str.extract(r'\#([\d]+)',expand=True)

    date_parser(russell_brand)
    
    russell_brand['guests'] = russell_brand.title.str.extract(r'\#(?:[\d]+)\s(?:[^(]+)\(?[Ww]ith ([^)]+)',expand=True)

    ### Manual cleaning
    
    for index, row in russell_brand.iterrows():
        if(row['episode']=='001'):
            russell_brand.at[index, 'guests'] = 'Dr Brad Evans'
        if(row['episode']=='002'):
            russell_brand.at[index, 'guests'] = 'Paul Gilroy'
        if(row['episode']=='003'):
            russell_brand.at[index, 'guests'] = 'Adam Curtis'
        if(row['episode']=='004'):
            russell_brand.at[index, 'guests'] = 'Anne Phillips'
        if(row['episode']=='005'):
            russell_brand.at[index, 'guests'] = 'Yuval Noah Harari'
        if(row['episode']=='008'):
            russell_brand.at[index, 'guests'] = 'Dr. Brad Evans'
        if(row['episode']=='012'):
            russell_brand.at[index, 'guests'] = 'Dr. Brad Evans, Rabbi Dr. Jonathan Romain'
        if(row['episode']=='014'):
            russell_brand.at[index, 'guests'] = 'Lindsey German and Dr. Brad Evans'
        if(row['episode']=='015'):
            russell_brand.at[index, 'guests'] = 'Yanis Varoufakis'
        if(row['episode']=='018'):
            russell_brand.at[index, 'guests'] = 'Naomi Klein'
        if(row['episode']=='019'):
            russell_brand.at[index, 'guests'] = 'Frankie Boyle'
        if(row['episode']=='022'):
            russell_brand.at[index, 'guests'] = 'Dr. Robin Carhart-Harris'
        if(row['episode']=='023'):
            russell_brand.at[index, 'guests'] = 'Al Gore'
        if(row['episode']=='027'):
            russell_brand.at[index, 'guests'] = 'Isabel Losada'
        if(row['episode']=='035'):
            russell_brand.at[index, 'guests'] = 'Ruby Wax'
        if(row['episode']=='043'):
            russell_brand.at[index, 'guests'] = 'Brian Cox'
        if(row['episode']=='048'):
            russell_brand.at[index, 'guests'] = 'Yuval Noah Harari'
        if(row['episode']=='049'):
            russell_brand.at[index, 'guests'] = 'Yanis Varoufakis'


    replace('Supervet Noel Fitzpatrick', 'Noel Fitzpatrick', russell_brand)
    replace('Ed Stafford - Is The Toughest Terrain Your Own Mind?', 'Ed Stafford', russell_brand)
    replace('Dr Brad Evans', 'Dr. Brad Evans', russell_brand)
    replace('Prof Barry Smith', 'Barry Smith', russell_brand)
    replace('Ryron & Rener Gracie', 'Ryron  Gracie & Rener Gracie', russell_brand)

    russell_brand = russell_brand[pd.notnull(russell_brand['guests'])]
    russell_brand = splitDataFrameList(russell_brand, 'guests', ', ')
    russell_brand = splitDataFrameList(russell_brand, 'guests', ' & ')
    russell_brand = splitDataFrameList(russell_brand, 'guests', ' And ')
    russell_brand = splitDataFrameList(russell_brand, 'guests', ' and ')

    guest_split_last('Prof', russell_brand)
    guest_split_last('Professor', russell_brand)
    
    return russell_brand

def clean_kevin_pereira(kevin_pereira):

    kevin_pereira = xml_to_df(kevin_pereira)

    ## Set Episode numbers
    
    kevin_pereira['episode'] = 185 - kevin_pereira.index

    date_parser(kevin_pereira)
    
    kevin_pereira['guests'] = kevin_pereira.title.str.extract(r'([\w\s\.\""]+)\s\/',expand=True)
    
    guest_split(' pt.', kevin_pereira)
    guest_split(' Returns', kevin_pereira)
    
    ### Manual cleaning
    
    for index, row in kevin_pereira.iterrows():
        if(row['episode']==104):
            kevin_pereira.at[index, 'guests'] = 'Alessandra Torresani'
        if(row['episode']==121):
            kevin_pereira.at[index, 'guests'] = 'Justin Roiland & Ryan Ridley'
        if(row['episode']==143):
            kevin_pereira.at[index, 'guests'] = np.nan
        if(row['episode']==166):
            kevin_pereira.at[index, 'guests'] = 'Casey Crescenzo'
        if(row['episode']==168):
            kevin_pereira.at[index, 'guests'] = 'Casey Crescenzo'
        if(row['episode']==176):
            kevin_pereira.at[index, 'guests'] = 'Andrey Yanyuk'
        if(row['episode']==154):
            kevin_pereira.at[index, 'guests'] = 'Alex Corea, Corrado Caretto, Jeremy Hache'
        if(row['episode']==170):
            kevin_pereira.at[index, 'guests'] = 'Alex Corea, Carlos Rivera, Jacob Strouckel, Joey Thimian'

    kevin_pereira = kevin_pereira[kevin_pereira.guests.str.contains("Virtual ") == False]
    kevin_pereira = kevin_pereira[kevin_pereira.guests.str.contains("Pointless ") == False]


            
    kevin_pereira = kevin_pereira[pd.notnull(kevin_pereira['guests'])]
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ', ')
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ' & ')
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ' And ')
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ' and ')
    
    return kevin_pereira


def clean_chris_hardwick(chris_hardwick):

    chris_hardwick = xml_to_df(chris_hardwick)

    date_parser(chris_hardwick)
    
    chris_hardwick['guests'] = chris_hardwick['title']
    
    guest_split(' #', chris_hardwick)
    guest_split(' Returns', chris_hardwick)
    guest_split(' returns', chris_hardwick)
    guest_split(' LIVE', chris_hardwick)
    guest_split(' Live', chris_hardwick)
    guest_split('Live', chris_hardwick)
    guest_split(' of', chris_hardwick)
    guest_split(': ', chris_hardwick)
    guest_split(' (', chris_hardwick)

    guest_split_last('w/ ', chris_hardwick)
    guest_split_last('with ', chris_hardwick)
    guest_split_last('Episode! ', chris_hardwick)
    
    ### Manual cleaning
    
    replace('Billy West.mp3', 'Billy West', chris_hardwick)
    replace("Greta's Calling!", 'Greta', chris_hardwick)
    replace('Orange Is The New Black (TWCH)', 'Taylor Schilling, Uzo Aduba, Danielle Brooks, and Taryn Manning', chris_hardwick)

    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains(' from ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains(' Should ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains(' de ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('HOSTFUL!') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Hostful') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('2016') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Two ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('The ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains(' Party') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Airplane!') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Cluster') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Honestly') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Show!') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Wedding') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Work ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('THING') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Happiness Period') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Methio') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Talking') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('V Cards') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Apple Tarts') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Husky Puppies') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Happy ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Donkey Sauce') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Microwave') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Mattstronaut!') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Puns ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Who ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Typical ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Button ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Burger ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Bulging ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Lunch ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Bionic ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Donut ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('FRACTURE ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Instagramming ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains(' for ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Short Pants') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Bugle') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Bloody') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Sound ') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Overruled') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('yeahYUH') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Traffic') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Cave Bear') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Sketchfest') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Number') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Dance') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Vajonah') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Snapsy') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Hairy Otter') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Italian') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Gangnam') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Gersberms') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Fire Pit') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Silly') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Texas Cake') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Minstrel') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Sorry') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('Catholic Crusader') == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("God's") == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("Super ") == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("Futurama") == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("Large Puppy") == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("Lemme ") == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("Travel ") == False]
    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains("Neeemooo!!!") == False]



    replace('Rove McManus/Axis', 'Rove McManus and Axis of Awesome', chris_hardwick)
    replace('John K.', 'John Kricfalusi', chris_hardwick)
    replace('YouTube Titans!', 'Grace Helbig, Harley Morenstein and Hannah Hart', chris_hardwick)
    replace('Silicon Valley', 'Thomas Middleditch, Martin Starr and Zach Woods', chris_hardwick)
    replace('Diani & Devine', 'Gabe Diani & Etta Devine', chris_hardwick)
    replace('930 Club:', 'John Patrick Lowrie, Ellen McLain', chris_hardwick)
    replace('Undateable', 'Brent Morin, Ron Funches, Rick Glassman and David Fynn', chris_hardwick)
    replace('Zero Charisma', 'Katie Graham, Andrew Mathews and Sam Eidson', chris_hardwick)
    replace("WIRED's Chris Anderson", 'Chris Anderson', chris_hardwick)
    replace('Workaholics', 'Adam Devine, Anders Holm, Blake Anderson and Kyle Newacheck', chris_hardwick)
    replace('Señor Dick', 'Kristen Rutherford', chris_hardwick)
    replace('Elvira, Mistress', 'Cassandra Peterson', chris_hardwick)
    replace('Wilco', 'Wil Wheaton, Jeff Tweedy', chris_hardwick)
    replace('Hola Mindy!', 'Mindy Holahan', chris_hardwick)
    replace('Ambassador Class', 'John Barrowman', chris_hardwick)
    replace('Superego', 'Matt Gourley, Jeremy Carter, Mark McConville and Paul F. Tompkins', chris_hardwick)
    replace('Greta', '', chris_hardwick)
    replace('She & Him', 'Zooey Deschanel and M. Ward', chris_hardwick)
    replace('Eliza Dushku/Tahmoh Penikett', 'Eliza Dushku and Tahmoh Penikett', chris_hardwick)
    replace('Big Bang Theory', 'Johnny Galecki, Jim Parsons, Kaley Cuoco, Kunal Nayyar, Simon Helberg, Mayim Bialik, Melissa Rauch, Chuck Lorre, Bill Prady and Steve Molaro', chris_hardwick)
    replace('Tim and Eric', 'Tim Heidecker and Eric Wareheim', chris_hardwick)
    replace('MYTHBUSTERS', 'Adam Savage, Jamie Hyneman, Grant Imahara, Kari Byron and Tory Belleci', chris_hardwick)
    replace('Man', 'Zack Snyder, Charles Roven, Debbie Snyder, Henry Cavill, Diane Lane, Russell Crowe, Amy Adams, Michael Shannon, Antje Traue, writer David Goyer and Hans Zimmer', chris_hardwick)
    replace('OZZY', 'Ozzy Osbourne', chris_hardwick)
    replace('THE MUPPETS', 'The Muppets', chris_hardwick)
    replace('Whotopia!', 'Steven Moffat, Matt Smith, Karen Gillan, Arthur Darvill, Alex Kingston, Toby Haynes, Piers Wenger, Beth Willis', chris_hardwick)

    chris_hardwick = chris_hardwick.replace(r'', np.nan, regex=True)
    
    chris_hardwick = chris_hardwick[pd.notnull(chris_hardwick['guests'])]
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ', ')
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ' & ')
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ' And ')
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ' and ')

    chris_hardwick = chris_hardwick[chris_hardwick.guests.str.contains('the Tantrums') == False]
    replace("Fitz", 'Fitz and the Tantrums', chris_hardwick)


    replace("Key", 'Keegan-Michael Key', chris_hardwick)
    replace('TJ Miller', 'T.J. Miller', chris_hardwick)
    replace('Tegan', 'Tegan Rain Quin', chris_hardwick)
    replace('Sara', 'Sara Keirsten Quin', chris_hardwick)
    replace('Kevin Smith 2', 'Kevin Smith', chris_hardwick)
    replace('Penn', 'Penn Jillette', chris_hardwick)
    replace('Teller', 'Raymond Teller', chris_hardwick)
    replace('Mike Birbiglia 3peat', 'Mike Birbiglia', chris_hardwick)
    replace('Peele', 'Jordan Peele', chris_hardwick)

    
    return chris_hardwick


def clean_sam_harris(sam_harris):

    sam_harris = xml_to_df_subt(sam_harris)

    date_parser(sam_harris)
    
    sam_harris['episode'] = sam_harris.title.str.extract(r'\#\s?([\d]+)',expand=True)

    sam_harris['guests'] = sam_harris.subtitle.str.extract('A Conversation with ([\w\s\.]+)',expand=True)
    
    sam_harris = sam_harris.drop('subtitle', 1)
    
    sam_harris = sam_harris[pd.notnull(sam_harris['guests'])]
    sam_harris = splitDataFrameList(sam_harris, 'guests', ', ')
    sam_harris = splitDataFrameList(sam_harris, 'guests', ' & ')
    sam_harris = splitDataFrameList(sam_harris, 'guests', ' And ')
    sam_harris = splitDataFrameList(sam_harris, 'guests', ' and ')
    
    return sam_harris


def clean_kill_tony(kill_tony):

    kill_tony = xml_to_df_subt(kill_tony)
    
    kill_tony = kill_tony[kill_tony.title.str.contains('KILL TONY') == True]

    ## Set Episode numbers
    
    kill_tony['episode'] = kill_tony.title.str.extract(r'KILL TONY \#([\d]+)',expand=True)

    date_parser(kill_tony)
    
    kill_tony['guests'] = kill_tony['subtitle']
    
    kill_tony = kill_tony.drop('subtitle', 1)

    replace('Sklar Brothers', 'Jason Sklar and Randy Sklar', kill_tony)
    
    kill_tony = kill_tony[pd.notnull(kill_tony['guests'])]
    kill_tony = splitDataFrameList(kill_tony, 'guests', ', ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', ' & ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', ' And ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', ' and ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', '. ')
    
    guest_split(' -', kill_tony)
    guest_split(r' –', kill_tony)
    replace('SteveO', 'Steve-O', kill_tony)
    replace('Luis J Gomez', 'Luis J. Gomez', kill_tony)
    replace('Luis j Gomez', 'Luis J. Gomez', kill_tony)
    replace('Wheel Walker Jr', 'Wheeler Walker Jr.', kill_tony)
    replace('Jason Acuña (Wee Man)', 'Jason Acuña', kill_tony)
    
    return kill_tony


def clean_dave_rubin(dave_rubin):

    dave_rubin = xml_to_df_summ(dave_rubin)

    ## Set Episode numbers
    
    dave_rubin['episode'] = 202 - dave_rubin.index

    date_parser(dave_rubin)
    
    dave_rubin['guests'] = dave_rubin['summary']
    
    dave_rubin = dave_rubin.drop('summary', 1)
    
    guest_split(' (', dave_rubin)
    guest_split(' join', dave_rubin)
    guest_split(' is', dave_rubin)
    
    
    for index, row in dave_rubin.iterrows():
        if(row['episode']==1):
            dave_rubin.at[index, 'guests'] = 'Sam Harris'
        if(row['episode']==2):
            dave_rubin.at[index, 'guests'] = 'Cara Santa Maria'
        if(row['episode']==3):
            dave_rubin.at[index, 'guests'] = 'Felicia Michaels and Jimmy Dore'
        if(row['episode']==4):
            dave_rubin.at[index, 'guests'] = 'Maajid Nawaz'
        if(row['episode']==5):
            dave_rubin.at[index, 'guests'] = 'Milo Yiannopoulos'
        if(row['episode']==6):
            dave_rubin.at[index, 'guests'] = 'Michael Steele'
        if(row['episode']==7):
            dave_rubin.at[index, 'guests'] = 'Kelly Carlin'
        if(row['episode']==8):
            dave_rubin.at[index, 'guests'] = 'Ayaan Hirsi Ali'
        if(row['episode']==9):
            dave_rubin.at[index, 'guests'] = 'Douglas Murray'
        if(row['episode']==10):
            dave_rubin.at[index, 'guests'] = 'Faisal Saeed Al-Mutar'
        if(row['episode']==12):
            dave_rubin.at[index, 'guests'] = 'Christina Hoff Sommers'
        if(row['episode']==13):
            dave_rubin.at[index, 'guests'] = 'Nick Cohen'
        if(row['episode']==17):
            dave_rubin.at[index, 'guests'] = 'David Pakman'
        if(row['episode']==20):
            dave_rubin.at[index, 'guests'] = 'Bryan Wright'
        if(row['episode']==31):
            dave_rubin.at[index, 'guests'] = 'Tarek Fatah'
        if(row['episode']==32):
            dave_rubin.at[index, 'guests'] = 'Melissa Chen and Faisal Saeed Al Mutar'
        if(row['episode']==83):
            dave_rubin.at[index, 'guests'] = 'Larry King'
        if(row['episode']==143):
            dave_rubin.at[index, 'guests'] = 'Jack Conte'
        if(row['episode']==156):
            dave_rubin.at[index, 'guests'] = 'Richard Lewis'
        if(row['episode']==163):
            dave_rubin.at[index, 'guests'] = 'Jordan Peterson, Dave Rubin, Onkar Ghate'
        if(row['episode']==191):
            dave_rubin.at[index, 'guests'] = 'Rob McDonald'
        if(row['episode']==192):
            dave_rubin.at[index, 'guests'] = 'Kevin Gutzman'
        if(row['episode']==193):
            dave_rubin.at[index, 'guests'] = 'Bradley Thompson'
        if(row['episode']==194):
            dave_rubin.at[index, 'guests'] = 'Brian Domitrovic'
        if(row['episode']==195):
            dave_rubin.at[index, 'guests'] = 'Jeffrey Rogers Hummel'
            
    dave_rubin = dave_rubin[~dave_rubin['guests'].str.startswith('20 fans')]
    dave_rubin = dave_rubin[~dave_rubin['guests'].str.startswith('Hey ')]
    dave_rubin = dave_rubin[~dave_rubin['guests'].str.startswith('Dave went')]
    dave_rubin = dave_rubin[~dave_rubin['guests'].str.startswith('Did you')]
    dave_rubin = dave_rubin[~dave_rubin['guests'].str.startswith('In an era')]
    dave_rubin = dave_rubin[~dave_rubin['guests'].str.startswith('Watch live')]
            
    guest_split_last('Gov. ', dave_rubin)
    guest_split_last('Governor ', dave_rubin)

    replace('Two years ago, Lubna Ahmed', 'Lubna Ahmed', dave_rubin)
    replace('Brothers Bret Weinstein', 'Bret Weinstein and Eric Weinstein', dave_rubin)
    
    dave_rubin = dave_rubin[pd.notnull(dave_rubin['guests'])]
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ', and ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ', ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ' & ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ' And ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ' and ')
    
    replace('Jordan B Peterson', 'Jordan Peterson', dave_rubin)
    replace('Red Pill Black', 'Candace Owens', dave_rubin)
    
    
    return dave_rubin


def clean_comedy_bang(comedy_bang):

    comedy_bang = xml_to_df(comedy_bang)
    
    comedy_bang = comedy_bang[comedy_bang.title.str.contains('Best of') == False]
    comedy_bang = comedy_bang[comedy_bang.title.str.contains('Xmas') == False]

    ## Set Episode numbers
    
    comedy_bang['episode'] = comedy_bang.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser(comedy_bang)
    
    comedy_bang['guests'] = comedy_bang.title.str.extract(r'(?:[\d]+)\s([\w\s\.\,&/\’\'\-"]+)',expand=True)

    comedy_bang = comedy_bang[comedy_bang.guests.str.contains('Live ') == False]

    replace('Threedom', 'Paul F. Tompkins and Lauren Lapkus', comedy_bang)
    
    comedy_bang = comedy_bang[pd.notnull(comedy_bang['guests'])]
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ', ')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ',')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ' & ')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ' And ')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ' and ')
    
    return comedy_bang

def clean_h3(h3):

    h3 = xml_to_df(h3)

    ## Set Episode numbers
    
    h3['episode'] = h3.title.str.extract(r'\#([\d]+)',expand=True)

    date_parser(h3)
    
    h3['guests'] = h3.title.str.extract(r'\#[\d]+ (?:- )?([\w\s\.\'\&-]+)',expand=True)
    
    
    h3 = h3[h3.guests.str.contains('Top of the Month') == False]
    h3 = h3[h3.title.str.contains(r'\(Top of the Week\)') == False]
    
    h3 = h3[h3.guests.str.contains('Logan Paul') == False]
    h3 = h3[h3.guests.str.contains('Jake Paul') == False]
    h3 = h3[h3.guests.str.contains('parents') == False]
    
    guest_split(' Live', h3)
    guest_split(' of', h3)
    guest_split(' Charity', h3)
    guest_split_last('With ', h3)
    
    replace('PewDiePie', 'Felix Kjellberg', h3)
    replace('Vsauce', 'Michael Stevens', h3)
    replace('Vsauce ', 'Michael Stevens', h3)
    replace('Vsauce3 ', 'Jake Roper', h3)
    replace('How To Save a Life', 'Chris Betancourt, Dillon Hill', h3)
    
    for index, row in h3.iterrows():
        if(row['episode']=='15'):
            h3.at[index, 'guests'] = np.nan
        if(row['episode']=='21'):
            h3.at[index, 'guests'] = np.nan
        if(row['episode']=='20'):
            h3.at[index, 'guests'] = 'Jimmie Lee'

    replace('Erik', 'Erik Hoffstad', h3)
    replace('Internet Comment Etiquette', 'Erik Hoffstad', h3)
    replace('Jacksfilms', 'Jack Douglass', h3)
    replace('Boogie2988', 'Steven Jay Williams', h3)
    replace('Moe & Ethan Bradberry', 'Moe Bradberry & Ethan Bradberry', h3)
    replace('MKBHD', 'Marques Brownlee', h3)
    replace('PewDiePie', 'Felix Kjellberg', h3)


    
    h3 = h3[pd.notnull(h3['guests'])]
    h3 = splitDataFrameList(h3, 'guests', ', ')
    h3 = splitDataFrameList(h3, 'guests', ' & ')
    h3 = splitDataFrameList(h3, 'guests', ' And ')
    h3 = splitDataFrameList(h3, 'guests', ' and ')

    h3['guests'] = [g.rstrip() for g in h3['guests']]

    replace('Rhett', 'Rhett James McLaughlin', h3)
    replace('Link', 'Charles Lincoln Neal', h3)
    replace('PUBG Creator Brendan Greene', 'Brendan Greene', h3)

    h3 = h3[h3.guests.str.contains('We Raised') == False]
    h3 = h3[h3.guests.str.contains('We Won') == False]
    h3 = h3[h3.guests.str.contains('The Madness') == False]
    h3 = h3[h3.guests.str.contains('PewDiePie Drops the') == False]
    h3 = h3[h3.guests.str.contains('Net Neutrality') == False]
    
    return h3


def clean_marc_maron(marc_maron):

    marc_maron = xml_to_df(marc_maron)

    ## Set Episode numbers
    
    marc_maron['episode'] = marc_maron.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser(marc_maron)
    
    marc_maron['guests'] = marc_maron.title.str.extract(r'(?:[\d]+)\s-\s([\w\s\.\,&/\’\'\-"]+)',expand=True)
    
    replace('The President Was Here', np.nan, marc_maron)
    
    marc_maron = marc_maron[pd.notnull(marc_maron['guests'])]
    marc_maron = splitDataFrameList(marc_maron, 'guests', ' / ')
    marc_maron = splitDataFrameList(marc_maron, 'guests', ' & ')

    marc_maron = marc_maron[marc_maron.guests.str.contains(' the ') == False]
    marc_maron = marc_maron[marc_maron.guests.str.contains("Marc's Family") == False]
    marc_maron = marc_maron[marc_maron.guests.str.contains('Christmas') == False]

    replace('Dr. Steve', 'Dr. Stephen Dansiger', marc_maron)

    return marc_maron


def clean_joey_diaz(joey_diaz):

    joey_diaz = xml_to_df(joey_diaz)

    ## Set Episode numbers
    
    joey_diaz['episode'] = joey_diaz.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser(joey_diaz)
    
    joey_diaz['guests'] = joey_diaz.title.str.extract(r'(?:[\d]+)\s-\s([\w\s\.\,&/\’\'"\-]+)',expand=True)

    joey_diaz = joey_diaz[pd.notnull(joey_diaz['guests'])]
    joey_diaz['guests'] = [g.lstrip() for g in joey_diaz['guests']]
    joey_diaz['guests'] = [g.rstrip() for g in joey_diaz['guests']]

    guest_split_last('guest ', joey_diaz)
    
    replace("The Church Of What's Happening Now", np.nan, joey_diaz)
    replace("The Church Of What's Happening Now ", np.nan, joey_diaz)
    replace("The Chuch Of What's Happening Now", np.nan, joey_diaz)
    joey_diaz = joey_diaz[joey_diaz.guests.str.contains('Church') == False]
    joey_diaz = joey_diaz[joey_diaz.guests.str.contains('Calls') == False]
    joey_diaz = joey_diaz[joey_diaz.guests.str.contains('Peter Segal') == False]

    replace('Lee Syatt 4', 'Lee Syatt', joey_diaz)
    replace('"Big" John McCarthy', 'Big John McCarthy', joey_diaz)
    
    joey_diaz = joey_diaz[pd.notnull(joey_diaz['guests'])]
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ', and ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ', ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' & ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' And ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' and ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' with ')

    replace('Steven Brody Stevens', 'Brody Stevens', joey_diaz)

    # replace('Lee Syatt with Uncle Mike', 'Lee Syatt and Uncle Mike', joey_diaz)
    # joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' and ')

    return joey_diaz


def clean_your_moms_house(your_moms_house):

    your_moms_house = xml_to_df(your_moms_house)

    ## Set Episode numbers
    
    your_moms_house['episode'] = your_moms_house.title.str.extract(r'([\d]+)\s?-',expand=True)

    date_parser(your_moms_house)
    
    your_moms_house['guests'] = your_moms_house.title.str.extract(r'(?:[\d]+-)?([\w\s]+)-',expand=True)
    your_moms_house['guests'] = your_moms_house.guests.str.extract(r'([\D]+)',expand=True)
    
    guest_split('Live', your_moms_house)
    guest_split('LIVE ', your_moms_house)

    replace('Episode ', np.nan, your_moms_house)
    
    your_moms_house = your_moms_house.replace(r'', np.nan, regex=True)
    
    for index, row in your_moms_house.iterrows():
        if(row['episode']=='255'):
            your_moms_house.at[index, 'guests'] = np.nan

    your_moms_house = your_moms_house[your_moms_house.guests.str.contains('Christmas') == False]
    your_moms_house = your_moms_house[your_moms_house.guests.str.contains('BONUS') == False]
    your_moms_house = your_moms_house[your_moms_house.guests.str.contains('Happy') == False]
    your_moms_house = your_moms_house[your_moms_house.guests.str.contains('The ') == False]
    
    your_moms_house = your_moms_house[pd.notnull(your_moms_house['guests'])]
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ', and ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ', ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ' & ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ' And ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ' and ')
    
    replace('Redban', 'Brian Redban', your_moms_house)
    replace('Wheeler Walker Jr', 'Wheeler Walker Jr.', your_moms_house)
    replace('Ms Pat', 'Ms. Pat', your_moms_house)

    return your_moms_house

def clean_harmontown(harmontown):
    
    harmontown = xml_to_df_summ(harmontown)

    date_parser(harmontown)
    
    harmontown = harmontown[harmontown.summary.str.contains('Featuring') == True]
    
    harmontown['guests'] = harmontown['summary']
    
    harmontown = harmontown.drop('summary', 1)
    
    guest_split_last('Featuring ', harmontown)
    
    ### Manual cleaning
    
    harmontown = harmontown[pd.notnull(harmontown['guests'])]
    harmontown = splitDataFrameList(harmontown, 'guests', ', and ')
    harmontown = splitDataFrameList(harmontown, 'guests', ', ')
    harmontown = splitDataFrameList(harmontown, 'guests', ' & ')
    harmontown = splitDataFrameList(harmontown, 'guests', ' And ')
    harmontown = splitDataFrameList(harmontown, 'guests', ' and ')
    
    guest_split('  Topics', harmontown)
    guest_split('!', harmontown)
    guests = [g.rstrip('.') for g in harmontown['guests']]
    harmontown['guests'] = guests
    
    replace('Kumail Nanjiani.', 'Kumail Nanjiani', harmontown)
    replace('DeMorge Brown…', 'DeMorge Brown', harmontown)
    replace('Spencer Crittenden, Church', 'Spencer Crittenden, Church', harmontown)
    harmontown = splitDataFrameList(harmontown, 'guests', ', ')
    replace('Cassandra Church. Watch the video at harmontown.com/live. Become a member', 'Church', harmontown)

    harmontown = harmontown[harmontown.guests.str.contains('then fights') == False]
    harmontown = harmontown[harmontown.guests.str.contains('missing ') == False]
    harmontown = harmontown[harmontown.guests.str.contains('emphysema') == False]
    harmontown = harmontown[harmontown.guests.str.contains('law enforcement') == False]
    harmontown = harmontown[harmontown.guests.str.contains('Special') == False]
    harmontown = harmontown[harmontown.guests.str.contains('victims') == False]
    harmontown = harmontown[harmontown.guests.str.contains('Thalidomide') == False]
    harmontown = harmontown[harmontown.guests.str.contains('cereal') == False]
    harmontown = harmontown[harmontown.guests.str.contains('Wreck it') == False]
    
    return harmontown



def clean_stefan_molyneux(stefan_molyneux):

    stefan_molyneux = xml_to_df(stefan_molyneux)

    ## Set Episode numbers
    
    stefan_molyneux['episode'] = stefan_molyneux.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser(stefan_molyneux)
    
    stefan_molyneux['guests'] = stefan_molyneux.title.str.extract(r'\| ([\w\s\.]+) and Stefan Molyneux',expand=True)

    stefan_molyneux = stefan_molyneux[pd.notnull(stefan_molyneux['guests'])]
    

    return stefan_molyneux


def clean_econtalk(econtalk):

    econtalk = xml_to_df(econtalk)

    date_parser(econtalk)
    
    econtalk['guests'] = econtalk.title.str.extract(r'([\w\s\.\,\']+) on',expand=True)
    guest_split(' on', econtalk)
    
    #econtalk = econtalk[pd.notnull(econtalk['guests'])]
    econtalk = splitDataFrameList(econtalk, 'guests', ', and ')
    econtalk = splitDataFrameList(econtalk, 'guests', ', ')
    econtalk = splitDataFrameList(econtalk, 'guests', ' & ')
    econtalk = splitDataFrameList(econtalk, 'guests', ' And ')
    econtalk = splitDataFrameList(econtalk, 'guests', ' and ')
    

    return econtalk


def clean_econtalk_archive(econtalk_archive):

    econtalk_archive = xml_to_df_desc(econtalk_archive)
        
    date_parser(econtalk_archive)
    
    econtalk_archive['guests'] = econtalk_archive.description.str.extract(r'([\w\s\'\.]+)',expand=True)
    econtalk_archive = econtalk_archive.drop('description', 1)
    
    guest_split(', ', econtalk_archive)
    guest_split(' of', econtalk_archive)
    guest_split(' talks', econtalk_archive)
    
    guest_split_last('Nobel Laureate ', econtalk_archive)
    guest_split_last('syndicated columnist ', econtalk_archive)
    guest_split_last('Investigative journalist ', econtalk_archive)
    guest_split_last('Author ', econtalk_archive)
    guest_split_last('Novelist ', econtalk_archive)
    guest_split_last('The legendary ', econtalk_archive)
            
    econtalk_archive = econtalk_archive[econtalk_archive.guests.str.contains('This is the') == False]
    econtalk_archive = econtalk_archive[econtalk_archive.guests.str.contains('EconTalk host') == False]
    econtalk_archive = econtalk_archive[econtalk_archive.guests.str.contains('In this bonus') == False]
    econtalk_archive = econtalk_archive[econtalk_archive.guests.str.contains('On April') == False]
    
    econtalk_archive = splitDataFrameList(econtalk_archive, 'guests', ' and ')

    return econtalk_archive


def clean_bill_maher(bill_maher):

    bill_maher = xml_to_df_subt(bill_maher)

    date_parser(bill_maher)
    
    bill_maher['guests'] = bill_maher.subtitle.str.extract(r'(?:guests\s(?:–|-)?\s?|guests are |guests \()([\w\s\.\,\'\`\’\(\)]+)(?: (?:– )?answer|. \(|\)|.$)',expand=True)
    
    guest_split('answer', bill_maher)
    guest_split_last('Secretary ', bill_maher)
    guest_split_last('are ', bill_maher)
    guest_split_last('panelists ', bill_maher)

    bill_maher = bill_maher.drop('subtitle', 1)



    
    bill_maher = bill_maher[pd.notnull(bill_maher['guests'])]
    bill_maher = splitDataFrameList(bill_maher, 'guests', ', and ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ', ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ' & ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ' And ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ' and ')

    replace('Senator Bernie Sanders (I-VT)', 'Bernie Sander', bill_maher)
    replace('Senator Bernie  Sanders (I-VT)', 'Bernie Sander', bill_maher)
    replace('Senator Bernie Sanders (I-VT)', 'Bernie Sander', bill_maher)
    replace('SE Cupp', 'S.E. Cupp', bill_maher)

    replace('former Rep. Harold Ford', 'Harold Ford Jr.', bill_maher)
    replace('Ralph Reed', 'Ralph Reed Jr.', bill_maher)
    replace('Jr.', np.nan, bill_maher)
    replace('Dr. Neil deGrasse Tyson', 'Neil deGrasse Tyson', bill_maher)

    bill_maher = bill_maher[pd.notnull(bill_maher['guests'])]

    # bill_maher['guests'] = [g.rstrip() for g in bill_maher['guests']]
    bill_maher['guests'] = [g.lstrip('(') for g in bill_maher['guests']]
    

    return bill_maher


def clean_pete_holmes(pete_holmes):

    pete_holmes = xml_to_df(pete_holmes)

    date_parser(pete_holmes)
    
    pete_holmes['guests'] = pete_holmes['title']
    
    guest_split(' Re-Release', pete_holmes)
    guest_split(' #', pete_holmes)
    guest_split(' Returns', pete_holmes)
    guest_split(' returns', pete_holmes)
    guest_split(' of ', pete_holmes)
    guest_split(' interviews', pete_holmes)
    guest_split(': ', pete_holmes)
    guest_split_last('are ', pete_holmes)
    guest_split_last('with ', pete_holmes)

    replace('Bert Kreischer Swapcast!', 'Bert Kreischer', pete_holmes)
    replace('Alex and Allyson Grey', 'Alex Grey and Allyson Grey', pete_holmes)

    pete_holmes = pete_holmes[pete_holmes.guests.str.contains(r'Special') == False]
    pete_holmes = pete_holmes[pete_holmes.guests.str.contains(r'Live') == False]
    pete_holmes = pete_holmes[pete_holmes.guests.str.contains(r'The ') == False]
    pete_holmes = pete_holmes[pete_holmes.guests.str.contains(r'Thanksgiving') == False]
    pete_holmes = pete_holmes[pete_holmes.guests.str.contains(r'Best Of') == False]
    pete_holmes = pete_holmes[pete_holmes.guests.str.contains(r'Sketchfest') == False]
    
    pete_holmes = pete_holmes[pd.notnull(pete_holmes['guests'])]
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ', and ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ', ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ' & ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ' And ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ' and ')

    replace('TJ Miller', 'T.J. Miller', pete_holmes)
    

    return pete_holmes


def clean_anna_faris(anna_faris):

    anna_faris = xml_to_df(anna_faris)

    date_parser(anna_faris)
    
    anna_faris['guests'] = anna_faris.title.str.extract(r'(?:ep [\d]+: )?([\w\s\.\,\'\`\’\-\/]+)',expand=True)

    guest_split(' Pt.', anna_faris)
    guest_split(' Returns', anna_faris)
    guest_split(' Live', anna_faris)
    guest_split('/', anna_faris)
    guest_split_last(' with ', anna_faris)
    guest_split_last('Attorney ', anna_faris)

    replace('My Favorite Murder Crossover', 'Karen Kilgariff and Georgia Hardstark', anna_faris)
    replace("2 Dope Queens' Phoebe Robinson", 'Phoebe Robinson', anna_faris)
    replace('Jack and Karen Faris/Alison Rosen', 'Jack Faris, Karen Faris, Alison Rosen', anna_faris)
    
    anna_faris = anna_faris[pd.notnull(anna_faris['guests'])]
    anna_faris = splitDataFrameList(anna_faris, 'guests', ', and ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ', ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ' & ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ' And ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ' and ')

    anna_faris = anna_faris[anna_faris.guests.str.contains(r'ep ') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'Birthday ') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'USC ') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'Memorable Moments') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'An Unqualified Engagement') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'Birthday') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'Bonus') == False]
    anna_faris = anna_faris[anna_faris.guests.str.contains(r'Coming soon') == False]
    
    return anna_faris


def clean_dax_shepard(dax_shepard):

    dax_shepard = xml_to_df(dax_shepard)

    date_parser(dax_shepard)
    
    dax_shepard['guests'] = dax_shepard['title']
    
    guest_split_last('with ', dax_shepard)
    
    return dax_shepard


def clean_grapefruit_simmons(grapefruit_simmons):

    grapefruit_simmons = xml_to_df(grapefruit_simmons)

    date_parser(grapefruit_simmons)
    
    grapefruit_simmons['guests'] = grapefruit_simmons['title']
    
    guest_split(' -', grapefruit_simmons)
    guest_split(' Is', grapefruit_simmons)
    

    grapefruit_simmons = splitDataFrameList(grapefruit_simmons, 'guests', ' and ')
    
    replace('Christina P', 'Christina Pazsitzky', grapefruit_simmons)
    replace('Christina P.', 'Christina Pazsitzky', grapefruit_simmons)
    
    return grapefruit_simmons


def clean_sam_tripoli(sam_tripoli):

    sam_tripoli = xml_to_df(sam_tripoli)

    date_parser(sam_tripoli)
    
    sam_tripoli['guests'] = sam_tripoli.title.str.extract(r'(?:with|The Naughty Show \#[\d]+(?: - |: ))([\w\s\.\,\'\`\’\!\"\&]+)',expand=True)
    
    guest_split(' is', sam_tripoli)
    guest_split(' Returns', sam_tripoli)
    guest_split(' plus', sam_tripoli)
    guest_split(' Gets', sam_tripoli)
    guest_split(' Forever', sam_tripoli)
    guest_split(' Brings', sam_tripoli)
    guest_split(' Rate', sam_tripoli)
    guest_split(' Overdrive', sam_tripoli)
    guest_split(' Revisited', sam_tripoli)
    guest_split(" Can't Lose", sam_tripoli)
    guest_split_last('with ', sam_tripoli)
    guest_split_last('With ', sam_tripoli)
    guest_split_last('Warrior ', sam_tripoli)
    guest_split_last('Gweed ', sam_tripoli)
    guest_split_last("Vice's ", sam_tripoli)
    guest_split_last("Expert ", sam_tripoli)
    guest_split_last("Burgers' ", sam_tripoli)
    guest_split_last("Director ", sam_tripoli)

    replace('Garfunkel & Oates', 'Riki Lindhome & Kate Micucci', sam_tripoli)
    replace('Dana & Julia', 'Dana Min Goodman & Julia Wolov', sam_tripoli)
    
    sam_tripoli = sam_tripoli[pd.notnull(sam_tripoli['guests'])]
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ', and ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ', ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ' & ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ' And ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ' and ')
    
    sam_tripoli['guests'] = [g.lstrip() for g in sam_tripoli['guests']]

    
    replace("the Pirate Life Radio's Tait Fletcher", 'Tait Fletcher', sam_tripoli)
    replace("The Doug Stanhope Podcast", 'Doug Stanhope', sam_tripoli)
    replace('Henry "The Polish Starseed" Zebrowski', 'Henry Zebrowski', sam_tripoli)
    replace('Redban', 'Brian Redban', sam_tripoli)
    replace('Dr. Redban', 'Brian Redban', sam_tripoli)
    replace('Rock', np.nan, sam_tripoli)
    replace('Reid', 'Riley Reid', sam_tripoli)
    replace('Hadley', 'Jason Hadley', sam_tripoli)
    replace('Chaos', 'Veronica Chaos', sam_tripoli)
    replace('Identical Twins', 'Cory & Chad', sam_tripoli)
    replace('Duncan', 'Duncan Trussell', sam_tripoli)
    replace('Roy Wood Jr', 'Roy Wood Jr.', sam_tripoli)
    replace('Danica', 'Danica Dillon', sam_tripoli)
    
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(r' Show') == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(r'Bingle') == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("the ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("The ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("When ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Sugar ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" gets ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Top ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Simply ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Simple ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" Dongs") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" vs. ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" Fun") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Save ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" from ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" Seen ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" of ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" a ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" for ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" It ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" Wedding ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Ep2") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("No ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" No") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Bingle ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("It's") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" Are ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" RubMaps") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" To ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" to ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("420 ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Lawyer") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" on ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Crunch") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Magic ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Prison ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Book") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Defense") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Back") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Vomit") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Ex") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("NBH") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Carousel") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Pie") == False]
    #sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Boats") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Girls") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Skittles") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Santa") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Nerds") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Recovery") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Boyfriend") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Person") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Chest") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Cliffhanger") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" News") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains(" Us") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Fake ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Games") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Ma'am") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Average ") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Sam Tripoli") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Taken") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Smallest") == False]
    sam_tripoli = sam_tripoli[sam_tripoli.guests.str.contains("Audition") == False]

    replace('All', np.nan, sam_tripoli)
    
    for index, row in sam_tripoli.iterrows():
        if(pd.notnull(row['guests'])):
            sam_tripoli.at[index, 'guests'] = row['guests'].title()

    sam_tripoli.replace('', np.nan, regex=True, inplace=True)
    sam_tripoli = sam_tripoli[pd.notnull(sam_tripoli['guests'])]

    sam_tripoli['guests'] = [g.rstrip('.') for g in sam_tripoli['guests']]
    sam_tripoli['guests'] = [g.rstrip('!') for g in sam_tripoli['guests']]
    sam_tripoli['guests'] = [g.rstrip() for g in sam_tripoli['guests']]
    
    return sam_tripoli


def clean_alison_rosen(alison_rosen):

    alison_rosen = xml_to_df(alison_rosen)
    
    date_parser(alison_rosen)
    
    alison_rosen['guests'] = alison_rosen['title']
    
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(r'[\w]\'s') == False]

    guest_split(' - Part', alison_rosen)
    guest_split(' Returns', alison_rosen)
    guest_split(' LIVE', alison_rosen)
    guest_split(' Live', alison_rosen)
    guest_split(' aka', alison_rosen)
    guest_split(' (', alison_rosen)
    guest_split(' -', alison_rosen)
    guest_split(r' #', alison_rosen)
    
    guest_split_last('with ', alison_rosen)
    guest_split_last('guests ', alison_rosen)
    
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('!') == False]
    
    replace('The Sklar Brothers', 'Jason Sklar, Randy Sklar', alison_rosen)
    replace('Hungry Girl', 'Lisa Lillien', alison_rosen)
    replace('Wendy and Lizzie Molyneux ', 'Wendy Molyneux and Lizzie Molyneux', alison_rosen)
    replace('Wheeler Walker, Jr.', 'Wheeler Walker Jr.', alison_rosen)
    replace('Emily Gordon', 'Emily V. Gordon', alison_rosen)
    
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Your ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Named ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Phone Calls') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Baby ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Sleep ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Cosmic ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Happy ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' Call') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' of ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' in ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' We ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Too ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Boners') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Shower') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Sandwiches') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('The ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Fake ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Hillicopters') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Soft') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Hands') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Update') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' a ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' to ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Hard ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('New ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' Face') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Spiders') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Special') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Talk') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' the ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Show') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' Is ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Quiz') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(r'\?') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Things') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Bonus') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Trees') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Soup') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Projection') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Pranks') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Email') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Trash') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Book') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Got ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' from ') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' Gang') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Knives') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(' Gang') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Judges') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Holes') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Judges') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('Drop-Offs') == False]
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('We Feel') == False]
    
    alison_rosen = alison_rosen[pd.notnull(alison_rosen['guests'])]
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ', and ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ', ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' & ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' And ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' and ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' / ')
    
    replace('Christina P', 'Christina Pazsitzky', alison_rosen)
    replace('Jason', 'Jason Sklar', alison_rosen)
    replace('Gary', 'Gary Smith', alison_rosen)
    replace('Chris', 'Chris Laxamana', alison_rosen)
    replace('Chris Laxamana-Maxipada', 'Chris Laxamana', alison_rosen)
    replace('Jenna', 'Jenna Kim Jones', alison_rosen)
    replace('Matt', 'Matt Fondiler', alison_rosen)
    
    alison_rosen['guests'] = [g.rstrip(',') for g in alison_rosen['guests']]
    
    return alison_rosen



def clean_chris_ryan(chris_ryan):

    chris_ryan = xml_to_df(chris_ryan)
    
    chris_ryan['episode'] = chris_ryan.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser(chris_ryan)
    
    chris_ryan['guests'] = chris_ryan.title.str.extract(r'(?:[\d]+\s-\s)([^(]+)',expand=True)
    
    guest_split(' In', chris_ryan)
    guest_split(' in', chris_ryan)
    guest_split(' Returns', chris_ryan)
    guest_split(' Blowin', chris_ryan)
    guest_split(' Doesn', chris_ryan)
    guest_split(' on ', chris_ryan)
    guest_split_last('with ', chris_ryan)
    guest_split_last('With ', chris_ryan)

    replace('Joe and Shannon', 'Joe Winke and Shannon Drake', chris_ryan)
    replace('Shrimp Parade', 'Joe Rogan and Duncan Trussell', chris_ryan)
    
    chris_ryan = chris_ryan[chris_ryan.guests.str.contains('Special') == False]
    chris_ryan = chris_ryan[chris_ryan.guests.str.contains('ROMA') == False]
    chris_ryan = chris_ryan[chris_ryan.guests.str.contains('TOMA') == False]
    
    chris_ryan = chris_ryan[pd.notnull(chris_ryan['guests'])]
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ', and ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ', ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ' & ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ' And ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ' and ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', '/')

    chris_ryan = chris_ryan[chris_ryan.guests.str.contains('Friends') == False]
    chris_ryan = chris_ryan[chris_ryan.guests.str.contains('Center') == False]
    
    replace('Daniel Bolelli', 'Daniele Bolelli', chris_ryan)
    replace('Daniele Bolleli', 'Daniele Bolelli', chris_ryan)
    replace('Danielle Bolleli', 'Daniele Bolelli', chris_ryan)
    replace('Danielle Bolelli', 'Daniele Bolelli', chris_ryan)
    replace("In Jake Johannsen's Kitchen", 'Jake Johannsen', chris_ryan)
    
    return chris_ryan


def clean_hdtgm(hdtgm):

    hdtgm = xml_to_df(hdtgm)
    
    hdtgm['episode'] = hdtgm.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser(hdtgm)
    
    hdtgm['guests'] = hdtgm.title.str.extract(r'\(w\/ ([^)]+)',expand=True)
    
    guest_split(' In', hdtgm)
    guest_split(' in', hdtgm)
    guest_split_last('with ', hdtgm)
    guest_split_last('With ', hdtgm)
    
    hdtgm = hdtgm[hdtgm.title.str.contains('Prequel') == False]
    
    hdtgm = hdtgm[pd.notnull(hdtgm['guests'])]
    hdtgm = splitDataFrameList(hdtgm, 'guests', ', and ')
    hdtgm = splitDataFrameList(hdtgm, 'guests', ', ')
    hdtgm = splitDataFrameList(hdtgm, 'guests', ' & ')
    hdtgm = splitDataFrameList(hdtgm, 'guests', ' And ')
    hdtgm = splitDataFrameList(hdtgm, 'guests', ' and ')
    
    return hdtgm


def clean_todd_glass(todd_glass):

    todd_glass = xml_to_df(todd_glass)
    
    todd_glass['episode'] = todd_glass.title.str.extract(r'([\d\.]+)-\s',expand=True)

    date_parser(todd_glass)
    
    todd_glass['guests'] = todd_glass.title.str.extract(r'[\d\.]+-\s([\w\s\.\,\'\`\’\&\-]+)',expand=True)

    replace('John Mulaney and Part 2 with Eric Ohlsen', 'John Mulaney and Eric Ohlsen', todd_glass)
    
    guest_split(' Part', todd_glass)
    guest_split(' part', todd_glass)
    guest_split('Live', todd_glass)
    guest_split(' returns', todd_glass)
    guest_split(' Returns', todd_glass)
    guest_split(' is', todd_glass)
    guest_split(' Presents', todd_glass)
    guest_split_last('with ', todd_glass)
    guest_split_last('ALMOST ', todd_glass)
    guest_split_last('Almost ', todd_glass)
    
    todd_glass = todd_glass[todd_glass.guests.str.contains('HAPPY') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Show') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('show') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Best ') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('The ') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Christmas') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Bonus') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('a special') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains(' from ') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Special') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Camping') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('episode') == False]

    
    todd_glass = todd_glass[pd.notnull(todd_glass['guests'])]
    todd_glass = splitDataFrameList(todd_glass, 'guests', ', and ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ', ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ', & ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ' & ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ' And ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ' and ')
    
    replace('Daniel', 'Daniel Kinno', todd_glass)
    replace('Hope', np.nan, todd_glass)
    replace('Child Therapist', np.nan, todd_glass)
    replace('', np.nan, todd_glass)
    replace('& Ian Karmel', 'Ian Karmel', todd_glass)
    replace('Todd', np.nan, todd_glass)
    todd_glass = todd_glass[pd.notnull(todd_glass['guests'])]

    todd_glass = todd_glass[todd_glass.guests.str.contains('the gang') == False]
    
    return todd_glass

def clean_dumb_people_town(dumb_people_town):

    dumb_people_town = xml_to_df(dumb_people_town)

    date_parser(dumb_people_town)
    
    dumb_people_town['guests'] = dumb_people_town.title.str.extract(r'(?:Minisode: )?([\w\s\.\,\'\`\’\&]+)\s-',expand=True)
    
    guest_split(' pt.', dumb_people_town)
    
    dumb_people_town = dumb_people_town[dumb_people_town.guests.str.contains(r'\d') == False]
    dumb_people_town = dumb_people_town[dumb_people_town.guests.str.contains('Solution') == False]
    
    dumb_people_town = dumb_people_town[pd.notnull(dumb_people_town['guests'])]
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ', and ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ', ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ' & ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ' And ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ' and ')
    
    replace('Joey CoCo Diaz', 'Joey Diaz', dumb_people_town)
    
    return dumb_people_town


def clean_doug_loves_movies(doug_loves_movies):

    doug_loves_movies = xml_to_df(doug_loves_movies)

    date_parser(doug_loves_movies)
    
    doug_loves_movies['guests'] = doug_loves_movies.title.str.extract(r'([\w\s\.\,\'\`\’\&\"]+)\sguest',expand=True)

    doug_loves_movies = doug_loves_movies[doug_loves_movies.guests.str.contains('"Mark Wahlberg"') == False]
    doug_loves_movies = doug_loves_movies[doug_loves_movies.guests.str.contains('others') == False]


    doug_loves_movies = doug_loves_movies[pd.notnull(doug_loves_movies['guests'])]
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ', and ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ', ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ' & ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ' And ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ' and ')

    doug_loves_movies = doug_loves_movies[doug_loves_movies.guests.str.contains('an audience') == False]
    doug_loves_movies = doug_loves_movies[doug_loves_movies.guests.str.contains(r'\d') == False]

    replace('Joey CoCo Diaz', 'Joey Diaz', doug_loves_movies)
    replace('more', np.nan, doug_loves_movies)
    doug_loves_movies = doug_loves_movies[pd.notnull(doug_loves_movies['guests'])]
    
    return doug_loves_movies

def clean_getting_doug_with_high(getting_doug_with_high):

    getting_doug_with_high = xml_to_df(getting_doug_with_high)
    
    getting_doug_with_high['episode'] = getting_doug_with_high.title.str.extract(r'E[pP] ([\d]+)',expand=True)

    date_parser(getting_doug_with_high)
    
    getting_doug_with_high['guests'] = getting_doug_with_high.title.str.extract(r'E[pP] [\d]+\s([\w\s\.\,\'\`\’\&\"\-]+)\s(?:\||\-)',expand=True)

    guest_split_last(' - ', getting_doug_with_high)

    getting_doug_with_high = getting_doug_with_high[pd.notnull(getting_doug_with_high['guests'])]
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ', and ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ', & ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ', ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' & ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' And ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' and ')

    getting_doug_with_high = getting_doug_with_high[getting_doug_with_high.guests.str.contains('pt. ') == False]
    getting_doug_with_high = getting_doug_with_high[getting_doug_with_high.guests.str.contains('Getting Doug') == False]

    replace('Joey CoCo Diaz', 'Joey Diaz', getting_doug_with_high)
    replace('Jay Oakerson', 'Big Jay Oakerson', getting_doug_with_high)
    replace('The Sklar Brothers', 'Jason Sklar and Randy Sklar', getting_doug_with_high)
    replace('Adam, Blake, & Anders from Workaholics', 'Adam Devine, Anders Holm, Blake Anderson', getting_doug_with_high)
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' and ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ', ')
    
    return getting_doug_with_high

def clean_who_charted(who_charted):

    who_charted = xml_to_df(who_charted)
    
    who_charted['episode'] = who_charted.title.str.extract(r'([\d]+)',expand=True)

    date_parser(who_charted)
    
    who_charted['guests'] = who_charted.title.str.extract(r'[\d]+\s([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)

    who_charted = who_charted[pd.notnull(who_charted['guests'])]
    who_charted = splitDataFrameList(who_charted, 'guests', ', and ')
    who_charted = splitDataFrameList(who_charted, 'guests', ', ')
    who_charted = splitDataFrameList(who_charted, 'guests', ' & ')
    who_charted = splitDataFrameList(who_charted, 'guests', ' And ')
    who_charted = splitDataFrameList(who_charted, 'guests', ' and ')

    return who_charted


def clean_the_indoor_kids(the_indoor_kids):

    the_indoor_kids = xml_to_df(the_indoor_kids)
    
    the_indoor_kids['episode'] = len(the_indoor_kids) - the_indoor_kids.index
    
    date_parser(the_indoor_kids)
    
    the_indoor_kids['guests'] = the_indoor_kids.title.str.extract(r'(?:with |w/)([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)

    for index, row in the_indoor_kids.iterrows():
        if(row['episode']==1):
            the_indoor_kids.at[index, 'guests'] = 'Steve Agee'
        if(row['episode']==2):
            the_indoor_kids.at[index, 'guests'] = 'Justin Roiland'
        if(row['episode']==3):
            the_indoor_kids.at[index, 'guests'] = 'Emily V. Gordon and Pete Holmes'
        if(row['episode']==4):
            the_indoor_kids.at[index, 'guests'] = 'Todd Levin'
        if(row['episode']==5):
            the_indoor_kids.at[index, 'guests'] = 'Jordan Morris'
        if(row['episode']==6):
            the_indoor_kids.at[index, 'guests'] = 'Carlos Ferro'
        if(row['episode']==7):
            the_indoor_kids.at[index, 'guests'] = 'Moshe Kasher and Brent Weinbach'
        if(row['episode']==9):
            the_indoor_kids.at[index, 'guests'] = 'Dominic Dierkes'
        if(row['episode']==10):
            the_indoor_kids.at[index, 'guests'] = 'Aisha Tyler'

    the_indoor_kids = the_indoor_kids[the_indoor_kids.guests.str.contains('episode') == False]

    replace('John And Susan', 'John Mathot and Susan Wright', the_indoor_kids)
    
    the_indoor_kids = the_indoor_kids[pd.notnull(the_indoor_kids['guests'])]
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ', and ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ', ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ' & ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ' And ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ' and ')

    replace('and... Eliza Dushku', 'Eliza Dushku', the_indoor_kids)
    replace('Mira', 'Matt Mira', the_indoor_kids)
    replace('Kumail', np.nan, the_indoor_kids)
    replace('Emily', np.nan, the_indoor_kids)
    replace('The Indoor Kids', np.nan, the_indoor_kids)
    replace('Ovenshire', 'Josh Ovenshire', the_indoor_kids)
    replace('more', np.nan, the_indoor_kids)
    replace('much more', np.nan, the_indoor_kids)
    replace('a Cavalcade of Stars', np.nan, the_indoor_kids)

    the_indoor_kids = the_indoor_kids[pd.notnull(the_indoor_kids['guests'])]

    
    return the_indoor_kids


def clean_comedy_film_nerds(comedy_film_nerds):

    comedy_film_nerds = xml_to_df(comedy_film_nerds)

    comedy_film_nerds['episode'] = comedy_film_nerds.title.str.extract(r'(Ep [\d]+)',expand=True)
    
    date_parser(comedy_film_nerds)
    
    comedy_film_nerds['guests'] = comedy_film_nerds.title.str.extract(r'(?:Ep [\d]+ - [\w\s\.\,\'\`\’\&\"\-\:]+)(?: - )([\w\s\.\,\'\`\’\&\"\-]+)$',expand=True)

    replace('The Sklar Brothers', 'Jason Sklar, Randy Sklar', comedy_film_nerds)
    
    comedy_film_nerds = comedy_film_nerds[pd.notnull(comedy_film_nerds['guests'])]
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ', and ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ', ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ' & ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ' And ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ' and ')

    replace('Graham', np.nan, comedy_film_nerds)
    replace('Chris', np.nan, comedy_film_nerds)

    comedy_film_nerds = comedy_film_nerds[pd.notnull(comedy_film_nerds['guests'])]

    
    return comedy_film_nerds

def clean_the_champs(the_champs):

    the_champs = xml_to_df(the_champs)
    
    date_parser(the_champs)
    
    the_champs['guests'] = the_champs.title.str.extract(r'([^(]+)',expand=True)
    
    guest_split(' Returns', the_champs)
    guest_split_last('- ', the_champs)
    guest_split_last(': ', the_champs)
    guest_split_last('/', the_champs)
    guest_split_last(r"'s", the_champs)
    guest_split_last(r"' ", the_champs)
    guest_split_last('writer ', the_champs)

    replace('Roy Woodm, Jr.', 'Roy Wood Jr.', the_champs)
    replace('Arsenio', 'Arsenio Hall', the_champs)
    replace('Shawn + Marlon Wayans', 'Shawn Wayans + Marlon Wayans', the_champs)
    replace('Bashir + Diallo', 'Bashir Sallahudin and Diallo Riddle', the_champs)
    

    the_champs = the_champs[the_champs.guests.str.contains('New Faces') == False]
    
    the_champs = the_champs[pd.notnull(the_champs['guests'])]
    the_champs = splitDataFrameList(the_champs, 'guests', ', and ')
    the_champs = splitDataFrameList(the_champs, 'guests', ', ')
    the_champs = splitDataFrameList(the_champs, 'guests', ' & ')
    the_champs = splitDataFrameList(the_champs, 'guests', ' And ')
    the_champs = splitDataFrameList(the_champs, 'guests', ' and ')
    the_champs = splitDataFrameList(the_champs, 'guests', ' + ')
    
    the_champs['guests'] = [g.rstrip() for g in the_champs['guests']]

    replace('Golden State Warrior Harrison Barnes', 'Harrison Barnes', the_champs)
    replace('NBA Star Blake Griffin', 'Blake Griffin', the_champs)
    replace('Musician Flying Lotus', 'Flying Lotus', the_champs)
    replace('Key', 'Keegan-Michael Key', the_champs)
    replace('Donnell "Ashy Larry" Rawlings', 'Donnell Rawlings', the_champs)
    replace('Superhead', 'Karrine Steffans', the_champs)
    replace('NBA All-Star Baron Davis', 'Baron Davis', the_champs)
    replace('Founder of World Star Hip Hop', np.nan, the_champs)

    the_champs = the_champs[pd.notnull(the_champs['guests'])]


    return the_champs


def clean_julian_loves_music(julian_loves_music):

    julian_loves_music = xml_to_df(julian_loves_music)
    
    date_parser(julian_loves_music)
    
    julian_loves_music['guests'] = julian_loves_music.title.str.extract(r'([^(]+)',expand=True)
    
    guest_split(' guest', julian_loves_music)

    replace('Julian Loves Music*', np.nan, julian_loves_music)
    
    julian_loves_music = julian_loves_music[pd.notnull(julian_loves_music['guests'])]
    julian_loves_music = splitDataFrameList(julian_loves_music, 'guests', ', and ')
    julian_loves_music = splitDataFrameList(julian_loves_music, 'guests', ', ')
    julian_loves_music = splitDataFrameList(julian_loves_music, 'guests', ' & ')
    julian_loves_music = splitDataFrameList(julian_loves_music, 'guests', ' And ')
    julian_loves_music = splitDataFrameList(julian_loves_music, 'guests', ' and ')

    return julian_loves_music

def clean_chris_cubas(chris_cubas):

    chris_cubas = xml_to_df(chris_cubas)
    
    chris_cubas['episode'] = chris_cubas.title.str.extract(r'Canceled Ep. ([\d]+)',expand=True)
    
    date_parser(chris_cubas)
    
    chris_cubas['guests'] = chris_cubas.title.str.extract(r'w/ ([^(]+)',expand=True)

    replace('Ralpie Hardesty', 'Ralphie Hardesty', chris_cubas)
    replace('Avery Moorre', 'Avery Moore', chris_cubas)
    
    chris_cubas = chris_cubas[pd.notnull(chris_cubas['guests'])]
    chris_cubas = splitDataFrameList(chris_cubas, 'guests', ', and ')
    chris_cubas = splitDataFrameList(chris_cubas, 'guests', ', ')
    chris_cubas = splitDataFrameList(chris_cubas, 'guests', ' & ')
    chris_cubas = splitDataFrameList(chris_cubas, 'guests', ' And ')
    chris_cubas = splitDataFrameList(chris_cubas, 'guests', ' and ')

    return chris_cubas


def clean_thomas_thakkar(thomas_thakkar):

    thomas_thakkar = xml_to_df(thomas_thakkar)
    
    thomas_thakkar['episode'] = thomas_thakkar.title.str.extract(r'Canceled Ep. ([\d]+)',expand=True)
    
    date_parser(thomas_thakkar)
    
    thomas_thakkar['guests'] = thomas_thakkar.title.str.extract(r'with ([^(]+)',expand=True)
    
    guest_split(' from', thomas_thakkar)
    guest_split(' preview', thomas_thakkar)
    
    thomas_thakkar = thomas_thakkar[pd.notnull(thomas_thakkar['guests'])]
    thomas_thakkar = splitDataFrameList(thomas_thakkar, 'guests', ', and ')
    thomas_thakkar = splitDataFrameList(thomas_thakkar, 'guests', ', ')
    thomas_thakkar = splitDataFrameList(thomas_thakkar, 'guests', ' & ')
    thomas_thakkar = splitDataFrameList(thomas_thakkar, 'guests', ' And ')
    thomas_thakkar = splitDataFrameList(thomas_thakkar, 'guests', ' and ')

    return thomas_thakkar


def clean_iliza(iliza):

    iliza = xml_to_df(iliza)
        
    date_parser(iliza)
    
    iliza['guests'] = iliza.title.str.extract(r'([^(]+)',expand=True)
    
    guest_split(' REVISITED', iliza)
    guest_split(' Returns', iliza)
    guest_split(' of ', iliza)
    
    iliza = iliza[iliza.guests.str.contains('Special') == False]
    iliza = iliza[iliza.guests.str.contains('BEST OF') == False]
    iliza = iliza[iliza.guests.str.contains('Rolling Solo') == False]
    
    iliza = iliza[pd.notnull(iliza['guests'])]
    iliza = splitDataFrameList(iliza, 'guests', ', and ')
    iliza = splitDataFrameList(iliza, 'guests', ', ')
    iliza = splitDataFrameList(iliza, 'guests', ' & ')
    iliza = splitDataFrameList(iliza, 'guests', ' And ')
    iliza = splitDataFrameList(iliza, 'guests', ' and ')

    return iliza


def clean_race_wars(race_wars):

    race_wars = xml_to_df(race_wars)
        
    date_parser(race_wars)
    
    race_wars['guests'] = race_wars.title.str.extract(r'(?:With |w/\s?|W/)([^(^)]+)',expand=True)
    
    guest_split_last('w/ ', race_wars)
    guest_split_last('Legends ', race_wars)

    for index, row in race_wars.iterrows():
        if(pd.notnull(row['guests'])):
            race_wars.at[index, 'guests'] = row['guests'].title()
            
    replace('Dante Nero Dick Cox Michael Brooks', 'Dante Nero, Dick Cox, Michael Brooks', race_wars)
    
    race_wars = race_wars[pd.notnull(race_wars['guests'])]
    race_wars = splitDataFrameList(race_wars, 'guests', ', and ')
    race_wars = splitDataFrameList(race_wars, 'guests', ', & ')
    race_wars = splitDataFrameList(race_wars, 'guests', ', ')
    race_wars = splitDataFrameList(race_wars, 'guests', ' & ')
    race_wars = splitDataFrameList(race_wars, 'guests', ' And ')
    race_wars = splitDataFrameList(race_wars, 'guests', ' and ')
    race_wars = splitDataFrameList(race_wars, 'guests', ' Feat. ')

    replace('Sa', 'SA', race_wars)
    replace('Michael Wood Jr', 'Michael Wood Jr.', race_wars)

    return race_wars

def clean_todd_barry(todd_barry):

    todd_barry = xml_to_df(todd_barry)
        
    date_parser(todd_barry)
    
    todd_barry['guests'] = todd_barry.title.str.extract(r'(?:LIVE: )?([^(^)]+)',expand=True)
            
    todd_barry = todd_barry[todd_barry.guests.str.contains('LIVE') == False]
    todd_barry = todd_barry[todd_barry.guests.str.contains('Live') == False]

    guest_split_last('with ', todd_barry)
    guest_split_last("it's ", todd_barry)

    replace('Jim & Jeannie Gaffigan', 'Jim Gaffigan & Jeannie Gaffigan', todd_barry)
    
    todd_barry = todd_barry[pd.notnull(todd_barry['guests'])]
    todd_barry = splitDataFrameList(todd_barry, 'guests', ', and ')
    todd_barry = splitDataFrameList(todd_barry, 'guests', ', ')
    todd_barry = splitDataFrameList(todd_barry, 'guests', ' & ')
    todd_barry = splitDataFrameList(todd_barry, 'guests', ' And ')
    todd_barry = splitDataFrameList(todd_barry, 'guests', ' and ')

    todd_barry['guests'] = [g.rstrip('!') for g in todd_barry['guests']]

    return todd_barry


def clean_my_dumb_friends(my_dumb_friends):#needs more cleaning

    my_dumb_friends = xml_to_df(my_dumb_friends)
        
    date_parser(my_dumb_friends)
    
    my_dumb_friends['guests'] = my_dumb_friends.title.str.extract(r'(?:[\w\s]+ \#\d+)(?:\s?: | - )([\w\s\'\&\.\+]+)',expand=True)
            
    guest_split(' from', my_dumb_friends)
    guest_split_last('guest ', my_dumb_friends)
    guest_split_last('Guest ', my_dumb_friends)
    guest_split_last(' of ', my_dumb_friends)
    guest_split_last(' Of ', my_dumb_friends)
    guest_split_last(' with ', my_dumb_friends)

    replace('Lucas Brothers', 'Kenneth Lucas, Keith Lucas', my_dumb_friends)
        
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains('LIVE') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(' in ') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains('Mailbag') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'\+') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'Dumb Things') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'Greatest Hits') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'The Skype One') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'WOMEN') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'Haunting') == False]
    my_dumb_friends = my_dumb_friends[my_dumb_friends.guests.str.contains(r'Dan & Sean') == False]

    my_dumb_friends['guests'] = [g.rstrip() for g in my_dumb_friends['guests']]

    replace('Dan', 'Dan St. Germain', my_dumb_friends)
    replace('Sean', 'Sean Donnelly', my_dumb_friends)
    
    my_dumb_friends = my_dumb_friends[pd.notnull(my_dumb_friends['guests'])]
    my_dumb_friends = splitDataFrameList(my_dumb_friends, 'guests', ', and ')
    my_dumb_friends = splitDataFrameList(my_dumb_friends, 'guests', ', ')
    my_dumb_friends = splitDataFrameList(my_dumb_friends, 'guests', ' & ')
    my_dumb_friends = splitDataFrameList(my_dumb_friends, 'guests', ' And ')
    my_dumb_friends = splitDataFrameList(my_dumb_friends, 'guests', ' and ')

    replace('Luis Gomez', 'Luis J. Gomez', my_dumb_friends)

    return my_dumb_friends


def clean_pleasure_monkey(pleasure_monkey):

    pleasure_monkey = xml_to_df(pleasure_monkey)
        
    date_parser(pleasure_monkey)
    
    pleasure_monkey['guests'] = pleasure_monkey.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(' from', pleasure_monkey)

    replace('Rick and Josh William ', 'Rick William and Josh William', pleasure_monkey)
    
    pleasure_monkey = pleasure_monkey[pd.notnull(pleasure_monkey['guests'])]
    pleasure_monkey = splitDataFrameList(pleasure_monkey, 'guests', ', and ')
    pleasure_monkey = splitDataFrameList(pleasure_monkey, 'guests', ', ')
    pleasure_monkey = splitDataFrameList(pleasure_monkey, 'guests', ' & ')
    pleasure_monkey = splitDataFrameList(pleasure_monkey, 'guests', ' And ')
    pleasure_monkey = splitDataFrameList(pleasure_monkey, 'guests', ' and ')

    pleasure_monkey['guests'] = [g.rstrip() for g in pleasure_monkey['guests']]

    return pleasure_monkey


def clean_steven_crowder(steven_crowder):

    steven_crowder = xml_to_df(steven_crowder)
    
    steven_crowder['episode'] = steven_crowder.title.str.extract(r'\#(\d+)',expand=True)
        
    date_parser(steven_crowder)
    
    steven_crowder['guests'] = steven_crowder.title.str.extract(r'\#?\d+([\w\s\.\,\'\`\’\&\"\-\!\?\:\$]+)',expand=True)
    
    guest_split_last('? ', steven_crowder)
    guest_split_last('! ', steven_crowder)
    guest_split_last('with ', steven_crowder)
    guest_split(' from', steven_crowder)
    guest_split(' Guest', steven_crowder)
    guest_split(' guest', steven_crowder)
    guest_split(' Talks', steven_crowder)
    guest_split(' Joins', steven_crowder)
    guest_split(' -', steven_crowder)
    guest_split(' Destroys', steven_crowder)

    replace('Jordan B. Peterson', 'Jordan Peterson', steven_crowder)
    
    steven_crowder['episode'] = pd.to_numeric(steven_crowder['episode'])
    steven_crowder = steven_crowder[steven_crowder['episode']>21]
    
    steven_crowder = steven_crowder[pd.notnull(steven_crowder['guests'])]
    steven_crowder = splitDataFrameList(steven_crowder, 'guests', ', and ')
    steven_crowder = splitDataFrameList(steven_crowder, 'guests', ', ')
    steven_crowder = splitDataFrameList(steven_crowder, 'guests', ' & ')
    steven_crowder = splitDataFrameList(steven_crowder, 'guests', ' And ')
    steven_crowder = splitDataFrameList(steven_crowder, 'guests', ' and ')

    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Mrs. Crowder') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('a Chinese') == False]
    replace('Sgt. Kathryn', 'Kathryn Haus', steven_crowder)
    replace('Jordan B. Peterson', 'Jordan Peterson', steven_crowder)

    steven_crowder = splitDataFrameList(steven_crowder, 'guests', '. ')
    steven_crowder['guests'] = [g.rstrip() for g in steven_crowder['guests']]

    replace('Queen', 'Notgay Jared', steven_crowder)
    replace('Nick DiPaolo Trigger', 'Nick DiPaolo', steven_crowder)
    replace('Milo', 'Milo Yiannopoulos', steven_crowder)
    replace("UFC's Chris Leben", 'Chris Leben', steven_crowder)
    replace('Gov', np.nan, steven_crowder)

    steven_crowder = steven_crowder[pd.notnull(steven_crowder['guests'])]
    
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains(r'[a-z]') == True]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains(':') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('!') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Crapping') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('"') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Nuff') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains(' Rapes ') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Plus') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Kasich Sucks') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Conservative Transgender') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Muslim') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Gets ') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Quits') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Hates') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Butts') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Oathkeepers') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Shooting') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Because') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains(' vs ') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains("'Stalker Jim Returns'") == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Inauguration') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Crippled') == False]
    steven_crowder = steven_crowder[steven_crowder.guests.str.contains('Papa Crowder') == False]

    guest_split(' Debates', steven_crowder)
    replace('RazörFist', 'RazorFist', steven_crowder)
    replace('Jordan B', 'Jordan Peterson', steven_crowder)
    guest_split('Dishes', steven_crowder)
    guest_split('Fire', steven_crowder)

    steven_crowder['guests'] = [g.rstrip() for g in steven_crowder['guests']]

    return steven_crowder


def clean_doughboys(doughboys):

    doughboys = xml_to_df(doughboys)
        
    date_parser(doughboys)
    
    doughboys['guests'] = doughboys.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    doughboys = doughboys[pd.notnull(doughboys['guests'])]
    doughboys = splitDataFrameList(doughboys, 'guests', ', and ')
    doughboys = splitDataFrameList(doughboys, 'guests', ', ')
    doughboys = splitDataFrameList(doughboys, 'guests', ' & ')
    doughboys = splitDataFrameList(doughboys, 'guests', ' And ')
    doughboys = splitDataFrameList(doughboys, 'guests', ' and ')

    doughboys = doughboys[doughboys.guests.str.contains('Episode') == False]
    guest_split(' Live', doughboys)

    doughboys['guests'] = [g.rstrip() for g in doughboys['guests']]

    return doughboys


def clean_bill_simmons(bill_simmons):

    bill_simmons = xml_to_df(bill_simmons)
        
    date_parser(bill_simmons)
    
    bill_simmons['guests1'] = bill_simmons.title.str.extract(r'([\w\s\.\s\&\']+)?(?: on [\w\s\.\s\&\']+)',expand=True)
    bill_simmons['guests2'] = bill_simmons.title.str.extract(r'w/ ([\w\s\.\s\&\']+)?',expand=True)
    bill_simmons.replace(np.nan, '', regex=True, inplace=True)
    bill_simmons['guests'] = bill_simmons['guests1'] + bill_simmons['guests2']  
    bill_simmons = bill_simmons.drop('guests1', 1)
    bill_simmons = bill_simmons.drop('guests2', 1)
    
    guest_split(' on', bill_simmons)

    replace('Michael and Martellus Bennett', 'Michael Bennett and Martellus Bennett', bill_simmons)
    replace('House', 'Joe House', bill_simmons)
    replace('The Sports Repodders', 'Jason Gay, Bryan Curtis', bill_simmons)

    replace('TV w', np.nan, bill_simmons)
    
    bill_simmons.replace('', np.nan, regex=True, inplace=True)
    
    bill_simmons = bill_simmons[pd.notnull(bill_simmons['guests'])]
    bill_simmons = splitDataFrameList(bill_simmons, 'guests', ', and ')
    bill_simmons = splitDataFrameList(bill_simmons, 'guests', ', ')
    bill_simmons = splitDataFrameList(bill_simmons, 'guests', ' & ')
    bill_simmons = splitDataFrameList(bill_simmons, 'guests', ' And ')
    bill_simmons = splitDataFrameList(bill_simmons, 'guests', ' and ')

    replace('TV w', np.nan, bill_simmons)
    bill_simmons = bill_simmons[pd.notnull(bill_simmons['guests'])]

    bill_simmons = bill_simmons[bill_simmons.guests.str.contains("Bill's Dad") == False]
    guest_split_last('Founder ', bill_simmons)
    guest_split_last('President ', bill_simmons)
    guest_split_last('Maven ', bill_simmons)
    guest_split_last('Mayor ', bill_simmons)


    bill_simmons['guests'] = [g.rstrip() for g in bill_simmons['guests']]

    return bill_simmons


def clean_legion_of_skanks(legion_of_skanks):

    legion_of_skanks = xml_to_df(legion_of_skanks)
        
    date_parser(legion_of_skanks)
    
    legion_of_skanks['guests'] = legion_of_skanks['title']
    
    guest_split_last(' - ', legion_of_skanks)
    
    legion_of_skanks = legion_of_skanks[pd.notnull(legion_of_skanks['guests'])]
    legion_of_skanks = splitDataFrameList(legion_of_skanks, 'guests', ', and ')
    legion_of_skanks = splitDataFrameList(legion_of_skanks, 'guests', ', ')
    legion_of_skanks = splitDataFrameList(legion_of_skanks, 'guests', ' & ')
    legion_of_skanks = splitDataFrameList(legion_of_skanks, 'guests', ' And ')
    legion_of_skanks = splitDataFrameList(legion_of_skanks, 'guests', ' and ')

    legion_of_skanks['guests'] = [g.rstrip() for g in legion_of_skanks['guests']]
    
    legion_of_skanks = legion_of_skanks[legion_of_skanks.guests.str.contains('Episode') == False]
    legion_of_skanks = legion_of_skanks[legion_of_skanks.guests.str.contains('The ') == False]

    return legion_of_skanks


def clean_punch_drunk_sports(punch_drunk_sports):

    punch_drunk_sports = xml_to_df(punch_drunk_sports)
        
    date_parser(punch_drunk_sports)
    
    punch_drunk_sports['guests'] = punch_drunk_sports.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(' from', punch_drunk_sports)
    guest_split(' on ', punch_drunk_sports)
    guest_split(' in ', punch_drunk_sports)
    
    punch_drunk_sports = punch_drunk_sports[pd.notnull(punch_drunk_sports['guests'])]
    punch_drunk_sports = splitDataFrameList(punch_drunk_sports, 'guests', ', and ')
    punch_drunk_sports = splitDataFrameList(punch_drunk_sports, 'guests', ', ')
    punch_drunk_sports = splitDataFrameList(punch_drunk_sports, 'guests', ' & ')
    punch_drunk_sports = splitDataFrameList(punch_drunk_sports, 'guests', ' And ')
    punch_drunk_sports = splitDataFrameList(punch_drunk_sports, 'guests', ' and ')

    replace('The Fight Nanny', 'Fight Nanny', punch_drunk_sports)
    replace('Danish', 'Jeff Danis', punch_drunk_sports)
    replace('O’Neill', 'Ryan O’Neill', punch_drunk_sports)
    replace("O'Neill", 'Ryan O’Neill', punch_drunk_sports)
    replace("O'Neil", 'Ryan O’Neill', punch_drunk_sports)

    punch_drunk_sports = punch_drunk_sports[punch_drunk_sports.guests.str.contains('Benefits') == False]
    punch_drunk_sports = punch_drunk_sports[punch_drunk_sports.guests.str.contains('Dorks') == False]
    punch_drunk_sports = punch_drunk_sports[punch_drunk_sports.guests.str.contains('the guys') == False]

    punch_drunk_sports['guests'] = [g.rstrip() for g in punch_drunk_sports['guests']]

    return punch_drunk_sports


def clean_hannibal(hannibal):

    hannibal = xml_to_df(hannibal)
        
    date_parser(hannibal)
    
    hannibal['guests'] = hannibal.title.str.extract(r'The ([\w\s\.\,\'\`\’\&\"\-]+) Episode',expand=True)

    replace('Lucas Brothers', 'Kenneth Lucas, Keith Lucas', hannibal)
    
    hannibal = hannibal[pd.notnull(hannibal['guests'])]
    hannibal = splitDataFrameList(hannibal, 'guests', ', and ')
    hannibal = splitDataFrameList(hannibal, 'guests', ', ')
    hannibal = splitDataFrameList(hannibal, 'guests', ' & ')
    hannibal = splitDataFrameList(hannibal, 'guests', ' And ')
    hannibal = splitDataFrameList(hannibal, 'guests', ' and ')

    hannibal = hannibal[hannibal.guests.str.contains('Advice') == False]
    replace('Serengeti', 'Dave Serengeti', hannibal)

    hannibal['guests'] = [g.rstrip() for g in hannibal['guests']]

    return hannibal


def clean_tait_fletcher(tait_fletcher):

    tait_fletcher = xml_to_df(tait_fletcher)
        
    date_parser(tait_fletcher)
    
    tait_fletcher['guests'] = tait_fletcher.title.str.extract(r'Episode \d+. ([\w\s\.\,\'\`\’\&\"\-\(\)]+)',expand=True)
    
    guest_split(' from', tait_fletcher)
    guest_split_last(r'With ', tait_fletcher)
    guest_split_last(r'with ', tait_fletcher)
    
    tait_fletcher = tait_fletcher[pd.notnull(tait_fletcher['guests'])]
    tait_fletcher = splitDataFrameList(tait_fletcher, 'guests', ', and ')
    tait_fletcher = splitDataFrameList(tait_fletcher, 'guests', ', & ')
    tait_fletcher = splitDataFrameList(tait_fletcher, 'guests', ', ')
    tait_fletcher = splitDataFrameList(tait_fletcher, 'guests', ' & ')
    tait_fletcher = splitDataFrameList(tait_fletcher, 'guests', ' And ')
    tait_fletcher = splitDataFrameList(tait_fletcher, 'guests', ' and ')

    replace("Donald 'Cowboy' Cerrone", 'Donald Cerrone', tait_fletcher)
    replace('Donald "Cowboy" Cerrone', 'Donald Cerrone', tait_fletcher)
    replace('Redban', 'Brian Redban', tait_fletcher)
    replace('Brian', np.nan, tait_fletcher)
    guest_split_last(r'Dr ', tait_fletcher)

    tait_fletcher = tait_fletcher[tait_fletcher.guests.str.contains(r' car ') == False]
    tait_fletcher = tait_fletcher[tait_fletcher.guests.str.contains(r'the Caveman ') == False]
    tait_fletcher = tait_fletcher[tait_fletcher.guests.str.contains(r'Fan Questions') == False]
    tait_fletcher = tait_fletcher[tait_fletcher.guests.str.contains(r'The China Chronicles') == False]
    tait_fletcher = tait_fletcher[tait_fletcher.guests.str.contains(r'Episode') == False]
    tait_fletcher = tait_fletcher[pd.notnull(tait_fletcher['guests'])]
    tait_fletcher['guests'] = [g.rstrip('.') for g in tait_fletcher['guests']]
    tait_fletcher['guests'] = [g.rstrip() for g in tait_fletcher['guests']]

    return tait_fletcher


def clean_steve_rannazzisi(steve_rannazzisi):

    steve_rannazzisi = xml_to_df(steve_rannazzisi)
        
    date_parser(steve_rannazzisi)
    
    steve_rannazzisi['guests'] = steve_rannazzisi.title.str.extract(r'\#\d+ - ([\w\s\.\,\'\`\’\&\"\-\(\)]+) - ',expand=True)
    
    guest_split_last(r'With ', steve_rannazzisi)
    guest_split_last(r'with ', steve_rannazzisi)
    
    steve_rannazzisi = steve_rannazzisi[pd.notnull(steve_rannazzisi['guests'])]
    steve_rannazzisi = splitDataFrameList(steve_rannazzisi, 'guests', ', and ')
    steve_rannazzisi = splitDataFrameList(steve_rannazzisi, 'guests', ', & ')
    steve_rannazzisi = splitDataFrameList(steve_rannazzisi, 'guests', ', ')
    steve_rannazzisi = splitDataFrameList(steve_rannazzisi, 'guests', ' & ')
    steve_rannazzisi = splitDataFrameList(steve_rannazzisi, 'guests', ' And ')
    steve_rannazzisi = splitDataFrameList(steve_rannazzisi, 'guests', ' and ')

    steve_rannazzisi['guests'] = [g.rstrip() for g in steve_rannazzisi['guests']]

    replace('My Teacher in High School Ms. Kerri Glynn', 'Kerri Glynn', steve_rannazzisi)

    steve_rannazzisi = steve_rannazzisi[steve_rannazzisi.guests.str.contains(r'My Family') == False]

    return steve_rannazzisi


def clean_jim_rome(jim_rome):

    jim_rome = xml_to_df(jim_rome)
        
    date_parser(jim_rome)
    
    jim_rome['guests'] = jim_rome.title.str.extract(r'\d+ - ([\w\s\.\,\'\`\’\&\"\-\(\)]+) - ',expand=True)
    
    jim_rome = jim_rome[pd.notnull(jim_rome['guests'])]
    jim_rome = splitDataFrameList(jim_rome, 'guests', ', and ')
    jim_rome = splitDataFrameList(jim_rome, 'guests', ', & ')
    jim_rome = splitDataFrameList(jim_rome, 'guests', ', ')
    jim_rome = splitDataFrameList(jim_rome, 'guests', ' & ')
    jim_rome = splitDataFrameList(jim_rome, 'guests', ' And ')
    jim_rome = splitDataFrameList(jim_rome, 'guests', ' and ')

    jim_rome['guests'] = [g.rstrip() for g in jim_rome['guests']]

    return jim_rome

def clean_sklar_brothers(sklar_brothers):

    sklar_brothers = xml_to_df(sklar_brothers)
        
    date_parser(sklar_brothers)
    
    sklar_brothers['guests'] = sklar_brothers.title.str.extract(r'(?:\d+ )?([\w\s\.\,\'\`\’\&\"\-\(\)\:]+)',expand=True)
    
    guest_split_last('with ', sklar_brothers)
    guest_split_last(' - ', sklar_brothers)
    guest_split_last('- ', sklar_brothers)
    guest_split_last(': ', sklar_brothers)
    
    sklar_brothers = sklar_brothers[pd.notnull(sklar_brothers['guests'])]
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ', and ')
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ', & ')
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ', ')
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ',')
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ' & ')
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ' And ')
    sklar_brothers = splitDataFrameList(sklar_brothers, 'guests', ' and ')

    sklar_brothers['guests'] = [g.rstrip() for g in sklar_brothers['guests']]

    sklar_brothers = sklar_brothers[sklar_brothers.guests.str.contains('The ') == False]
    sklar_brothers = sklar_brothers[sklar_brothers.guests.str.contains('Remote Control ') == False]
    sklar_brothers = sklar_brothers[sklar_brothers.guests.str.contains('Mixtape') == False]

    replace('Snowjob', 'Nick Thune', sklar_brothers)

    return sklar_brothers


def clean_all_things_comedy(all_things_comedy):

    all_things_comedy = xml_to_df(all_things_comedy)
        
    date_parser(all_things_comedy)
    
    all_things_comedy['guests'] = all_things_comedy.title.str.extract(r'(?:\#\d+ )?([\w\s\.\,\'\`\’\&\"\-\(\)\:]+)',expand=True)
    
    guest_split(' On', all_things_comedy)
    guest_split(' explains', all_things_comedy)

    
    all_things_comedy = all_things_comedy[pd.notnull(all_things_comedy['guests'])]
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ', and ')
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ', & ')
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ', ')
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ',')
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ' & ')
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ' And ')
    all_things_comedy = splitDataFrameList(all_things_comedy, 'guests', ' and ')

    all_things_comedy['guests'] = [g.rstrip() for g in all_things_comedy['guests']]
    
    return all_things_comedy


def clean_dom_irrera(dom_irrera):

    dom_irrera = xml_to_df(dom_irrera)
        
    date_parser(dom_irrera)
    
    dom_irrera['guests'] = dom_irrera['title']
    
    guest_split(' Returns', dom_irrera)
    guest_split(' Part', dom_irrera)

    dom_irrera = dom_irrera[pd.notnull(dom_irrera['guests'])]
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ', and ')
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ', & ')
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ', ')
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ',')
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ' & ')
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ' And ')
    dom_irrera = splitDataFrameList(dom_irrera, 'guests', ' and ')

    dom_irrera['guests'] = [g.rstrip() for g in dom_irrera['guests']]
    
    return dom_irrera


def clean_aubrey_marcus(aubrey_marcus):

    aubrey_marcus = xml_to_df(aubrey_marcus)
        
    date_parser(aubrey_marcus)
    
    aubrey_marcus['guests'] = aubrey_marcus.title.str.extract(r'(?:\#\d+ )?([\w\s\.\,\'\`\’\&\"\-\(\)\:\/]+)',expand=True)
    
    guest_split_last('with ', aubrey_marcus)
    guest_split_last('With ', aubrey_marcus)
    guest_split_last('w/ ', aubrey_marcus)
    guest_split_last(r'\#\d+\s', aubrey_marcus)
    guest_split_last('UFC Champ ', aubrey_marcus)
    
    guest_split(' Returns', aubrey_marcus)
    guest_split(' Part', aubrey_marcus)
    guest_split(' of', aubrey_marcus)
    guest_split(': ', aubrey_marcus)
    
    replace('MAPS Org Rick Doblin', 'Rick Doblin', aubrey_marcus)
    replace('Dr. Chris Ryan', 'Christopher Ryan', aubrey_marcus)
    replace('Spoken Through Paul Selig', 'Paul Selig', aubrey_marcus)
    replace('Matt and Jared Vengrin', 'Matt Vengrin and Jared Vengrin', aubrey_marcus)
    replace('Dr. Dan Engle MD', 'Dr. Dan Engle', aubrey_marcus)
    replace('Whitney Miller (Miss Texas)', 'Whitney Miller', aubrey_marcus)
    replace('Donald "Cowboy" Cerrone', 'Donald Cerrone', aubrey_marcus)
    replace('Stephen "Twitch" Boss', 'Stephen Boss', aubrey_marcus)
    replace('Stephen "tWitch" Boss', 'Stephen Boss', aubrey_marcus)

    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('Trials and Triumphs') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains(' You ') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains(' from ') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('Experiencing') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('Inspiration') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('Team') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('No More') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains(' to ') == False]

    aubrey_marcus = aubrey_marcus[pd.notnull(aubrey_marcus['guests'])]
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ', and ')
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ', & ')
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ', ')
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ',')
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ' & ')
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ' And ')
    aubrey_marcus = splitDataFrameList(aubrey_marcus, 'guests', ' and ')
    
    replace('Spoken Through Paul Selig', 'Paul Selig', aubrey_marcus)

    aubrey_marcus['guests'] = [g.rstrip() for g in aubrey_marcus['guests']]

    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('The ') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('Is ') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('SPECIAL') == False]
    aubrey_marcus = aubrey_marcus[aubrey_marcus.guests.str.contains('- ') == False]
    
    return aubrey_marcus


def clean_happy_sad_confused(happy_sad_confused):

    happy_sad_confused = xml_to_df(happy_sad_confused)
        
    date_parser(happy_sad_confused)
    
    happy_sad_confused['guests'] = happy_sad_confused['title']
    
    guest_split(', Vol.', happy_sad_confused)
    guest_split(' Vol.', happy_sad_confused)
    guest_split(' Part', happy_sad_confused)
    
    guest_split_last('HSC SHORT: ', happy_sad_confused)
    guest_split_last('plus ', happy_sad_confused)
    
    replace('Joe & Anthony Russo', 'Joe Russo & Anthony Russo', happy_sad_confused)
    replace('War of the Planet of the Apes and Bruce Campbell', 'Andy Serkis, Matt Reeves, and Dylan Clark and Bruce Campbell', happy_sad_confused)
    replace('The Lonely Island (Andy Samberg, Akiva Schaffer, Jorma Taccone)', 'Andy Samberg, Akiva Schaffer, Jorma Taccone', happy_sad_confused)

    happy_sad_confused = happy_sad_confused[happy_sad_confused.guests.str.contains('Happy ') == False]

    happy_sad_confused = happy_sad_confused[pd.notnull(happy_sad_confused['guests'])]

    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', '; Plus, ')

    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ', and ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ', And ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ', & ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ', ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ',')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ' & ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ' And ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ' and ')
    happy_sad_confused = splitDataFrameList(happy_sad_confused, 'guests', ' / ')

    happy_sad_confused['guests'] = [g.rstrip() for g in happy_sad_confused['guests']]
    
    return happy_sad_confused


def clean_sam_jones(sam_jones):

    sam_jones = xml_to_df(sam_jones)
        
    date_parser(sam_jones)

    sam_jones['guests'] = sam_jones.title.str.extract(r'(?:\d+. )([\w\s\.\,\'\`\’\&\"\-\(\)\:\/]+)',expand=True)

    sam_jones = sam_jones[pd.notnull(sam_jones['guests'])]

    sam_jones['guests'] = [g.rstrip() for g in sam_jones['guests']]

    replace('Robert Downey Jr', 'Robert Downey Jr.', sam_jones)
    replace('Michael B Jordan', 'Michael B. Jordan', sam_jones)
    
    return sam_jones


def clean_maltin(maltin):

    maltin = xml_to_df(maltin)
        
    date_parser(maltin)

    maltin['guests'] = maltin.title.str.extract(r'(?:\d+ )?([\w\s\.\,\'\`\’\&\"\-\:\/]+)',expand=True)
    
    guest_split(' Pt.', maltin)
    guest_split(' of ', maltin)
    guest_split(' Encore', maltin)
    guest_split_last('w/ ', maltin)
    guest_split_last('with ', maltin)
    guest_split_last(': ', maltin)
    guest_split_last("Special's ", maltin)
    guest_split_last('guest ', maltin)
    guest_split_last('Hero ', maltin)
    guest_split_last('Meet ', maltin)

    maltin = maltin[maltin.guests.str.contains('Stories') == False]
    maltin = maltin[maltin.guests.str.contains(' for ') == False]
    maltin = maltin[maltin.guests.str.contains('Breakthrough') == False]
    maltin = maltin[maltin.guests.str.contains('Stars ') == False]
    maltin = maltin[maltin.guests.str.contains(' The ') == False]
    maltin = maltin[maltin.guests.str.contains('Oscar Nominees') == False]
    maltin = maltin[maltin.guests.str.contains('Oscars') == False]
    maltin = maltin[maltin.guests.str.contains('Film Festival') == False]
    maltin = maltin[maltin.guests.str.contains('Holiday Movies') == False]
    maltin = maltin[maltin.guests.str.contains('Black History Films') == False]
    maltin = maltin[maltin.guests.str.contains('Sequels') == False]
    maltin = maltin[maltin.guests.str.contains('Nominated') == False]
    maltin = maltin[maltin.guests.str.contains('Movie Walkouts') == False]
    maltin = maltin[maltin.guests.str.contains('Stranger Than Fiction') == False]

    replace('The Nelms Brothers', 'Ian Nelms and Eshom Nelms', maltin)
    replace('Chaplin and Keaton', np.nan, maltin)
    replace('Ed Begley, Jr.', 'Ed Begley Jr.', maltin)


    maltin = maltin[pd.notnull(maltin['guests'])]
    maltin = splitDataFrameList(maltin, 'guests', ', and ')
    maltin = splitDataFrameList(maltin, 'guests', ', & ')
    maltin = splitDataFrameList(maltin, 'guests', ', ')
    maltin = splitDataFrameList(maltin, 'guests', ',')
    maltin = splitDataFrameList(maltin, 'guests', ' & ')
    maltin = splitDataFrameList(maltin, 'guests', ' And ')
    maltin = splitDataFrameList(maltin, 'guests', ' and ')

    maltin = maltin[maltin.guests.str.contains('Senior Editor') == False]
    maltin = maltin[maltin.guests.str.contains('Movie') == False]
    maltin = maltin[maltin.guests.str.contains('Films') == False]
    maltin = maltin[maltin.guests.str.contains('Page To Screen') == False]
    maltin = maltin[maltin.guests.str.contains('Behind the Scenes') == False]
    maltin = maltin[maltin.guests.str.contains('Business') == False]
    maltin = maltin[maltin.guests.str.contains('From ') == False]
    maltin = maltin[maltin.guests.str.contains('Simpsons writer') == False]
    maltin = maltin[maltin.guests.str.contains('comedian') == False]
    maltin = maltin[maltin.guests.str.contains(' to ') == False]
    maltin = maltin[maltin.guests.str.contains('Biopics') == False]
    maltin = maltin[maltin.guests.str.contains(' from ') == False]
    maltin = maltin[maltin.guests.str.contains('Tales') == False]
    maltin = maltin[maltin.guests.str.contains('The ') == False]
    maltin = maltin[maltin.guests.str.contains('director') == False]
    maltin = maltin[maltin.guests.str.contains('Funny') == False]
    maltin = maltin[maltin.guests.str.contains('Ladies') == False]
    maltin = maltin[maltin.guests.str.contains('Animated') == False]
    maltin = maltin[maltin.guests.str.contains(' the ') == False]

    replace('Jessie', np.nan, maltin)
    maltin = maltin[pd.notnull(maltin['guests'])]

    maltin['guests'] = [g.rstrip(r')') for g in maltin['guests']]
    maltin['guests'] = [g.rstrip() for g in maltin['guests']]

    
    return maltin


def clean_guy_raz(guy_raz):

    guy_raz = xml_to_df(guy_raz)
        
    date_parser(guy_raz)
    
    guy_raz['guests'] = guy_raz.title.str.extract(r'\: ([\w\s\.\,\'\`\’\&\"\-\(\)\:]+)',expand=True)
    
    replace('Kate & Andy Spade', 'Kate Spade & Andy Spade', guy_raz)
    replace('Melissa And Doug Bernstein', 'Melissa Bernstein And Doug Bernstein', guy_raz)
    replace('Maureen & Tony Wheeler', 'Maureen Wheeler & Tony Wheeler', guy_raz)
    
    guy_raz = guy_raz[pd.notnull(guy_raz['guests'])]
    guy_raz = splitDataFrameList(guy_raz, 'guests', ', and ')
    guy_raz = splitDataFrameList(guy_raz, 'guests', ', & ')
    guy_raz = splitDataFrameList(guy_raz, 'guests', ', ')
    guy_raz = splitDataFrameList(guy_raz, 'guests', ',')
    guy_raz = splitDataFrameList(guy_raz, 'guests', ' & ')
    guy_raz = splitDataFrameList(guy_raz, 'guests', ' And ')
    guy_raz = splitDataFrameList(guy_raz, 'guests', ' and ')

    guy_raz['guests'] = [g.rstrip() for g in guy_raz['guests']]

    guy_raz = guy_raz[guy_raz.guests.str.contains('How I Built This') == False]
    
    return guy_raz


def clean_modern_love(modern_love):

    modern_love = xml_to_df(modern_love)
        
    date_parser(modern_love)
    
    modern_love['guests'] = modern_love.title.str.extract(r'\| With ([\w\s\.\,\'\`\’\&\"\-\(\)\:]+)',expand=True)
    
    modern_love = modern_love[pd.notnull(modern_love['guests'])]
    modern_love = splitDataFrameList(modern_love, 'guests', ', and ')
    modern_love = splitDataFrameList(modern_love, 'guests', ', & ')
    modern_love = splitDataFrameList(modern_love, 'guests', ', ')
    modern_love = splitDataFrameList(modern_love, 'guests', ',')
    modern_love = splitDataFrameList(modern_love, 'guests', ' & ')
    modern_love = splitDataFrameList(modern_love, 'guests', ' And ')
    modern_love = splitDataFrameList(modern_love, 'guests', ' and ')

    modern_love['guests'] = [g.rstrip() for g in modern_love['guests']]

    replace('Emily Gordon', 'Emily V. Gordon', modern_love)
    
    return modern_love


def clean_lewis_howes(lewis_howes):

    lewis_howes = xml_to_df(lewis_howes)
        
    date_parser(lewis_howes)
    
    lewis_howes['guests'] = lewis_howes.title.str.extract(r'EP \d+ ([\w\s\.\,\'\`\’\&\"\-\(\)\:]+)',expand=True)
    
    guest_split(': ', lewis_howes)
    
    guest_split_last('with ', lewis_howes)
    guest_split_last('Founder ', lewis_howes)
    guest_split_last('Negotiator ', lewis_howes)
    guest_split_last('Champion ', lewis_howes)
    guest_split_last('Master ', lewis_howes)
    guest_split_last('Nutritionist ', lewis_howes)
    guest_split_last('Surfer ', lewis_howes)
    guest_split_last('Model ', lewis_howes)
    guest_split_last('Professor ', lewis_howes)
    guest_split_last('Star ', lewis_howes)
    
    guest_split(' on', lewis_howes)

    replace('Chris and Heidi Powell', 'Chris Powell and Heidi Powell', lewis_howes)
    replace('Rockstars, Fame, and Celebrities', 'Shep Gordon', lewis_howes)
    
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'My Success Habits, Rituals and Morning Routine') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'How I Use Faith, Mindset, and Positivity to Thrive') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'How to Connect with Influencers, Thought Leaders and Decision Makers') == False]

    lewis_howes = lewis_howes[pd.notnull(lewis_howes['guests'])]
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ', and ')
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ', & ')
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ', ')
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ',')
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ' & ')
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ' And ')
    lewis_howes = splitDataFrameList(lewis_howes, 'guests', ' and ')

    lewis_howes['guests'] = [g.rstrip() for g in lewis_howes['guests']]

    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'\(') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'\d') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' is ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' to ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' the ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' Up$') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' of ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Thought ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Mindset') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' Is ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' In ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' Are ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' Me') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' a ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r' v. ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Coffee Conversations') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Going ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Living With Less') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Without') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Influencers') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Your ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'The ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'What ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Why ') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Celebrate Full Circle') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'No More') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Love') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Wealth') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Success') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Look') == False]
    lewis_howes = lewis_howes[lewis_howes.guests.str.contains(r'Yourself') == False]

    lewis_howes = lewis_howes[lewis_howes['duration'] > 600]

    return lewis_howes


def clean_ringer_nba(ringer_nba):

    ringer_nba = xml_to_df_desc(ringer_nba)
        
    date_parser(ringer_nba)
    
    ringer_nba['guests'] = ringer_nba.description.str.extract(r'(?:joined by |grabs )([\w\s\.\,\'\`\’\&\"\-\(\)\:]+) to ',expand=True)
    
    guest_split(' to ', ringer_nba)
    guest_split(' on ', ringer_nba)
    guest_split(' of ', ringer_nba)
    guest_split(' (', ringer_nba)
    guest_split(' after a ', ringer_nba)
    guest_split_last('coach ', ringer_nba)
    guest_split_last('writer ', ringer_nba)
    guest_split_last("Today's ", ringer_nba)
    guest_split_last("Post's ", ringer_nba)
    guest_split_last("Vertical's ", ringer_nba)
    guest_split_last("Ringer's ", ringer_nba)
    guest_split_last("Ringer’s ", ringer_nba)
    guest_split_last("confidant ", ringer_nba)
    guest_split_last("superfan ", ringer_nba)
    guest_split_last("champion ", ringer_nba)
    guest_split_last("ESPNer ", ringer_nba)
    guest_split_last("TV’s ", ringer_nba)
    guest_split_last("manager ", ringer_nba)
    guest_split_last("frontman ", ringer_nba)
    guest_split_last("Nuggets' ", ringer_nba)
    guest_split_last("analyst ", ringer_nba)
    guest_split_last("guard ", ringer_nba)
    
    ringer_nba['guests2'] = ringer_nba.title.str.extract(r'(?:With )([\w\s\.\,\'\`\’\&\"\-\:]+)',expand=True)
    
    ringer_nba.replace(np.nan, ' and ', regex=True, inplace=True)
    ringer_nba['guests'] = ringer_nba['guests'] + ' and ' + ringer_nba['guests2']
    ringer_nba = ringer_nba.drop('guests2', 1)  
    ringer_nba = ringer_nba.drop('description', 1)
    ringer_nba.replace('', np.nan, regex=True, inplace=True)
    
    ringer_nba = ringer_nba[pd.notnull(ringer_nba['guests'])]
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ', and ')
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ', & ')
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ', ')
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ',')
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ' & ')
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ' And ')
    ringer_nba = splitDataFrameList(ringer_nba, 'guests', ' and ')

    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r'potential') == False]

    replace(' and', '', ringer_nba)
    replace('and ', '', ringer_nba)
    replace('the godfather of grassroots basketball', 'Sonny Vaccaro', ringer_nba)
    replace("The Vertical's Adrian Wojnarowski", 'Adrian Wojnarowski', ringer_nba)
    replace("Haley O’Shaughnessy", "Haley O'Shaughnessy", ringer_nba)

    guest_split(r' (', ringer_nba)

    ringer_nba['guests'] = [g.rstrip() for g in ringer_nba['guests']]
    ringer_nba.replace('', np.nan, regex=True, inplace=True)
    ringer_nba = ringer_nba[pd.notnull(ringer_nba['guests'])]

    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"Kevin O'Connor") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"HBO") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"the head coach") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"Hillsong pastor") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"Part ") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"former ") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"current ") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"One-and-Dones") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"hid dad") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"Bill’s Dad") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"the Magic") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"forward") == False]
    ringer_nba = ringer_nba[ringer_nba.guests.str.contains(r"Rookie") == False]


    ringer_nba.drop_duplicates(inplace=True)
    
    return ringer_nba


def clean_mike_lupica(mike_lupica):

    mike_lupica = xml_to_df(mike_lupica)
    
    mike_lupica = mike_lupica[mike_lupica.title.str.contains('In The Loop') == False]
        
    date_parser(mike_lupica)
    
    mike_lupica['guests'] = mike_lupica.title.str.extract(r'Episode \d+ -([\w\s\.\,\'\`\’\&\"\-\(\)\:]+)',expand=True)

    mike_lupica = mike_lupica[pd.notnull(mike_lupica['guests'])]
    mike_lupica = splitDataFrameList(mike_lupica, 'guests', ' & ')

    mike_lupica = mike_lupica[mike_lupica.guests.str.contains('Year ') == False]
    
    mike_lupica = mike_lupica[pd.notnull(mike_lupica['guests'])]

    mike_lupica['guests'] = [g.rstrip() for g in mike_lupica['guests']]
    
    return mike_lupica


def clean_ask_me_another(ask_me_another):

    ask_me_another = xml_to_df(ask_me_another)
        
    date_parser(ask_me_another)
    
    ask_me_another['guests'] = ask_me_another.title.str.extract(r'([^:]+): ',expand=True)
    
    replace('Mark and Jay Duplass', 'Mark Duplass and Jay Duplass', ask_me_another)
    replace('C2E2', 'Rose McGowan', ask_me_another)
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('AMA ') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('The ') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains(' to ') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('Sketchfest') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('Wet Hot American Summer') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('Welcome To Night Vale') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('VIDEO') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('Road Tripping') == False]
    ask_me_another = ask_me_another[ask_me_another.guests.str.contains('Foodie') == False]


    ask_me_another = ask_me_another[pd.notnull(ask_me_another['guests'])]
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ', and ')
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ', & ')
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ', ')
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ',')
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ' & ')
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ' And ')
    ask_me_another = splitDataFrameList(ask_me_another, 'guests', ' and ')

    ask_me_another['guests'] = [g.rstrip() for g in ask_me_another['guests']]
    
    return ask_me_another


def clean_dear_sugars(dear_sugars):

    dear_sugars = xml_to_df(dear_sugars)
        
    date_parser(dear_sugars)
    
    dear_sugars['guests'] = dear_sugars.title.str.extract(r'With ([^:]+)',expand=True)
    
    dear_sugars = dear_sugars[dear_sugars.guests.str.contains('Our ') == False]
    dear_sugars = dear_sugars[dear_sugars.guests.str.contains('Benefits,') == False]
    dear_sugars = dear_sugars[dear_sugars.guests.str.contains('Younger Men') == False]
    dear_sugars = dear_sugars[dear_sugars.guests.str.contains('His Boyfriend') == False]
    dear_sugars = dear_sugars[dear_sugars.guests.str.contains('A Hermit Crab') == False]

    dear_sugars = dear_sugars[pd.notnull(dear_sugars['guests'])]

    dear_sugars['guests'] = [g.rstrip() for g in dear_sugars['guests']]
    
    return dear_sugars


def clean_bugle(bugle):

    bugle = xml_to_df_desc(bugle)
        
    date_parser(bugle)
    
    bugle['guests'] = bugle.description.str.extract(r'(?:joined by |with )([\w\s\.\,\'\`\’\&\"\-]+)(?: for | to )',expand=True)
    bugle['guests1'] = bugle.description.str.extract(r'(Andy and John|Andy and Anuvab|Andy and Nish|Andy and Hari|Andy and Helen|Andy and Alice)',expand=True)
    
    guest_split(' to', bugle)
        
    bugle.replace(np.nan, '', regex=True, inplace=True)
    bugle['guests'] = bugle['guests'] + bugle['guests1']
    bugle = bugle.drop('guests1', 1)  
    bugle = bugle.drop('description', 1)
    bugle.replace('', np.nan, regex=True, inplace=True)
    
    replace('Andy and John', 'John Oliver', bugle)
    replace('Andy and Anuvab', 'Anuvab Pal', bugle)
    replace('Andy and Nish', 'Nish Kumar', bugle)
    replace('Andy and Hari', 'Hari Kondabolu', bugle)
    replace('Andy and Helen', 'Helen Zaltman', bugle)
    replace('Andy and Alice', 'Alice Fraser', bugle)
    replace('Helen and Nish', 'Helen Zaltman and Nish Kumar', bugle)
    replace('Nish and Alice', 'Nish Kumar and Alice Fraser', bugle)
    replace('Helen, Nish and Producer Chris', 'Helen Zaltman and Nish Kumar and Producer Chris', bugle)
    
    bugle = bugle[bugle.guests.str.contains('Obamacare') == False]

    bugle = bugle[pd.notnull(bugle['guests'])]

    bugle = splitDataFrameList(bugle, 'guests', ', and ')
    bugle = splitDataFrameList(bugle, 'guests', ', & ')
    bugle = splitDataFrameList(bugle, 'guests', ', ')
    bugle = splitDataFrameList(bugle, 'guests', ',')
    bugle = splitDataFrameList(bugle, 'guests', ' & ')
    bugle = splitDataFrameList(bugle, 'guests', ' And ')
    bugle = splitDataFrameList(bugle, 'guests', ' and ')

    guest_split_last('Bugle debutant ', bugle)

    bugle['guests'] = [g.rstrip() for g in bugle['guests']]
    
    return bugle


def clean_daily_zeitgeist(daily_zeitgeist):

    daily_zeitgeist = xml_to_df_desc(daily_zeitgeist)
        
    date_parser(daily_zeitgeist)
    
    daily_zeitgeist['guests'] = daily_zeitgeist.description.str.extract(r'joined by ([^:]+) to discuss',expand=True)
    
    guest_split_last('comedian ', daily_zeitgeist)
    guest_split_last('writer ', daily_zeitgeist)
    guest_split_last('guest ', daily_zeitgeist)
    guest_split_last('creator ', daily_zeitgeist)
    guest_split_last('performer ', daily_zeitgeist)
    guest_split_last('& comic artist ', daily_zeitgeist)
    guest_split_last('our favorite ', daily_zeitgeist)
    guest_split_last('writers ', daily_zeitgeist)
    guest_split_last('guests ', daily_zeitgeist)
    guest_split_last("Is This Racist's'", daily_zeitgeist)
    guest_split_last("Stuff You Should Know's", daily_zeitgeist)
    
    guest_split(' to', daily_zeitgeist)
    
    daily_zeitgeist = daily_zeitgeist.drop('description', 1)

    daily_zeitgeist = daily_zeitgeist[pd.notnull(daily_zeitgeist['guests'])]
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ', and ')
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ', & ')
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ', ')
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ',')
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ' & ')
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ' And ')
    daily_zeitgeist = splitDataFrameList(daily_zeitgeist, 'guests', ' and ')

    daily_zeitgeist['guests'] = [g.rstrip() for g in daily_zeitgeist['guests']]
    
    return daily_zeitgeist


def clean_smodcast(smodcast):

    smodcast = xml_to_df_summ(smodcast)
        
    date_parser(smodcast)
    
    smodcast['guests'] = smodcast.summary.str.extract(r'[Gg]uest (?:[Ss]tar:? |[Ss]tarring |stars)?([^:]+).',expand=True)
    
    guest_split_last('podcaster ', smodcast)
    guest_split_last('hostess ', smodcast)
    guest_split_last('director ', smodcast)
    guest_split_last('Host ', smodcast)
    guest_split_last('Hoaxter ', smodcast)
    
    guest_split(' celebrates', smodcast)
    guest_split('. ', smodcast)
    guest_split('.\n', smodcast)
    guest_split(' talks', smodcast)
    guest_split(' calls', smodcast)
    
    replace('stars', np.nan, smodcast)
    
    smodcast = smodcast.drop('summary', 1)

    smodcast = smodcast[pd.notnull(smodcast['guests'])]
    smodcast = splitDataFrameList(smodcast, 'guests', ', and ')
    smodcast = splitDataFrameList(smodcast, 'guests', ', & ')
    smodcast = splitDataFrameList(smodcast, 'guests', ', ')
    smodcast = splitDataFrameList(smodcast, 'guests', ',')
    smodcast = splitDataFrameList(smodcast, 'guests', ' & ')
    smodcast = splitDataFrameList(smodcast, 'guests', ' And ')
    smodcast = splitDataFrameList(smodcast, 'guests', ' and ')

    smodcast['guests'] = [g.rstrip() for g in smodcast['guests']]
    
    return smodcast


def clean_rapaport(rapaport):

    rapaport = xml_to_df(rapaport)
        
    date_parser(rapaport)
    
    rapaport['guests'] = rapaport.title.str.extract(r'EP \d+ - ([^\(]+)',expand=True)
    
    rapaport = rapaport[rapaport.guests.str.contains(r'[A-Z]{2}') == False]
    rapaport = rapaport[rapaport.guests.str.contains(r'\@B') == False]
    
    guest_split(': ', rapaport)
    
    rapaport['guests'] = [g.rstrip() for g in rapaport['guests']]
    
    replace('Joey Coco Diaz', 'Joey Diaz', rapaport)
    
    return rapaport


def clean_jimmy_pardo(jimmy_pardo):

    jimmy_pardo = xml_to_df(jimmy_pardo)
        
    date_parser(jimmy_pardo)
    
    jimmy_pardo['guests'] = jimmy_pardo.title.str.extract(r' - ([^\(]+)',expand=True)

    replace('The Sklar Brothers', 'Jason Sklar, Randy Sklar', jimmy_pardo)

    guest_split(' of ', jimmy_pardo)

    jimmy_pardo = jimmy_pardo[jimmy_pardo.guests.str.contains('The ') == False]
    
    jimmy_pardo = jimmy_pardo[pd.notnull(jimmy_pardo['guests'])]
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ', and ')
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ', & ')
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ', ')
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ',')
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ' & ')
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ' And ')
    jimmy_pardo = splitDataFrameList(jimmy_pardo, 'guests', ' and ')

    jimmy_pardo['guests'] = [g.rstrip() for g in jimmy_pardo['guests']]
    
    return jimmy_pardo



def clean_crabfeast(crabfeast):

    crabfeast = xml_to_df(crabfeast)
        
    date_parser(crabfeast)
    
    crabfeast['guests'] = crabfeast.title.str.extract(r'The CrabFeast \d+: ([^:]+)$',expand=True)

    crabfeast = crabfeast[crabfeast.guests.str.contains('Ryan & Jay') == False]
    crabfeast = crabfeast[crabfeast.guests.str.contains('Jay & Ryan') == False]
    
    guest_split(' Pt.', crabfeast)
    guest_split(' Live', crabfeast)
    guest_split(' LIVE', crabfeast)


    crabfeast = crabfeast[pd.notnull(crabfeast['guests'])]
    crabfeast = splitDataFrameList(crabfeast, 'guests', ', and ')
    crabfeast = splitDataFrameList(crabfeast, 'guests', ', & ')
    crabfeast = splitDataFrameList(crabfeast, 'guests', ', ')
    crabfeast = splitDataFrameList(crabfeast, 'guests', ',')
    crabfeast = splitDataFrameList(crabfeast, 'guests', ' & ')
    crabfeast = splitDataFrameList(crabfeast, 'guests', ' And ')
    crabfeast = splitDataFrameList(crabfeast, 'guests', ' and ')

    crabfeast['guests'] = [g.rstrip() for g in crabfeast['guests']]

    replace('TJ Miller', 'T.J. Miller', crabfeast)
    replace('"Big" Jay Oakerson', 'Big Jay Oakerson', crabfeast)
    replace('Roy Wood Jr', 'Roy Wood Jr.', crabfeast)
    replace('Emily Gordon', 'Emily V. Gordon', crabfeast)

    crabfeast = crabfeast[crabfeast.guests.str.contains('The ') == False]
    
    return crabfeast


def clean_matt_besser(matt_besser):

    matt_besser = xml_to_df(matt_besser)
        
    date_parser(matt_besser)
    
    matt_besser['guests'] = matt_besser.title.str.extract(r'\d+ ([^:]+)$',expand=True)
    
    matt_besser = matt_besser[matt_besser.guests.str.contains('The Best of') == False]

    matt_besser = matt_besser[pd.notnull(matt_besser['guests'])]
    matt_besser = splitDataFrameList(matt_besser, 'guests', ', and ')
    matt_besser = splitDataFrameList(matt_besser, 'guests', ', & ')
    matt_besser = splitDataFrameList(matt_besser, 'guests', ', ')
    matt_besser = splitDataFrameList(matt_besser, 'guests', ',')
    matt_besser = splitDataFrameList(matt_besser, 'guests', ' & ')
    matt_besser = splitDataFrameList(matt_besser, 'guests', ' And ')
    matt_besser = splitDataFrameList(matt_besser, 'guests', ' and ')

    matt_besser['guests'] = [g.rstrip() for g in matt_besser['guests']]
    
    return matt_besser


def clean_gilbert_gottfried(gilbert_gottfried):

    gilbert_gottfried = xml_to_df(gilbert_gottfried)
        
    date_parser(gilbert_gottfried)
    
    gilbert_gottfried['guests'] = gilbert_gottfried.title.str.extract(r'\#\d+ ([^:]+)$',expand=True)
    
    gilbert_gottfried = gilbert_gottfried[gilbert_gottfried.guests.str.contains('Bonus') == False]
    gilbert_gottfried = gilbert_gottfried[gilbert_gottfried.guests.str.contains('In ') == False]
    
    guest_split(' aka', gilbert_gottfried)
    guest_split(' Returns', gilbert_gottfried)

    gilbert_gottfried = gilbert_gottfried[pd.notnull(gilbert_gottfried['guests'])]
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ', and ')
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ', & ')
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ', ')
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ',')
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ' & ')
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ' And ')
    gilbert_gottfried = splitDataFrameList(gilbert_gottfried, 'guests', ' and ')

    gilbert_gottfried['guests'] = [g.rstrip() for g in gilbert_gottfried['guests']]
    
    return gilbert_gottfried


def clean_jordan_jesse_go(jordan_jesse_go):

    jordan_jesse_go = xml_to_df(jordan_jesse_go)
        
    date_parser(jordan_jesse_go)
    
    jordan_jesse_go['guests'] = jordan_jesse_go.title.str.extract(r'with ([^:]+)$',expand=True)

    guest_split(r' (', jordan_jesse_go)

    guest_split_last("Ninja's ", jordan_jesse_go)
    guest_split_last("with ", jordan_jesse_go)
    guest_split_last("Superego's ", jordan_jesse_go)

    replace('the Doughboys', 'Nick Wiger, Mike Mitchell', jordan_jesse_go)
    replace('Jason and Randy Sklar', 'Jason Sklar and Randy Sklar', jordan_jesse_go)
    replace('Jason and Randy', np.nan, jordan_jesse_go)
    replace('The Sklar Brothers', 'Jason Sklar and Randy Sklar', jordan_jesse_go)

    jordan_jesse_go = jordan_jesse_go[pd.notnull(jordan_jesse_go['guests'])]
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ', and ')
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ', & ')
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ', ')
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ',')
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ' & ')
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ' And ')
    jordan_jesse_go = splitDataFrameList(jordan_jesse_go, 'guests', ' and ')


    jordan_jesse_go['guests'] = [g.rstrip('!') for g in jordan_jesse_go['guests']]
    jordan_jesse_go['guests'] = [g.rstrip() for g in jordan_jesse_go['guests']]
    
    return jordan_jesse_go


def clean_jesse_thorn(jesse_thorn):

    jesse_thorn = xml_to_df(jesse_thorn)
        
    date_parser(jesse_thorn)
    
    jesse_thorn['guests'] = jesse_thorn['title']

    guest_split_last(' with ', jesse_thorn)
    guest_split_last("Eerie's ", jesse_thorn)
    guest_split_last("Pixar's ", jesse_thorn)
    guest_split_last("Throne's ", jesse_thorn)
    guest_split_last("Breeder's ", jesse_thorn)
    guest_split_last(": ", jesse_thorn)

    guest_split(' on', jesse_thorn)

    replace("Bullseye's Judge John Hodgman Special", 'John Hodgman', jesse_thorn)
    replace("The Breeders' Kim Deal", 'Kim Deal', jesse_thorn)
    replace('My Brother, My Brother and Me & Gina Prince-Bythewood', 'Justin McElroy, Travis McElroy and Griffin McElroy and Gina Prince-Bythewood', jesse_thorn)
    replace("Throwing Shade", 'Erin Gibson and Bryan Safi', jesse_thorn)
    replace('David Wain & Belle and Sebastian', 'David Wain & Stuart Murdoch', jesse_thorn)
    replace('Carl Reiner & Kate and Laura Mulleavy', 'Carl Reiner & Kate Mulleavy and Laura Mulleavy', jesse_thorn)
    replace('Vince Staples & The Trailer Park Boys', 'Vince Staples & John Paul Tremblay, Robb Well and Mike Smith', jesse_thorn)

    jesse_thorn = jesse_thorn[pd.notnull(jesse_thorn['guests'])]
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ', and ')
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ', & ')
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ', ')
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ',')
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ' & ')
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ' And ')
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ' and ')

    replace('Another Period', 'Natasha Leggero and Riki Lindhome', jesse_thorn)
    replace('The Egyptian Lover', 'Greg Broussard', jesse_thorn)
    replace('Me', np.nan, jesse_thorn)
    replace('High Maintenance', 'Katja Blichfeld and Ben Sinclair', jesse_thorn)
    replace('Fresh Off the Boat', 'Randall Park and Nahnatchka Khan', jesse_thorn)
    jesse_thorn = jesse_thorn[pd.notnull(jesse_thorn['guests'])]
    jesse_thorn = splitDataFrameList(jesse_thorn, 'guests', ' and ')

    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('at a Time') == False]
    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('special') == False]
    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('Special') == False]
    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('more!') == False]
    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('The Bullseye') == False]
    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('"Corporate"') == False]
    jesse_thorn = jesse_thorn[jesse_thorn.guests.str.contains('Happy Hour') == False]


    jesse_thorn['guests'] = [g.rstrip() for g in jesse_thorn['guests']]
    
    return jesse_thorn


def clean_stop_podcasting_yourself(stop_podcasting_yourself):

    stop_podcasting_yourself = xml_to_df(stop_podcasting_yourself)
        
    date_parser(stop_podcasting_yourself)
    
    stop_podcasting_yourself['guests'] = stop_podcasting_yourself.title.str.extract(r'Episode \d+ - ([^:]+)$',expand=True)

    guest_split_last('with ', stop_podcasting_yourself)
    
    stop_podcasting_yourself = stop_podcasting_yourself[pd.notnull(stop_podcasting_yourself['guests'])]
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ', and ')
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ', & ')
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ', ')
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ',')
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ' & ')
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ' And ')
    stop_podcasting_yourself = splitDataFrameList(stop_podcasting_yourself, 'guests', ' and ')

    stop_podcasting_yourself = stop_podcasting_yourself[stop_podcasting_yourself.guests.str.contains('EVERY') == False]
    stop_podcasting_yourself = stop_podcasting_yourself[stop_podcasting_yourself.guests.str.contains('Countdown') == False]

    replace('Pete', 'Pete Johansson', stop_podcasting_yourself)

    stop_podcasting_yourself['guests'] = [g.rstrip() for g in stop_podcasting_yourself['guests']]
    
    return stop_podcasting_yourself


def clean_spontaneanation(spontaneanation):

    spontaneanation = xml_to_df(spontaneanation)
        
    date_parser(spontaneanation)
    
    spontaneanation['guests'] = spontaneanation.title.str.extract(r'\(w/ ([^\)]+)',expand=True)
    
    guest_split_last(': ', spontaneanation)
    
    spontaneanation = spontaneanation[pd.notnull(spontaneanation['guests'])]
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ', and ')
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ', & ')
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ', ')
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ',')
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ' & ')
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ' And ')
    spontaneanation = splitDataFrameList(spontaneanation, 'guests', ' and ')

    replace('Little Janet Varney', 'Janet Varney', spontaneanation)

    spontaneanation['guests'] = [g.rstrip() for g in spontaneanation['guests']]
    
    return spontaneanation


def clean_tompkast(tompkast):

    tompkast = xml_to_df(tompkast)
        
    date_parser(tompkast)
    
    tompkast['guests'] = tompkast.title.str.extract(r'Episode \d+: ([^:]+)',expand=True)
    
    guest_split('Live ', tompkast)
    replace('', np.nan, tompkast)
    
    tompkast = tompkast[pd.notnull(tompkast['guests'])]
    tompkast = splitDataFrameList(tompkast, 'guests', ', and ')
    tompkast = splitDataFrameList(tompkast, 'guests', ', & ')
    tompkast = splitDataFrameList(tompkast, 'guests', ', ')
    tompkast = splitDataFrameList(tompkast, 'guests', ',')
    tompkast = splitDataFrameList(tompkast, 'guests', ' & ')
    tompkast = splitDataFrameList(tompkast, 'guests', ' And ')
    tompkast = splitDataFrameList(tompkast, 'guests', ' and ')

    tompkast = tompkast[tompkast.guests.str.contains('The ') == False]

    tompkast['guests'] = [g.rstrip() for g in tompkast['guests']]
    
    return tompkast

def clean_dead_authors(dead_authors):

    dead_authors = xml_to_df(dead_authors)
        
    date_parser(dead_authors)
    
    dead_authors['guests'] = dead_authors.title.str.extract(r'featuring ([^:]+)',expand=True)
    
    dead_authors = dead_authors[pd.notnull(dead_authors['guests'])]
    dead_authors = splitDataFrameList(dead_authors, 'guests', ', and ')
    dead_authors = splitDataFrameList(dead_authors, 'guests', ', & ')
    dead_authors = splitDataFrameList(dead_authors, 'guests', ', ')
    dead_authors = splitDataFrameList(dead_authors, 'guests', ',')
    dead_authors = splitDataFrameList(dead_authors, 'guests', ' & ')
    dead_authors = splitDataFrameList(dead_authors, 'guests', ' And ')
    dead_authors = splitDataFrameList(dead_authors, 'guests', ' and ')

    dead_authors['guests'] = [g.rstrip() for g in dead_authors['guests']]
    
    return dead_authors


def clean_bone_zone(bone_zone):

    bone_zone = xml_to_df(bone_zone)
        
    date_parser(bone_zone)
    
    bone_zone['guests'] = bone_zone.title.str.extract(r'\#\d+ ([^:^\-^\(]+)',expand=True)
    
    for index, row in bone_zone.iterrows():
        if(pd.notnull(row['guests'])):
            bone_zone.at[index, 'guests'] = row['guests'].title()
            

    guest_split(' Part', bone_zone)
    bone_zone = bone_zone[bone_zone.guests.str.contains('Of ') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains('The ') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains('Girlfriend') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'\#') == False]

    guest_split(' Interview', bone_zone)
    guest_split(' In Studio', bone_zone)
    guest_split(' Live', bone_zone)
    guest_split(' Telethon', bone_zone)
    
    bone_zone = bone_zone[pd.notnull(bone_zone['guests'])]
    bone_zone = splitDataFrameList(bone_zone, 'guests', ', and ')
    bone_zone = splitDataFrameList(bone_zone, 'guests', ', & ')
    bone_zone = splitDataFrameList(bone_zone, 'guests', ', ')
    bone_zone = splitDataFrameList(bone_zone, 'guests', ',')
    bone_zone = splitDataFrameList(bone_zone, 'guests', ' & ')
    bone_zone = splitDataFrameList(bone_zone, 'guests', ' And ')
    bone_zone = splitDataFrameList(bone_zone, 'guests', ' and ')
    bone_zone = splitDataFrameList(bone_zone, 'guests', '/')

    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Parents') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Episode') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Phone Sex') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Live ') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Upstairs') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Special') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Are Us') == False]
    bone_zone = bone_zone[bone_zone.guests.str.contains(r'Christmas') == False]

    bone_zone['guests'] = [g.rstrip() for g in bone_zone['guests']]
    
    return bone_zone


def clean_economic_rockstar(economic_rockstar):

    economic_rockstar = xml_to_df(economic_rockstar)
    
    economic_rockstar['episode'] = economic_rockstar.title.str.extract(r'(\d+): ',expand=True)
        
    date_parser(economic_rockstar)
    
    economic_rockstar['guests'] = economic_rockstar.title.str.extract(r'\d+: ([\w\s\.\,\'\`\’\&\"\-]+) on ',expand=True)
    
    guest_split(' on', economic_rockstar)
    guest_split('- ', economic_rockstar)
    
    for index, row in economic_rockstar.iterrows():
        if(row['episode']=='009'):
            economic_rockstar.at[index, 'guests'] = 'Naomi Brockwell'
        if(row['episode']=='131'):
            economic_rockstar.at[index, 'guests'] = 'Vernon Smith'
    
    economic_rockstar = economic_rockstar[pd.notnull(economic_rockstar['guests'])]
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ', and ')
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ', & ')
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ', ')
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ',')
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ' & ')
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ' And ')
    economic_rockstar = splitDataFrameList(economic_rockstar, 'guests', ' and ')

    economic_rockstar = economic_rockstar[economic_rockstar.guests.str.contains(r'The ') == False]

    economic_rockstar['guests'] = [g.rstrip() for g in economic_rockstar['guests']]
    
    return economic_rockstar


def clean_john_roy(john_roy):

    john_roy = xml_to_df(john_roy)
        
    date_parser(john_roy)
    
    john_roy['guests'] = john_roy['title']
    
    guest_split(': ', john_roy)
    guest_split(', ', john_roy)

    replace('TJ Miller', 'T.J. Miller', john_roy)
    replace('Brea & Zane Grant', 'Brea Grant & Zane Grant', john_roy)
    john_roy = splitDataFrameList(john_roy, 'guests', ' & ')

    john_roy = john_roy[john_roy.guests.str.contains('Episode') == False]
    
    return john_roy


def clean_kurt_braunohler(kurt_braunohler):

    kurt_braunohler = xml_to_df(kurt_braunohler)
        
    date_parser(kurt_braunohler)
    
    kurt_braunohler['guests'] = kurt_braunohler.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    kurt_braunohler = kurt_braunohler[kurt_braunohler.guests.str.contains('Other ') == False]
    kurt_braunohler = kurt_braunohler[kurt_braunohler.guests.str.contains('Found ') == False]
    kurt_braunohler = kurt_braunohler[kurt_braunohler.guests.str.contains('Zelda') == False]

    replace('Pat and Steve', 'Pat Shepherd and Steve Shaheen', kurt_braunohler)
    replace('Kurty B', 'Andy Wood', kurt_braunohler)

    guest_split_last(' Part', kurt_braunohler)
    
    kurt_braunohler = kurt_braunohler[pd.notnull(kurt_braunohler['guests'])]
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ', and ')
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ', & ')
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ', ')
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ',')
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ' & ')
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ' And ')
    kurt_braunohler = splitDataFrameList(kurt_braunohler, 'guests', ' and ')

    kurt_braunohler['guests'] = [g.rstrip() for g in kurt_braunohler['guests']]

    replace('Paul F Tompkins', 'Paul F. Tompkins', kurt_braunohler)
    
    return kurt_braunohler


def clean_steve_agee(steve_agee):

    steve_agee = xml_to_df(steve_agee)
        
    date_parser(steve_agee)
    
    steve_agee['guests'] = steve_agee['title']   #.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split_last('with ', steve_agee)
    guest_split_last('Flashback: ', steve_agee)
    guest_split(' of', steve_agee)
    guest_split(r' (', steve_agee)

    replace('Alie and Georgia', 'Alie Ward and Georgia Hardstark', steve_agee)
    replace('Cody', 'Diablo Cody', steve_agee)
    
    steve_agee = steve_agee[steve_agee.guests.str.contains('!') == False]
    steve_agee = steve_agee[steve_agee.guests.str.contains('The ') == False]
    steve_agee = steve_agee[steve_agee.guests.str.contains(' his ') == False]
    steve_agee = steve_agee[steve_agee.guests.str.contains(' is ') == False]
    steve_agee = steve_agee[steve_agee.guests.str.contains('pisode') == False]

    steve_agee = steve_agee[pd.notnull(steve_agee['guests'])]
    steve_agee = splitDataFrameList(steve_agee, 'guests', ', and ')
    steve_agee = splitDataFrameList(steve_agee, 'guests', ', & ')
    steve_agee = splitDataFrameList(steve_agee, 'guests', ', ')
    steve_agee = splitDataFrameList(steve_agee, 'guests', ',')
    steve_agee = splitDataFrameList(steve_agee, 'guests', ' & ')
    steve_agee = splitDataFrameList(steve_agee, 'guests', ' And ')
    steve_agee = splitDataFrameList(steve_agee, 'guests', ' and ')

    steve_agee['guests'] = [g.rstrip() for g in steve_agee['guests']]
    
    return steve_agee


def clean_jon_gabrus(jon_gabrus):

    jon_gabrus = xml_to_df(jon_gabrus)
        
    date_parser(jon_gabrus)
    
    jon_gabrus['guests'] = jon_gabrus.title.str.extract(r'w\/ ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    jon_gabrus = jon_gabrus[jon_gabrus.guests.str.contains('2 ') == False]

    replace('Black Men Cant Jump', 'Jonathan Braylock, James III, and Jerah Milligan', jon_gabrus)
    replace('The Action Boyz', 'Ben Rodgers and Ryan Stanger', jon_gabrus)

    guest_split_last('Creators ', jon_gabrus)
    guest_split_last('Coordinator ', jon_gabrus)
    
    jon_gabrus = jon_gabrus[pd.notnull(jon_gabrus['guests'])]
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ', and ')
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ', & ')
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ', ')
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ',')
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ' & ')
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ' And ')
    jon_gabrus = splitDataFrameList(jon_gabrus, 'guests', ' and ')

    jon_gabrus['guests'] = [g.rstrip() for g in jon_gabrus['guests']]
    
    return jon_gabrus

def clean_x_files(x_files):

    x_files = xml_to_df(x_files)
        
    date_parser(x_files)
    
    x_files['guests'] = x_files.title.str.extract(r'[Ww]ith ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(', ', x_files)
    guest_split(' LIVE', x_files)
    guest_split_last('writer ', x_files)
    
    replace('Brea Grant and Zane Grant', 'Brea and Zane Grant', x_files)
    replace('Emily Gordon', 'Emily V. Gordon', x_files)
    replace('Brea and Zane Grant', 'Brea Grant and Zane Grant', x_files)
    
    x_files = x_files[pd.notnull(x_files['guests'])]
    x_files = splitDataFrameList(x_files, 'guests', ', and ')
    x_files = splitDataFrameList(x_files, 'guests', ', & ')
    x_files = splitDataFrameList(x_files, 'guests', ', ')
    x_files = splitDataFrameList(x_files, 'guests', ',')
    x_files = splitDataFrameList(x_files, 'guests', ' & ')
    x_files = splitDataFrameList(x_files, 'guests', ' And ')
    x_files = splitDataFrameList(x_files, 'guests', ' and ')

    guest_split_last('with ', x_files)

    x_files['guests'] = [g.rstrip() for g in x_files['guests']]
    
    return x_files


def clean_jonathan_van_ness(jonathan_van_ness):

    jonathan_van_ness = xml_to_df(jonathan_van_ness)
        
    date_parser(jonathan_van_ness)
    
    jonathan_van_ness['guests'] = jonathan_van_ness.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-\/]+)',expand=True)
    
    guest_split(', ', jonathan_van_ness)
    guest_split(' of', jonathan_van_ness)

    guest_split_last('writer ', jonathan_van_ness)
    guest_split_last('Prof. ', jonathan_van_ness)
    guest_split_last('professor ', jonathan_van_ness)
    guest_split_last('actress', jonathan_van_ness)
    guest_split_last('student', jonathan_van_ness)
    guest_split_last('author ', jonathan_van_ness)
    guest_split_last('Consultant ', jonathan_van_ness)
    guest_split_last('biologist ', jonathan_van_ness)
    guest_split_last('director ', jonathan_van_ness)
    guest_split_last('actor ', jonathan_van_ness)
    guest_split_last('lobbyist ', jonathan_van_ness)
    guest_split_last('designer ', jonathan_van_ness)
    guest_split_last('comedian ', jonathan_van_ness)
    guest_split_last('Clinician ', jonathan_van_ness)
    guest_split_last('Dr ', jonathan_van_ness)
    
    jonathan_van_ness = jonathan_van_ness[pd.notnull(jonathan_van_ness['guests'])]
    jonathan_van_ness = splitDataFrameList(jonathan_van_ness, 'guests', ' and ')

    jonathan_van_ness['guests'] = [g.rstrip() for g in jonathan_van_ness['guests']]
    
    return jonathan_van_ness


def clean_hollywood_handbook(hollywood_handbook):

    hollywood_handbook = xml_to_df(hollywood_handbook)
        
    date_parser(hollywood_handbook)
    
    hollywood_handbook['guests'] = hollywood_handbook.title.str.extract(r'([\w\s\.\'\`\’\&\"\-]+), Our',expand=True)
    
    hollywood_handbook = hollywood_handbook[pd.notnull(hollywood_handbook['guests'])]

    hollywood_handbook = splitDataFrameList(hollywood_handbook, 'guests', ' and ')

    hollywood_handbook = hollywood_handbook[hollywood_handbook.guests.str.contains(r'Her Friends') == False]
    hollywood_handbook = hollywood_handbook[hollywood_handbook.guests.str.contains(r'Listeners') == False]

    hollywood_handbook['guests'] = [g.rstrip() for g in hollywood_handbook['guests']]
    
    return hollywood_handbook


def clean_rupaul(rupaul):

    rupaul = xml_to_df(rupaul)
        
    date_parser(rupaul)
    
    rupaul['guests'] = rupaul.title.str.extract(r'Episode \d+: ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(' Returns', rupaul)
    guest_split_last('with ', rupaul)
    guest_split_last('With ', rupaul)
    guest_split_last('featuring ', rupaul)

    replace('David & Amy Sedaris', 'David Sedaris & Amy Sedaris', rupaul)

    
    rupaul = rupaul[rupaul.guests.str.contains(r'[Tt]he ') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r' I ') == False] 
    rupaul = rupaul[rupaul.guests.str.contains(r' Your ') == False]
    
    rupaul = rupaul[pd.notnull(rupaul['guests'])]
    rupaul = splitDataFrameList(rupaul, 'guests', ', and ')
    rupaul = splitDataFrameList(rupaul, 'guests', ', & ')
    rupaul = splitDataFrameList(rupaul, 'guests', ', ')
    rupaul = splitDataFrameList(rupaul, 'guests', ',')
    rupaul = splitDataFrameList(rupaul, 'guests', ' & ')
    rupaul = splitDataFrameList(rupaul, 'guests', ' And ')
    rupaul = splitDataFrameList(rupaul, 'guests', ' and ')

    replace('Ross Mathews.', 'Ross Mathews', rupaul)
    replace('Alaska', 'Alaska Thunderfuck', rupaul)

    rupaul = rupaul[rupaul.guests.str.contains(r'Halloween') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Christmas') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Our ') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Ear Hair') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'EnterTaintment') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Hawaii') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Las Vegas') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Facelifts') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Juicing') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Disco Jesus') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Meditation') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Nail Art') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Auditions') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Whoreders') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Yourself') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Ruenactments') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'Queer Eye') == False]
    rupaul = rupaul[rupaul.guests.str.contains(r'RATS') == False]


    rupaul['guests'] = [g.rstrip() for g in rupaul['guests']]
    
    return rupaul


def clean_shane_dawson(shane_dawson):

    shane_dawson = xml_to_df_desc(shane_dawson)
        
    date_parser(shane_dawson)
    
    shane_dawson['guests'] = shane_dawson.description.str.extract(r'interview ([\w\s\.\,\'\`\’\&\"\-]+)!',expand=True)
    
    shane_dawson = shane_dawson.drop('description', 1)
    
    guest_split(', the ', shane_dawson)
    guest_split(' of ', shane_dawson)
    guest_split_last('star ', shane_dawson)
    guest_split_last('stars ', shane_dawson)
    guest_split_last('psychic ', shane_dawson)
    guest_split_last('wrangler ', shane_dawson)
    guest_split_last("Tank's ", shane_dawson)
    guest_split_last('"Scare Actor" ', shane_dawson)
    guest_split_last('Superfan ', shane_dawson)
    guest_split_last(' aka ', shane_dawson)
    guest_split_last(' AKA ', shane_dawson)
    guest_split_last('Performer ', shane_dawson)
    guest_split_last('escorts ', shane_dawson)
    
    shane_dawson = shane_dawson[shane_dawson.guests.str.contains(r'[Tt]he ') == False]
    
    shane_dawson = shane_dawson[pd.notnull(shane_dawson['guests'])]
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ', and ')
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ', & ')
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ', ')
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ',')
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ' & ')
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ' And ')
    shane_dawson = splitDataFrameList(shane_dawson, 'guests', ' and ')

    shane_dawson = shane_dawson[shane_dawson.guests.str.contains(r"Uno's") == False]
    shane_dawson = shane_dawson[shane_dawson.guests.str.contains(r"A Stripper") == False]
    shane_dawson = shane_dawson[shane_dawson.guests.str.contains(r"Social ") == False]
    shane_dawson = shane_dawson[shane_dawson.guests.str.contains(r"their Moms") == False]

    shane_dawson['guests'] = [g.rstrip() for g in shane_dawson['guests']]
    
    return shane_dawson


def clean_grace_helbig(grace_helbig):

    grace_helbig = xml_to_df(grace_helbig)
        
    date_parser(grace_helbig)
    
    grace_helbig['guests'] = grace_helbig.title.str.extract(r'Ep. \d+ - ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(' - ', grace_helbig)
    guest_split(' of', grace_helbig)
    guest_split(' Live', grace_helbig)
    guest_split(' LIVE', grace_helbig)
    guest_split(' at ', grace_helbig)
    guest_split(' Explains', grace_helbig)
    guest_split_last("Try Guys' ", grace_helbig)
    guest_split_last("Sorted Food's ", grace_helbig)
    guest_split_last("with ", grace_helbig)
    
    replace('Guys We F', 'Corinne Fisher & Krystyna Hutchinson', grace_helbig)
    replace('AsapSCIENCE', np.nan, grace_helbig)
    replace('SUP3RFRUIT', 'Sup3rfruit', grace_helbig)
    replace('Jack and Dean', 'Jack Howard and Dean Dobbs', grace_helbig)
    replace('Eugene and Zach', 'Eugene Lee Yang & Zach Kornfeld', grace_helbig)
    replace('Ned & Keith', 'Ned Fulmer & Keith Habersberger', grace_helbig)
    replace('Zane & Heath', 'Zane Hijazi and Heath Hussar', grace_helbig)
    replace('Scotty & Toddy', 'Scott Sire & Todd Smith', grace_helbig)
    replace('The Gabbie Show', 'Gabbie Hanna', grace_helbig)
    replace('Carly & Erin', 'Carly Incontro & Erin Gilfoy', grace_helbig)
    replace('FunForLouis', 'Louis Cole', grace_helbig)
    replace('Vsauce', 'Michael Stevens', grace_helbig)
    
    replace('Grace', np.nan, grace_helbig)
    grace_helbig = grace_helbig[pd.notnull(grace_helbig['guests'])]
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ', and ')
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ', & ')
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ', ')
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ',')
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ' & ')
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ' And ')
    grace_helbig = splitDataFrameList(grace_helbig, 'guests', ' and ')

    replace('Rhett', 'Rhett James McLaughlin', grace_helbig)
    replace('Link', 'Charles Lincoln Neal', grace_helbig)

    grace_helbig = grace_helbig[grace_helbig.guests.str.contains(r'Special') == False]
    grace_helbig = grace_helbig[grace_helbig.guests.str.contains(r' Rants') == False]
    grace_helbig = grace_helbig[grace_helbig.guests.str.contains(r'Halloween') == False]
    grace_helbig = grace_helbig[grace_helbig.guests.str.contains(r'The Best') == False]
    grace_helbig = grace_helbig[grace_helbig.guests.str.contains(r'Welcome') == False]


    grace_helbig['guests'] = [g.rstrip() for g in grace_helbig['guests']]
    
    return grace_helbig


def clean_think_again(think_again):

    think_again = xml_to_df(think_again)
        
    date_parser(think_again)
    
    think_again['guests'] = think_again.title.str.extract(r'\d+. ([\w\s\.\,\'\`\’\&\"\-]+) \(',expand=True)
    
    guest_split(', ', think_again)
    
    think_again = think_again[pd.notnull(think_again['guests'])]
    think_again = splitDataFrameList(think_again, 'guests', ', and ')
    think_again = splitDataFrameList(think_again, 'guests', ', & ')
    think_again = splitDataFrameList(think_again, 'guests', ', ')
    think_again = splitDataFrameList(think_again, 'guests', ',')
    think_again = splitDataFrameList(think_again, 'guests', ' & ')
    think_again = splitDataFrameList(think_again, 'guests', ' And ')
    think_again = splitDataFrameList(think_again, 'guests', ' and ')

    think_again['guests'] = [g.rstrip() for g in think_again['guests']]
    
    return think_again


def clean_rationally_speaking(rationally_speaking):

    rationally_speaking = xml_to_df(rationally_speaking)
        
    date_parser(rationally_speaking)
    
    rationally_speaking['guests'] = rationally_speaking.title.str.extract(r'\d+ - ([\w\s\.\,\'\`\’\&\"\-]+) (?:on|and the|discusses) ',expand=True)
    
    guest_split(' on', rationally_speaking)
    guest_split_last('With ', rationally_speaking)
    guest_split_last('Guest ', rationally_speaking)
    guest_split_last('Historian ', rationally_speaking)
    guest_split_last(' -- ', rationally_speaking)
    
    rationally_speaking = rationally_speaking[pd.notnull(rationally_speaking['guests'])]
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ', and ')
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ', & ')
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ', ')
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ',')
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ' & ')
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ' And ')
    rationally_speaking = splitDataFrameList(rationally_speaking, 'guests', ' and ')

    rationally_speaking['guests'] = [g.rstrip() for g in rationally_speaking['guests']]

    rationally_speaking = rationally_speaking[rationally_speaking.guests.str.contains(r'Crowdsourcing') == False]
    rationally_speaking = rationally_speaking[rationally_speaking.guests.str.contains(r'Celebrities') == False]
    rationally_speaking = rationally_speaking[rationally_speaking.guests.str.contains(r'Nonsense') == False]
    rationally_speaking = rationally_speaking[rationally_speaking.guests.str.contains(r'Massimo') == False]

    
    return rationally_speaking


def clean_skepticality(skepticality):

    skepticality = xml_to_df_desc(skepticality)
        
    date_parser(skepticality)
    
    skepticality['guests'] = skepticality.description.str.extract(r'(?:with |guest, )([\w\s\.\'\`\’\&\"\-]+), ',expand=True)
    skepticality = skepticality.drop('description', 1)
    
    skepticality.replace(u"\u00A0", " ", regex=True, inplace=True)
    
    guest_split(' about', skepticality)
    guest_split(' had', skepticality)
    guest_split(' not', skepticality)
    guest_split(' to ', skepticality)
    guest_split(' on ', skepticality)
    guest_split('. Until', skepticality)
    guest_split('. We', skepticality)
    guest_split(' PhD', skepticality)
    guest_split(' discus', skepticality)
    guest_split('. William', skepticality)
    guest_split('biochemistries. ', skepticality)
    guest_split_last('publisher ', skepticality)
    guest_split_last('editor ', skepticality)
    guest_split_last('author ', skepticality)
    guest_split_last('programmer ', skepticality)
    guest_split_last('scientist ', skepticality)
    guest_split_last('podcaster ', skepticality)
    guest_split_last('bloggers ', skepticality)
    guest_split_last('Colonel ', skepticality)
    guest_split_last('spokesman ', skepticality)
    guest_split_last('guest ', skepticality)
    guest_split_last('Dr. ', skepticality)
    guest_split_last('journalist ', skepticality)
    guest_split_last('humanist ', skepticality)
    guest_split_last('professor ', skepticality)
    guest_split_last("ologist' ", skepticality)
    guest_split_last('Professor ', skepticality)
    guest_split_last('sister ', skepticality)
    guest_split_last('including ', skepticality)

    replace('James Randi.  We also get some listener surprises', 'James Randi', skepticality)
    replace('turned hard science fiction author', 'Andy Weir', skepticality)
    replace('someone who knows a bit', 'Dr. Peter Steidl', skepticality)
    replace('Molly', 'Molly Crockett', skepticality)
    replace('her', 'Dale McGowan and Karen Stollznow', skepticality)

    skepticality = skepticality[skepticality.guests.str.contains(r'[Tt]he ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r' of ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r' from ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r' for ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'guest') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r' this ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'touching ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'their') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r' have ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'Swoopy') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'psychologist') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'our vastly') == False]
    
    skepticality = skepticality[pd.notnull(skepticality['guests'])]
    skepticality = splitDataFrameList(skepticality, 'guests', ', and ')
    skepticality = splitDataFrameList(skepticality, 'guests', ', & ')
    skepticality = splitDataFrameList(skepticality, 'guests', ', ')
    skepticality = splitDataFrameList(skepticality, 'guests', ',')
    skepticality = splitDataFrameList(skepticality, 'guests', ' & ')
    skepticality = splitDataFrameList(skepticality, 'guests', ' And ')
    skepticality = splitDataFrameList(skepticality, 'guests', ' and ')

    replace('Derek', np.nan, skepticality)
    replace('novel', np.nan, skepticality)
    replace('us', np.nan, skepticality)
    replace('a short announcement', np.nan, skepticality)
    replace('SETI Astronomer', np.nan, skepticality)
    replace('author', np.nan, skepticality)
    replace('"that guy"', np.nan, skepticality)
    replace('Jim', 'Jim Ottaviani', skepticality)
    replace('Alexis', 'Alexis Gambis', skepticality)
    replace('Daniel', 'Daniel Loxton', skepticality)
    replace('Donald', 'Donald Prothero', skepticality)
    replace('Hal', 'Hal Bidlack', skepticality)
    replace('Sara', 'Sara E. Mayhew', skepticality)
    skepticality = skepticality[pd.notnull(skepticality['guests'])]

    skepticality = skepticality[skepticality.guests.str.contains(r'our vastly') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'a look') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'messages') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'rabble ') == False]
    skepticality = skepticality[skepticality.guests.str.contains(r'reliable ') == False]

    skepticality['guests'] = [g.rstrip() for g in skepticality['guests']]
    
    return skepticality


def clean_friendly_atheist(friendly_atheist):

    friendly_atheist = xml_to_df(friendly_atheist)
        
    date_parser(friendly_atheist)
    
    friendly_atheist['guests'] = friendly_atheist.title.str.extract(r'Ep. \d+ - ([\w\s\.\,\'\`\’\&\"\-]+), ',expand=True)

    guest_split_last('TAM2014 - ', friendly_atheist)

    
    friendly_atheist = friendly_atheist[pd.notnull(friendly_atheist['guests'])]
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ', and ')
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ', & ')
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ', ')
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ',')
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ' & ')
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ' And ')
    friendly_atheist = splitDataFrameList(friendly_atheist, 'guests', ' and ')
    
    guest_split_last('Comedians ', friendly_atheist)
    guest_split_last('Attorney ', friendly_atheist)

    replace('Hemant', np.nan, friendly_atheist)
    replace('Jessica', np.nan, friendly_atheist)
    friendly_atheist = friendly_atheist[pd.notnull(friendly_atheist['guests'])]

    
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r' of ') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r'Goodbye') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r'Yep') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r'Congratulations') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r'Why') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r'Al Franken') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r'We ') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r' Do ') == False]
    friendly_atheist = friendly_atheist[friendly_atheist.guests.str.contains(r' Not ') == False]

    friendly_atheist['guests'] = [g.rstrip() for g in friendly_atheist['guests']]
    
    return friendly_atheist


def clean_katie_couric(katie_couric):

    katie_couric = xml_to_df(katie_couric)
        
    date_parser(katie_couric)
    
    katie_couric['guests'] = katie_couric.title.str.extract(r'\d+.\d? ([\w\s\.\,\'\`\’\&\"\-]+):',expand=True)
    katie_couric['guests1'] = katie_couric.title.str.extract(r'Wonder Woman: ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    replace('Wonder Woman', '', katie_couric)
    katie_couric.replace(np.nan, '', regex=True, inplace=True)
    katie_couric['guests'] = katie_couric['guests'] + katie_couric['guests1']
    katie_couric.replace('', np.nan, regex=True, inplace=True)
    katie_couric = katie_couric.drop('guests1', 1)
    
    guest_split_last('Sen. ', katie_couric)
    guest_split_last('Rep. ', katie_couric)
    
    replace('Pod Save America', 'Jon Favreau, Jon Lovett, Tommy Vietor', katie_couric)
    replace("What I've Learned", 'Christie Todd Whitman', katie_couric)
    
    katie_couric = katie_couric[pd.notnull(katie_couric['guests'])]
    katie_couric = splitDataFrameList(katie_couric, 'guests', ', and ')
    katie_couric = splitDataFrameList(katie_couric, 'guests', ', & ')
    katie_couric = splitDataFrameList(katie_couric, 'guests', ', ')
    katie_couric = splitDataFrameList(katie_couric, 'guests', ',')
    katie_couric = splitDataFrameList(katie_couric, 'guests', ' & ')
    katie_couric = splitDataFrameList(katie_couric, 'guests', ' And ')
    katie_couric = splitDataFrameList(katie_couric, 'guests', ' and ')
    
    katie_couric = katie_couric[katie_couric.guests.str.contains(r' Time ') == False]
    katie_couric = katie_couric[katie_couric.guests.str.contains(r' Presents') == False]

    katie_couric['guests'] = [g.rstrip() for g in katie_couric['guests']]
    
    return katie_couric


def clean_etl(etl):

    etl = xml_to_df(etl)
        
    date_parser(etl)
    
    etl['guests'] = etl.title.str.extract(r'([\w\s\.\,\'\`\’\&\"\-]+) \(',expand=True)
    
    etl = etl[pd.notnull(etl['guests'])]
    etl = splitDataFrameList(etl, 'guests', ', and ')
    etl = splitDataFrameList(etl, 'guests', ', & ')
    etl = splitDataFrameList(etl, 'guests', ', ')
    etl = splitDataFrameList(etl, 'guests', ',')
    etl = splitDataFrameList(etl, 'guests', ' & ')
    etl = splitDataFrameList(etl, 'guests', ' And ')
    etl = splitDataFrameList(etl, 'guests', ' and ')

    etl['guests'] = [g.rstrip() for g in etl['guests']]
    
    return etl


def clean_ezra_klein(ezra_klein):

    ezra_klein = xml_to_df(ezra_klein)
        
    date_parser(ezra_klein)
    
    ezra_klein['guests1'] = ezra_klein.title.str.extract(r'^([\w\s\.\,\'\`\’\&\"\-]+) on ',expand=True)
    ezra_klein['guests2'] = ezra_klein.title.str.extract(r' with ([\w\s\.\,\'\`\’\&\"\-]+)$',expand=True)
    ezra_klein.replace(np.nan, '', regex=True, inplace=True)
    ezra_klein['guests'] = ezra_klein['guests1'] + ezra_klein['guests2']  
    ezra_klein = ezra_klein.drop('guests1', 1)
    ezra_klein = ezra_klein.drop('guests2', 1)
    ezra_klein.replace('', np.nan, regex=True, inplace=True)
    
    guest_split(', ', ezra_klein)
    guest_split('gives ', ezra_klein)
    guest_split_last('America’s ', ezra_klein)
    guest_split_last('intellectual ', ezra_klein)
    guest_split_last('lobbyist ', ezra_klein)
    guest_split_last('Secretary ', ezra_klein)
    guest_split_last('CEO ', ezra_klein)
    guest_split_last('chef ', ezra_klein)
    
    ezra_klein = ezra_klein[ezra_klein.guests.str.contains(r' better ') == False]
    ezra_klein = ezra_klein[ezra_klein.guests.str.contains(r' most ') == False]
    ezra_klein = ezra_klein[ezra_klein.guests.str.contains(r'Death') == False]
    
    ezra_klein = ezra_klein[pd.notnull(ezra_klein['guests'])]

    ezra_klein['guests'] = [g.rstrip() for g in ezra_klein['guests']]
    
    return ezra_klein


def clean_john_gruber(john_gruber):

    john_gruber = xml_to_df(john_gruber)
        
    date_parser(john_gruber)
    
    john_gruber['guests'] = john_gruber.title.str.extract(r'With ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)
    
    guest_split_last('Guest ', john_gruber)
    guest_split_last('Guests ', john_gruber)
    
    john_gruber = john_gruber[pd.notnull(john_gruber['guests'])]
    john_gruber = splitDataFrameList(john_gruber, 'guests', ', and ')
    john_gruber = splitDataFrameList(john_gruber, 'guests', ', & ')
    john_gruber = splitDataFrameList(john_gruber, 'guests', ', ')
    john_gruber = splitDataFrameList(john_gruber, 'guests', ',')
    john_gruber = splitDataFrameList(john_gruber, 'guests', ' & ')
    john_gruber = splitDataFrameList(john_gruber, 'guests', ' And ')
    john_gruber = splitDataFrameList(john_gruber, 'guests', ' and ')

    replace("Ben ‘Bengate’ Thompson", 'Ben Thompson', john_gruber)
    replace("More", np.nan, john_gruber)
    john_gruber = john_gruber[pd.notnull(john_gruber['guests'])]

    john_gruber['guests'] = [g.rstrip() for g in john_gruber['guests']]
    
    return john_gruber


def clean_shane_mauss(shane_mauss):

    shane_mauss = xml_to_df_desc(shane_mauss)
    
    shane_mauss['episode'] = len(shane_mauss) - shane_mauss.index
        
    date_parser(shane_mauss)
    
    shane_mauss['guests'] = shane_mauss.description.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)
    shane_mauss = shane_mauss.drop('description', 1)
    

        
    for index, row in shane_mauss.iterrows():
        if(row['episode']==145):
            shane_mauss.at[index, 'guests'] = 'Eric Osborne'
        if(row['episode']==146):
            shane_mauss.at[index, 'guests'] = 'Emanuel Sferios'
        if(row['episode']==147):
            shane_mauss.at[index, 'guests'] = 'Peter Boghossian'
        if(row['episode']==148):
            shane_mauss.at[index, 'guests'] = 'Katherine MacLean'
        if(row['episode']==149):
            shane_mauss.at[index, 'guests'] = 'Martie Haselton'
        if(row['episode']==150):
            shane_mauss.at[index, 'guests'] = 'Jana Gallus'
        if(row['episode']==151):
            shane_mauss.at[index, 'guests'] = 'Cassie Mogilner Holmes'
        if(row['episode']==152):
            shane_mauss.at[index, 'guests'] = 'Chris Kilham'
        if(row['episode']==153):
            shane_mauss.at[index, 'guests'] = 'James A. Lindsay'
        if(row['episode']==154):
            shane_mauss.at[index, 'guests'] = 'Brittany Alperin'
        if(row['episode']==155):
            shane_mauss.at[index, 'guests'] = 'John Harkness'
        if(row['episode']==158):
            shane_mauss.at[index, 'guests'] = 'Rachel Stone'
        if(row['episode']==159):
            shane_mauss.at[index, 'guests'] = 'Katharine Marske'
        if(row['episode']==160):
            shane_mauss.at[index, 'guests'] = 'Joel Suss'
        if(row['episode']==161):
            shane_mauss.at[index, 'guests'] = np.nan
        if(row['episode']==162):
            shane_mauss.at[index, 'guests'] = np.nan
        if(row['episode']==163):
            shane_mauss.at[index, 'guests'] = 'Rebecca Hood'
            
    shane_mauss = shane_mauss[pd.notnull(shane_mauss['guests'])]
    shane_mauss['guests'] = [g.rstrip('\n \n') for g in shane_mauss['guests']]
    
    guest_split(', Ph.D', shane_mauss)
    guest_split_last('Ph.D. ', shane_mauss)
            
            
    replace('Todd & Viviana Weekes-Shackelford.', 'Todd K. Shackelford & Viviana Weekes-Shackelford.', shane_mauss)
    
    shane_mauss = shane_mauss[pd.notnull(shane_mauss['guests'])]
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ', and ')
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ', & ')
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ', ')
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ',')
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ' & ')
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ' And ')
    shane_mauss = splitDataFrameList(shane_mauss, 'guests', ' and ')

    shane_mauss = shane_mauss[shane_mauss.guests.str.contains(r'Zookeepers') == False]
    shane_mauss = shane_mauss[shane_mauss.guests.str.contains(r'Live from') == False]

    shane_mauss['guests'] = [g.rstrip('.') for g in shane_mauss['guests']]
    shane_mauss['guests'] = [g.rstrip() for g in shane_mauss['guests']]
    shane_mauss['guests'] = [g.lstrip() for g in shane_mauss['guests']]
    
    return shane_mauss


def clean_double_date(double_date):

    double_date = xml_to_df(double_date)
        
    date_parser(double_date)
    
    double_date['guests'] = double_date.title.str.extract(r'Double Date: ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)
    
    double_date = double_date[pd.notnull(double_date['guests'])]
    double_date = splitDataFrameList(double_date, 'guests', ', and ')
    double_date = splitDataFrameList(double_date, 'guests', ', & ')
    double_date = splitDataFrameList(double_date, 'guests', ', ')
    double_date = splitDataFrameList(double_date, 'guests', ',')
    double_date = splitDataFrameList(double_date, 'guests', ' & ')
    double_date = splitDataFrameList(double_date, 'guests', ' And ')
    double_date = splitDataFrameList(double_date, 'guests', ' and ')

    guest_split(' - ', double_date)
    guest_split(' From', double_date)

    double_date['guests'] = [g.rstrip() for g in double_date['guests']]
    
    return double_date


def clean_zach_leary(zach_leary):

    zach_leary = xml_to_df(zach_leary)
        
    date_parser(zach_leary)
    
    zach_leary['guests'] = zach_leary.title.str.extract(r'Episode \d+ (?:-|with) ([\w\s\.\,\'\`\’\&\"\-\‘\(\)]+)',expand=True)
    
    guest_split('Live', zach_leary)
    guest_split(', PhD', zach_leary)
    
    
    replace('Chris Ryan', 'Christopher Ryan', zach_leary)
    replace('Donald (DJ) Salmon, Jr.', 'Donald Salmon Jr.', zach_leary)
    replace('Alex and Allyson Grey', 'Alex Grey and Allyson Grey', zach_leary)
    replace('Alex and Allyson Grey and Duncan Trussell', 'Alex Grey and Allyson Grey and Duncan Trussell', zach_leary)
    replace('Jason Louv (with Ram Dass too', 'Jason Louv and Ram Dass')

    zach_leary = zach_leary[zach_leary.guests.str.contains(r' in ') == False]
    zach_leary = zach_leary[zach_leary.guests.str.contains(r'the legend ') == False]
    zach_leary = zach_leary[zach_leary.guests.str.contains(r'Community ') == False]
    
    zach_leary = zach_leary[pd.notnull(zach_leary['guests'])]
    zach_leary = splitDataFrameList(zach_leary, 'guests', ', and ')
    zach_leary = splitDataFrameList(zach_leary, 'guests', ', & ')
    zach_leary = splitDataFrameList(zach_leary, 'guests', ', ')
    zach_leary = splitDataFrameList(zach_leary, 'guests', ',')
    zach_leary = splitDataFrameList(zach_leary, 'guests', ' & ')
    zach_leary = splitDataFrameList(zach_leary, 'guests', ' And ')
    zach_leary = splitDataFrameList(zach_leary, 'guests', ' and ')

    replace('the Legend of Angelyne', 'Angelyne', zach_leary)

    zach_leary['guests'] = [g.rstrip(r'\( ') for g in zach_leary['guests']]

    zach_leary['guests'] = [g.rstrip() for g in zach_leary['guests']]
    
    return zach_leary


def clean_cory_allen(cory_allen):

    cory_allen = xml_to_df(cory_allen)
        
    date_parser(cory_allen)
    
    cory_allen['guests'] = cory_allen.title.str.extract(r'\#\d+ ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)
    
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' of ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' Of ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' the ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r'The ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' To ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' Our ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' better ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' Into ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' is ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' with ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' Your ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' Are ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r' and ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r'One ') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r'Be What You Are') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r'Existential Paralysis') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r'Cory Reads Cory') == False]
    cory_allen = cory_allen[cory_allen.guests.str.contains(r'Consciousness Cryptomnesia') == False]
    
    replace('John F Simon Jr', 'John F. Simon Jr', cory_allen)
    
    cory_allen = cory_allen[pd.notnull(cory_allen['guests'])]
    cory_allen = splitDataFrameList(cory_allen, 'guests', ' & ')

    cory_allen['guests'] = [g.rstrip() for g in cory_allen['guests']]
    
    return cory_allen


def clean_raghu_markus(raghu_markus):

    raghu_markus = xml_to_df(raghu_markus)
        
    date_parser(raghu_markus)
    
    raghu_markus['guests'] = raghu_markus.title.str.extract(r'Ep. \d+ (?:-|–) ([\w\s\.\,\'\`\’\&\"\-\‘\/]+)',expand=True)
    
    guest_split(' Part', raghu_markus)
    guest_split(' Returns', raghu_markus)
    guest_split(' Live', raghu_markus)
    guest_split(' Goes', raghu_markus)
    guest_split(' Explores', raghu_markus)
    guest_split("'s ", raghu_markus)
    guest_split_last('with ', raghu_markus)
    guest_split_last('w/ ', raghu_markus)
    guest_split_last('Clearly ', raghu_markus)
    guest_split_last('Founder ', raghu_markus)
    
    replace('Anne and Joan Watts', 'Anne Watts and Joan Watts', raghu_markus)
    replace('It', np.nan, raghu_markus)
    replace('2018', np.nan, raghu_markus)
    replace("Teal Swan's Vision", "Teal Swan", raghu_markus)
    
    
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' of ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' Of ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' the ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'The ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' To ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' Our ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' better ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' Into ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' is ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' with ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' Your ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' in ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' it ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' Days') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' than ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' as ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Politics') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Rascals') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Yourself') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Musings') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'World') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Attention') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Glories') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'After') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Suffering') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Digital') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Close') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Teachers') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'India') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Irregular') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'India') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Spontaneous') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Brain') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Within') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Happiness') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Unconscious') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Conscious') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Street') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Giant') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Matters') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'True') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Mindfulness') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' his ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' to ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' for ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Imagination') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Shock') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Power') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Thought') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r' A ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'G-d') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Mode') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Buddhism') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Abundance') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Quantum') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Tour ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Presence') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Mental') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Home') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'EUDAIMONIA') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'There') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Love') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'One ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Seekers ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Dream ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Sacred ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'Jungle ') == False]
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'What ') == False]
    
    raghu_markus = raghu_markus[pd.notnull(raghu_markus['guests'])]
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ', and ')
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ', & ')
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ', ')
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ',')
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ' & ')
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ' And ')
    raghu_markus = splitDataFrameList(raghu_markus, 'guests', ' and ')
    
    raghu_markus = raghu_markus[raghu_markus.guests.str.contains(r'MLK') == False]

    raghu_markus['guests'] = [g.rstrip() for g in raghu_markus['guests']]
    raghu_markus.replace('', np.nan, inplace=True)
    raghu_markus = raghu_markus[pd.notnull(raghu_markus['guests'])]
    
    return raghu_markus


def clean_chris_grosso(chris_grosso):

    chris_grosso = xml_to_df(chris_grosso)
        
    date_parser(chris_grosso)
    
    chris_grosso['guests'] = chris_grosso.title.str.extract(r'Ep. \d+ (?:-|–) ([\w\s\.\,\'\`\’\&\"\-\‘\/]+)',expand=True)
    
    guest_split(' Part', chris_grosso)
    guest_split(' Returns', chris_grosso)
    guest_split(', PhD', chris_grosso)
    guest_split(' - ', chris_grosso)
    guest_split_last('with ', chris_grosso)
    guest_split_last('w/ ', chris_grosso)
    guest_split_last('Fighter ', chris_grosso)
    
    chris_grosso = chris_grosso[pd.notnull(chris_grosso['guests'])]

    chris_grosso['guests'] = [g.rstrip() for g in chris_grosso['guests']]
    
    return chris_grosso


def clean_london_real(london_real):

    london_real = xml_to_df(london_real)
        
    date_parser(london_real)
    
    london_real['guests'] = london_real.title.str.extract(r'([\w\s\.\,\'\`\’\&\"\-\‘]+) - ',expand=True)
    
    london_real = london_real[london_real['duration'] > 200]
    london_real = london_real[london_real['guests'].str.len() < 22]
    
    for index, row in london_real.iterrows():
        if(pd.notnull(row['guests'])):
            london_real.at[index, 'guests'] = row['guests'].title()

    guest_split_last(' - ', london_real)
    guest_split_last('Fighter ', london_real)
    guest_split_last('With ', london_real)
    guest_split_last(' By ', london_real)

    guest_split(' Live', london_real)
    guest_split(' Is ', london_real)

    london_real = london_real[london_real.guests.str.contains(r'Now ') == False]
    london_real = london_real[london_real.guests.str.contains(r'Things ') == False]
    london_real = london_real[london_real.guests.str.contains(r' Talk') == False]
    london_real = london_real[london_real.guests.str.contains(r'The ') == False]
    london_real = london_real[london_real.guests.str.contains(r'I ') == False]
    london_real = london_real[london_real.guests.str.contains(r'Are ') == False]
    london_real = london_real[london_real.guests.str.contains(r'Q&A') == False]
    london_real = london_real[london_real.guests.str.contains(r'How To ') == False]
    london_real = london_real[london_real.guests.str.contains(r'Yourself') == False]
    london_real = london_real[london_real.guests.str.contains(r'Tbt') == False]
    london_real = london_real[london_real.guests.str.contains(r'11') == False]
    london_real = london_real[london_real.guests.str.contains(r'Manners') == False]
    london_real = london_real[london_real.guests.str.contains(r'London Vs New York') == False]
    london_real = london_real[london_real.guests.str.contains(r'Collaboration Is King') == False]
    london_real = london_real[london_real.guests.str.contains(r'Slack Killed Email') == False]

    replace('Neil Degrasse Tyson', 'Neil deGrasse Tyson', london_real)
    replace('Killing Kittens', 'Emma Sayle', london_real)
    replace('Kevin Ferguson Jr', 'Kevin Ferguson Jr.', london_real)
    replace('Dan Pena', 'Dan Peña', london_real)
    replace('Garyvee Lessons', 'Gary Vaynerchuk', london_real)
    
    london_real = london_real[pd.notnull(london_real['guests'])]

    london_real['guests'] = [g.rstrip() for g in london_real['guests']]
    
    return london_real


def clean_onnit(onnit):

    onnit = xml_to_df(onnit)
        
    date_parser(onnit)
    
    onnit['guests'] = onnit.title.str.extract(r'[Ww]ith ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)
    
    guest_split_last('friends ', onnit)
    guest_split_last('champion ', onnit)
    guest_split_last('CEO ', onnit)
    guest_split_last('Kid ', onnit)
    guest_split_last('Guest ', onnit)
    guest_split_last('Guests ', onnit)
    guest_split_last('guest ', onnit)
    guest_split_last('driver ', onnit)
    guest_split_last('Wrestler ', onnit)
    guest_split_last('Superstar ', onnit)
    guest_split_last("UFC's ", onnit)

    
    guest_split(' of', onnit)
    
    onnit = onnit[pd.notnull(onnit['guests'])]
    onnit = splitDataFrameList(onnit, 'guests', ', and ')
    onnit = splitDataFrameList(onnit, 'guests', ', & ')
    onnit = splitDataFrameList(onnit, 'guests', ', ')
    onnit = splitDataFrameList(onnit, 'guests', ',')
    onnit = splitDataFrameList(onnit, 'guests', ' & ')
    onnit = splitDataFrameList(onnit, 'guests', ' And ')
    onnit = splitDataFrameList(onnit, 'guests', ' and ')

    replace('Rafael Lovato Jr', 'Rafael Lovato Jr.', onnit)
    replace('Whey w', 'Laura Williams', onnit)
    replace('Twitch', 'Stephen Boss', onnit)

    onnit['guests'] = [g.rstrip() for g in onnit['guests']]
    
    return onnit


def clean_festival_of_sports(festival_of_sports):

    festival_of_sports = xml_to_df(festival_of_sports)
        
    date_parser(festival_of_sports)
    
    festival_of_sports['guests'] = festival_of_sports.title.str.extract(r'Episode \d+ - ([\w\s\.\,\'\`\’\&\"\-\‘\/]+)',expand=True)
    
    guest_split_last('w/ ', festival_of_sports)
    guest_split_last('"The ', festival_of_sports)
    
    guest_split('"', festival_of_sports)
    guest_split(' Returns', festival_of_sports)
    
    festival_of_sports = festival_of_sports[pd.notnull(festival_of_sports['guests'])]
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ', and ')
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ', & ')
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ', ')
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ',')
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ' & ')
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ' And ')
    festival_of_sports = splitDataFrameList(festival_of_sports, 'guests', ' and ')

    festival_of_sports = festival_of_sports[festival_of_sports.guests.str.contains(r'Introduction') == False]
    festival_of_sports = festival_of_sports[festival_of_sports.guests.str.contains(r'Tornado ') == False]

    festival_of_sports['guests'] = [g.rstrip() for g in festival_of_sports['guests']]
    
    return festival_of_sports


def clean_brody_stevens(brody_stevens):

    brody_stevens = xml_to_df(brody_stevens)
        
    date_parser(brody_stevens)
    
    brody_stevens['guests'] = brody_stevens['title']
    
    guest_split_last('with ', brody_stevens)
    guest_split_last('With ', brody_stevens)

    guest_split(' Returns', brody_stevens)
    guest_split(' II', brody_stevens)
    guest_split(' 2', brody_stevens)
    
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Brody') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'BRODY') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'The ') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r' is ') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r' To ') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Family') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'pt.') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Pt.') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r' from ') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r' From ') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Pt.') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Podcast') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Age ') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Play By') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Nasally') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Ghosts') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Detox') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Coach Bro') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'MLB') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Channel Surfing') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Off Lex') == False]
    brody_stevens = brody_stevens[brody_stevens.guests.str.contains(r'Synthetic') == False]
    
    brody_stevens = brody_stevens[pd.notnull(brody_stevens['guests'])]
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ', and ')
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ', & ')
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ', ')
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ',')
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ' & ')
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ' And ')
    brody_stevens = splitDataFrameList(brody_stevens, 'guests', ' and ')

    replace("Carl Reid's Holy Socks", 'Carl Reid', brody_stevens)

    brody_stevens['guests'] = [g.rstrip() for g in brody_stevens['guests']]
    brody_stevens['guests'] = [g.rstrip('!') for g in brody_stevens['guests']]
    
    return brody_stevens


def clean_wwdtm(wwdtm):

    wwdtm = xml_to_df(wwdtm)
        
    date_parser(wwdtm)
    
    wwdtm['guests'] = wwdtm['title']
    
    wwdtm = wwdtm[wwdtm.guests.str.contains(r'Best of') == False]
    
    wwdtm = wwdtm[pd.notnull(wwdtm['guests'])]

    wwdtm['guests'] = [g.rstrip() for g in wwdtm['guests']]
    
    return wwdtm


def clean_superego(superego):

    superego = xml_to_df_desc(superego)
        
    date_parser(superego)
    
    superego['guests'] = superego.description.str.extract(r'With ([\w\s\.\,\'\`\’\&\"\-]+). Case',expand=True)
    superego.drop('description', 1, inplace=True)
    
    superego = superego[pd.notnull(superego['guests'])]
    superego = splitDataFrameList(superego, 'guests', ', and ')
    superego = splitDataFrameList(superego, 'guests', ', & ')
    superego = splitDataFrameList(superego, 'guests', ', ')
    superego = splitDataFrameList(superego, 'guests', ',')
    superego = splitDataFrameList(superego, 'guests', ' & ')
    superego = splitDataFrameList(superego, 'guests', ' And ')
    superego = splitDataFrameList(superego, 'guests', ' and ')
    
    superego = superego[superego.guests.str.contains(r'more') == False]

    superego['guests'] = [g.rstrip() for g in superego['guests']]
    
    return superego


def clean_dan_savage(dan_savage):

    dan_savage = xml_to_df_desc(dan_savage)
        
    date_parser(dan_savage)
    
    dan_savage['guests'] = dan_savage.description.str.extract(r'(?:chats with |talk with |talks to )([\w\s\.\,\'\`\’\&\"\-]+)(?:, | on | about)',expand=True)
    dan_savage.drop('description', 1, inplace=True)
    
    guest_split(' about', dan_savage)
    guest_split(' on ', dan_savage)
    guest_split(' not', dan_savage)
    guest_split('. We', dan_savage)
    guest_split(', founder', dan_savage)
    guest_split(', author', dan_savage)
    guest_split('. And', dan_savage)
    guest_split(' of', dan_savage)
    guest_split(' who ', dan_savage)
    guest_split(', to ', dan_savage)
    guest_split(', from ', dan_savage)
    guest_split(' from ', dan_savage)
    guest_split('- ', dan_savage)
    guest_split(', ', dan_savage)
    guest_split_last('publisher ', dan_savage)
    guest_split_last('editor ', dan_savage)
    guest_split_last('author ', dan_savage)
    guest_split_last('writer ', dan_savage)
    guest_split_last('programmer ', dan_savage)
    guest_split_last('scientist ', dan_savage)
    guest_split_last('podcaster ', dan_savage)
    guest_split_last('bloggers ', dan_savage)
    guest_split_last('comedian ', dan_savage)
    guest_split_last('spokesman ', dan_savage)
    guest_split_last('guest ', dan_savage)
    guest_split_last('filmmaker ', dan_savage)
    guest_split_last('educator ', dan_savage)
    guest_split_last('expert ', dan_savage)
    guest_split_last('activist ', dan_savage)
    guest_split_last('Professor ', dan_savage)
    guest_split_last('sensation ', dan_savage)
    guest_split_last('trailblazer ', dan_savage)
    guest_split_last('lawyer ', dan_savage)
    guest_split_last('co-founder ', dan_savage)
    guest_split_last('woman ', dan_savage)
    guest_split_last('columnist ', dan_savage)
    guest_split_last("MTV's", dan_savage)
    guest_split_last('star ', dan_savage)
    guest_split_last('super-freaky ', dan_savage)
    guest_split_last('luminary ', dan_savage)
    guest_split_last('with ', dan_savage)
    guest_split_last('fabulous ', dan_savage)
    guest_split_last('dominatrix ', dan_savage)

    replace("ex-muslim sex blogger and children's book author", 'Elynah', dan_savage)
    replace("identical twins", 'Tegan Rain Quin and Sara Keirsten Quin', dan_savage)
    replace('stoner', 'David Schmader', dan_savage)
    replace('the Queen', 'Panti Bliss', dan_savage)
    replace('the hilarious', 'Cameron Esposito', dan_savage)
    replace('the creators', 'Eric Klinenberg', dan_savage)
    replace('the lad', np.nan, dan_savage)


    dan_savage = dan_savage[pd.notnull(dan_savage['guests'])]
    dan_savage = splitDataFrameList(dan_savage, 'guests', ', and ')
    dan_savage = splitDataFrameList(dan_savage, 'guests', ', & ')
    dan_savage = splitDataFrameList(dan_savage, 'guests', ', ')
    dan_savage = splitDataFrameList(dan_savage, 'guests', ',')
    dan_savage = splitDataFrameList(dan_savage, 'guests', ' & ')
    dan_savage = splitDataFrameList(dan_savage, 'guests', ' And ')
    dan_savage = splitDataFrameList(dan_savage, 'guests', ' and ')

    replace('pro-dominatrix', 'Mistress Matisse', dan_savage)
    replace('Dan', np.nan, dan_savage)
    replace('the charming', np.nan, dan_savage)
    replace('writer', 'Parker Molloy', dan_savage)
    replace('the force', 'Lea Delaria', dan_savage)
    dan_savage = dan_savage[pd.notnull(dan_savage['guests'])]
    
    dan_savage = dan_savage[dan_savage.guests.str.contains(r'^a ') == False]
    dan_savage = dan_savage[dan_savage.guests.str.contains(r'^an ') == False]
    dan_savage = dan_savage[dan_savage.guests.str.contains(r'^and ') == False]
    dan_savage = dan_savage[dan_savage.guests.str.contains(r'the hosts') == False]

    dan_savage['guests'] = [g.rstrip() for g in dan_savage['guests']]
    dan_savage['guests'] = [g.rstrip(',') for g in dan_savage['guests']]
    dan_savage['guests'] = [g.rstrip() for g in dan_savage['guests']]
    dan_savage['guests'] = [g.rstrip('-') for g in dan_savage['guests']]
    
    dan_savage.replace('', np.nan, inplace=True)
    dan_savage = dan_savage[pd.notnull(dan_savage['guests'])]
    
    return dan_savage


def clean_tom_rhodes(tom_rhodes):

    tom_rhodes = xml_to_df(tom_rhodes)
        
    date_parser(tom_rhodes)
    
    tom_rhodes['guests'] = tom_rhodes['title']
    
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r'^\d+ ') == False]
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r'Smart Camp') == False]
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r'Happy ') == False]
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r'Comedy Notebook') == False]
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r'Movie ') == False]
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r'Post Oscars Chat') == False]
    tom_rhodes = tom_rhodes[tom_rhodes.guests.str.contains(r' For ') == False]
    
    guest_split_last(' with', tom_rhodes)
    guest_split(' reports', tom_rhodes)
    guest_split(' (', tom_rhodes)
    guest_split(r' \d+', tom_rhodes)
    guest_split(' 2', tom_rhodes)
    guest_split(' 3', tom_rhodes)
    guest_split(' 4', tom_rhodes)
    guest_split(' aka ', tom_rhodes)
    guest_split(' Part ', tom_rhodes)
    guest_split_last('Brother ', tom_rhodes)
    guest_split_last('by ', tom_rhodes)

    replace('A Criminal History Of Mankind', 'Colin Wilson', tom_rhodes)
    replace('His Purple Magesty', np.nan, tom_rhodes)
    
    tom_rhodes = tom_rhodes[pd.notnull(tom_rhodes['guests'])]
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ', and ')
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ', & ')
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ', ')
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ',')
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ' & ')
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ' And ')
    tom_rhodes = splitDataFrameList(tom_rhodes, 'guests', ' and ')

    tom_rhodes['guests'] = [g.rstrip('!') for g in tom_rhodes['guests']]
    tom_rhodes['guests'] = [g.rstrip() for g in tom_rhodes['guests']]
    
    return tom_rhodes


def clean_full_charge(full_charge):

    full_charge = xml_to_df(full_charge)
        
    date_parser(full_charge)
    
    full_charge['guests'] = full_charge.title.str.extract(r'(?:with |featuring )([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)

    guest_split('Episode 2', full_charge)

    
    full_charge = full_charge[pd.notnull(full_charge['guests'])]
    full_charge = splitDataFrameList(full_charge, 'guests', ', and ')
    full_charge = splitDataFrameList(full_charge, 'guests', ', & ')
    full_charge = splitDataFrameList(full_charge, 'guests', ', ')
    full_charge = splitDataFrameList(full_charge, 'guests', ',')
    full_charge = splitDataFrameList(full_charge, 'guests', ' & ')
    full_charge = splitDataFrameList(full_charge, 'guests', ' And ')
    full_charge = splitDataFrameList(full_charge, 'guests', ' and ')

    full_charge['guests'] = [g.rstrip('.') for g in full_charge['guests']]
    full_charge['guests'] = [g.rstrip() for g in full_charge['guests']]

    replace('Craig', np.nan, full_charge)
    replace('Wendell', np.nan, full_charge)
    replace('Josh O&#8217;Brien', "Josh O’Brien")

    guest_split(' The Party', full_charge)
    guest_split(' Part ', full_charge)
    
    full_charge.replace('', np.nan, inplace=True)
    full_charge = full_charge[pd.notnull(full_charge['guests'])]
    
    return full_charge


def clean_brandt_tobler(brandt_tobler):

    brandt_tobler = xml_to_df(brandt_tobler)
        
    date_parser(brandt_tobler)
    
    brandt_tobler['guests'] = brandt_tobler.title.str.extract(r'Episode \d+:?-? ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)

    guest_split(' Part', brandt_tobler)
    guest_split_last('Return of ', brandt_tobler)
    
    replace('The TURNER BROTHERS', 'The Turner Brothers', brandt_tobler)
    
    brandt_tobler = brandt_tobler[pd.notnull(brandt_tobler['guests'])]
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ', and ')
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ', & ')
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ', ')
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ',')
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ' & ')
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ' And ')
    brandt_tobler = splitDataFrameList(brandt_tobler, 'guests', ' and ')

    brandt_tobler['guests'] = [g.rstrip() for g in brandt_tobler['guests']]
    
    return brandt_tobler


def clean_steve_simeone(steve_simeone):

    steve_simeone = xml_to_df(steve_simeone)
        
    date_parser(steve_simeone)
    
    steve_simeone['guests'] = steve_simeone.title.str.extract(r'\#\d+ - ([\w\s\.\,\'\`\’\&\"\-\‘]+) - Good',expand=True)

    steve_simeone = steve_simeone[steve_simeone.guests.str.contains(r'Special') == False]
    steve_simeone = steve_simeone[steve_simeone.guests.str.contains(r' for ') == False]

    replace('Steve and Lee Hang Out', 'Lee Syatt', steve_simeone)
    
    steve_simeone = steve_simeone[pd.notnull(steve_simeone['guests'])]
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ', and ')
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ', & ')
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ', ')
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ',')
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ' & ')
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ' And ')
    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ' and ')

    guest_split_last('Coach ', steve_simeone)
    replace('Steven Brody Stevens', 'Brody Stevens', steve_simeone)
    replace("Children's Hospital", 'Raul Gonzalez and Hector Pulido', steve_simeone)

    steve_simeone = splitDataFrameList(steve_simeone, 'guests', ' and ')

    steve_simeone = steve_simeone[steve_simeone.guests.str.contains(r'Family') == False]
    steve_simeone = steve_simeone[steve_simeone.guests.str.contains(r'Thank you Mitzi') == False]
    steve_simeone = steve_simeone[steve_simeone.guests.str.contains(r'Happy') == False]

    steve_simeone['guests'] = [g.rstrip() for g in steve_simeone['guests']]
    
    return steve_simeone


def clean_johnny_pemberton(johnny_pemberton):

    johnny_pemberton = xml_to_df(johnny_pemberton)
        
    date_parser(johnny_pemberton)
    
    johnny_pemberton['guests'] = johnny_pemberton.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-\‘]+)',expand=True)

    for index, row in johnny_pemberton.iterrows():
        if(pd.notnull(row['guests'])):
            johnny_pemberton.at[index, 'guests'] = row['guests'].title()
    
    guest_split(' -', johnny_pemberton)
    
    replace('Ryan And Jess', 'Ryan Nassichuk and Jessica Hammersmark', johnny_pemberton)
    replace('Fadem, Brown, Cregger, And Moore', 'Josh Fadem, Sam Brown, Zach Cregger, And Trevor Moore', johnny_pemberton)
    replace('Whit & Clay', 'Clay Tatum and Whitmer Thomas', johnny_pemberton)
    replace('Randy L. And Brendon W.', 'Brendon Walsh and Randy Liedtke', johnny_pemberton)
    replace('Mikey And Adam', 'Mikey Kampmann and Adam Forkner', johnny_pemberton)
    replace('Brendon And Randy', 'Randy Liedtke and Brendon Walsh', johnny_pemberton)
    replace('The Walsh Brothers', 'Dave Walsh, Chris Walsh', johnny_pemberton)
    replace('Phil & Steve', np.nan, johnny_pemberton)
    
    johnny_pemberton = johnny_pemberton[johnny_pemberton.guests.str.contains(r'A Boot') == False]
    
    johnny_pemberton = johnny_pemberton[pd.notnull(johnny_pemberton['guests'])]
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ', and ')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ', And ')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ', & ')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ', ')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ',')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ' & ')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ' And ')
    johnny_pemberton = splitDataFrameList(johnny_pemberton, 'guests', ' and ')

    johnny_pemberton['guests'] = [g.rstrip() for g in johnny_pemberton['guests']]
    
    return johnny_pemberton


def clean_live_to_tape(live_to_tape):

    live_to_tape = xml_to_df(live_to_tape)
        
    date_parser(live_to_tape)
    
    live_to_tape['guests'] = live_to_tape['title']
    
    guest_split(' -', live_to_tape)
    guest_split(': ', live_to_tape)

    guest_split_last(' returns', live_to_tape)

    replace('Brendon and Randy ', 'Randy Liedtke and Brendon Walsh', live_to_tape)
    replace('Swamp Dogg', 'Jerry Williams Jr.', live_to_tape)
    
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'CA') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'tribute') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'BALLS') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'SCOOP') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'who ') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'no.') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'Mom') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'ON') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'BABY') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'YACHT') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'Xmas') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'Update') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'A.L.E.') == False]
    live_to_tape = live_to_tape[live_to_tape.guests.str.contains(r'TRENCH') == False]
    
    live_to_tape = live_to_tape[pd.notnull(live_to_tape['guests'])]
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ', and ')
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ', & ')
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ', ')
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ',')
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ' & ')
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ' And ')
    live_to_tape = splitDataFrameList(live_to_tape, 'guests', ' and ')

    live_to_tape['guests'] = [g.rstrip() for g in live_to_tape['guests']]
    
    return live_to_tape


def clean_jay_mohr(jay_mohr):

    jay_mohr = xml_to_df(jay_mohr)
        
    date_parser(jay_mohr)
    
    jay_mohr['guests'] = jay_mohr.title.str.extract(r'\d+: ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)

    replace('Randy and Jason Sklar', 'Randy Sklar and Jason Sklar', jay_mohr)
    
    jay_mohr = jay_mohr[pd.notnull(jay_mohr['guests'])]
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ', and ')
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ', & ')
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ', ')
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ',')
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ' & ')
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ' And ')
    jay_mohr = splitDataFrameList(jay_mohr, 'guests', ' and ')

    jay_mohr = jay_mohr[jay_mohr.guests.str.contains(r' Your ') == False]
    jay_mohr = jay_mohr[jay_mohr.guests.str.contains(r'Comedy') == False]

    jay_mohr['guests'] = [g.rstrip() for g in jay_mohr['guests']]
    
    return jay_mohr


def clean_pony_hour(pony_hour):

    pony_hour = xml_to_df(pony_hour)
        
    date_parser(pony_hour)
    
    pony_hour['guests'] = pony_hour['title']  #.str.extract(r'\d+: ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    replace('The Mean Boys', 'Connor Mcspadden & Keith Carey', pony_hour)
    
    pony_hour = pony_hour[pd.notnull(pony_hour['guests'])]
    pony_hour = splitDataFrameList(pony_hour, 'guests', ', and ')
    pony_hour = splitDataFrameList(pony_hour, 'guests', ', & ')
    pony_hour = splitDataFrameList(pony_hour, 'guests', ', ')
    pony_hour = splitDataFrameList(pony_hour, 'guests', ',')
    pony_hour = splitDataFrameList(pony_hour, 'guests', ' & ')
    pony_hour = splitDataFrameList(pony_hour, 'guests', ' And ')
    pony_hour = splitDataFrameList(pony_hour, 'guests', ' and ')

    pony_hour['guests'] = [g.rstrip() for g in pony_hour['guests']]
    
    return pony_hour


def clean_jocko(jocko):

    jocko = xml_to_df(jocko)
    
    jocko['episode'] = jocko.title.str.extract(r'(\d+): ',expand=True)
        
    date_parser(jocko)
    
    jocko['guests'] = jocko.title.str.extract(r'(?:[Ww]ith |by )([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split('.  ', jocko)
    guest_split(', US ', jocko)
    
    guest_split_last('Recipient, ', jocko)
    guest_split_last('Pilot, ', jocko)
    guest_split_last('Marine Corporal, ', jocko)
    guest_split_last('Capt. ', jocko)
    guest_split_last('Colonel ', jocko)
    guest_split_last('Col. ', jocko)
    guest_split_last('CWO ', jocko)
    replace('Lewis Puller Jr', 'Lewis Puller Jr.', jocko)
    
    
    for index, row in jocko.iterrows():
        if(row['episode']=='108'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='107'):
            jocko.at[index, 'guests'] = 'Hal Moore'
        if(row['episode']=='98'):
            jocko.at[index, 'guests'] = 'Jordan Peterson'
        if(row['episode']=='97'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='99'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='96'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='93'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='61'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='55'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='54'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='48'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='44'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='30'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='41'):
            jocko.at[index, 'guests'] = 'Tony Eafrati'
        if(row['episode']=='42'):
            jocko.at[index, 'guests'] = 'Andrew Paul'
        if(row['episode']=='37'):
            jocko.at[index, 'guests'] = 'Roger Hayden'
        if(row['episode']=='36'):
            jocko.at[index, 'guests'] = 'Kieran Doherty'
        if(row['episode']=='34'):
            jocko.at[index, 'guests'] = 'Leif Babin'
        if(row['episode']=='25'):
            jocko.at[index, 'guests'] = 'Jody Mitic'
        if(row['episode']=='24'):
            jocko.at[index, 'guests'] = 'Jody Mitic'
        if(row['episode']=='21'):
            jocko.at[index, 'guests'] = 'Tim Kennedy'
        if(row['episode']=='10'):
            jocko.at[index, 'guests'] = np.nan
        if(row['episode']=='4'):
            jocko.at[index, 'guests'] = np.nan
    
    jocko = jocko[pd.notnull(jocko['guests'])]

    jocko['guests'] = [g.rstrip('.') for g in jocko['guests']]
    jocko['guests'] = [g.rstrip() for g in jocko['guests']]

    return jocko


def clean_tim_ferriss(tim_ferriss):

    tim_ferriss = xml_to_df_summ(tim_ferriss)

    tim_ferriss.replace(u"\u00A0", " ", regex=True, inplace=True)
    
    ## Set Episode numbers
    
    tim_ferriss['episode'] = len(tim_ferriss) - tim_ferriss.index
    
    date_parser(tim_ferriss)
    
    tim_ferriss['guests'] = tim_ferriss['summary']
    tim_ferriss.drop('summary', 1, inplace=True)
    
    guest_split(' is ', tim_ferriss)
    guest_split(r' (@', tim_ferriss)
    guest_split(r'(@', tim_ferriss)
    guest_split(r' (IG', tim_ferriss)
    guest_split(' has ', tim_ferriss)
    guest_split(' was ', tim_ferriss)
    guest_split(', who ', tim_ferriss)
    guest_split('. We all ', tim_ferriss)
    guest_split(' built his ', tim_ferriss)
    guest_split(', MD', tim_ferriss)
    
    guest_split_last('guest is ', tim_ferriss)
    guest_split_last('guests: ', tim_ferriss)
    guest_split_last('features', tim_ferriss)
    guest_split_last(' 3.', tim_ferriss)
    guest_split_last(' 2.', tim_ferriss)
    guest_split_last('\n', tim_ferriss)
    guest_split_last('2 of 2 ', tim_ferriss)
    guest_split_last('Yes, ', tim_ferriss)
    guest_split_last('then ', tim_ferriss)
    
    replace('Mike Maples, Jr.', 'Mike Maples Jr.', tim_ferriss)
    replace('"War', 'Rolf Potts', tim_ferriss)
    replace('The guest', 'Daniel Pink', tim_ferriss)
    replace('this', np.nan, tim_ferriss)
    
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'This') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r' this ') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'tribal ') == False]
    
    tim_ferriss = tim_ferriss[pd.notnull(tim_ferriss['guests'])]
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ', and ')
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ', & ')
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ', ')
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ',')
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ' & ')
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ' And ')
    tim_ferriss = splitDataFrameList(tim_ferriss, 'guests', ' and ')

    tim_ferriss['guests'] = [g.rstrip() for g in tim_ferriss['guests']]
    tim_ferriss['guests'] = [g.lstrip() for g in tim_ferriss['guests']]

    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'PHD') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'Ph.D.') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'My guest') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'"My lab') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'"The answer') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'My job') == False]
    tim_ferriss = tim_ferriss[tim_ferriss.guests.str.contains(r'When a guest') == False]

    replace('Mr. Money Mustache', 'Pete Adeney', tim_ferriss)
    replace('Cal', 'Cal Fussman', tim_ferriss)
    replace('Links', 'Arnold Schwarzenegger', tim_ferriss)
    replace('By popular demand', 'Pavel Tsatsouline', tim_ferriss)

    guest_split_last('Dr. ', tim_ferriss)
    guest_split('. He', tim_ferriss)

    replace('here', np.nan, tim_ferriss)
    replace('this', np.nan, tim_ferriss)
    tim_ferriss = tim_ferriss[pd.notnull(tim_ferriss['guests'])]
    
    tim_ferriss = tim_ferriss[tim_ferriss['guests'].str.len() < 22]
    tim_ferriss = tim_ferriss[tim_ferriss['duration'] > 1350]
    
    return tim_ferriss


def clean_star_talk(star_talk):

    star_talk = xml_to_df(star_talk)
        
    date_parser(star_talk)
    
    star_talk['guests'] = star_talk.title.str.extract(r'with ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(' - ', star_talk)
    
    guest_split_last('Medalists ', star_talk)
    guest_split_last('Medalist ', star_talk)
    guest_split_last('Olympians ', star_talk)
    guest_split_last('Astro ', star_talk)
    guest_split_last('Legend ', star_talk)
    guest_split_last('with ', star_talk)
    
    replace('God', np.nan, star_talk)
    
    star_talk = star_talk[star_talk.guests.str.contains(r' Time ') == False]
    star_talk = star_talk[star_talk.guests.str.contains(r'Science') == False]
    star_talk = star_talk[star_talk.guests.str.contains(r'Revisited') == False]
    
    star_talk = star_talk[pd.notnull(star_talk['guests'])]
    star_talk = splitDataFrameList(star_talk, 'guests', ', and ')
    star_talk = splitDataFrameList(star_talk, 'guests', ', & ')
    star_talk = splitDataFrameList(star_talk, 'guests', ', ')
    star_talk = splitDataFrameList(star_talk, 'guests', ',')
    star_talk = splitDataFrameList(star_talk, 'guests', ' & ')
    star_talk = splitDataFrameList(star_talk, 'guests', ' And ')
    star_talk = splitDataFrameList(star_talk, 'guests', ' and ')
    
    replace('Penn', 'Penn Jillette', star_talk)
    replace('Teller', 'Raymond Teller', star_talk)
    replace('Dr. Skateboard', 'Dr. Bill Robertson', star_talk)

    star_talk['guests'] = [g.rstrip() for g in star_talk['guests']]
    
    return star_talk


def clean_doug_stanhope(doug_stanhope):

    doug_stanhope = xml_to_df_desc(doug_stanhope)
    
    doug_stanhope.replace(u"\u00A0", " ", regex=True, inplace=True)
        
    date_parser(doug_stanhope)
    
    doug_stanhope['guests'] = doug_stanhope.description.str.extract(r'with Doug Stanhope \(@DougStanhope\), ([\w\s\.\,\'\`\’\&\"\-\(\)\@]+) \(',expand=True)
    doug_stanhope.drop('description', 1, inplace=True)
    
    doug_stanhope = doug_stanhope[pd.notnull(doug_stanhope['guests'])]
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ', and ')
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ', & ')
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ', ')
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ',')
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ' & ')
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ' And ')
    doug_stanhope = splitDataFrameList(doug_stanhope, 'guests', ' and ')
    
    guest_split(r' (@', doug_stanhope)
    guest_split(r' ( @', doug_stanhope)
    guest_split(r'. ', doug_stanhope)
    guest_split(r' from', doug_stanhope)
    
    guest_split_last('& ', doug_stanhope)
    guest_split_last('author ', doug_stanhope)
    guest_split_last('comedian ', doug_stanhope)
    
    replace('Jobi', 'Jobi Whitlock', doug_stanhope)
    replace('Ggreg Chaille', 'Greg Chaille', doug_stanhope)
    
    doug_stanhope = doug_stanhope[doug_stanhope.guests.str.contains(r'Edited ') == False]
    doug_stanhope = doug_stanhope[doug_stanhope.guests.str.contains(r' the ') == False]
    doug_stanhope = doug_stanhope[doug_stanhope.guests.str.contains(r' Cut ') == False]

    doug_stanhope = doug_stanhope[doug_stanhope.guests.str.contains(r'Mom') == False]

    doug_stanhope['guests'] = [g.rstrip() for g in doug_stanhope['guests']]
    
    return doug_stanhope


def clean_bitch_sesh(bitch_sesh):

    bitch_sesh = xml_to_df(bitch_sesh)
        
    date_parser(bitch_sesh)
    
    bitch_sesh['guests'] = bitch_sesh.title.str.extract(r'w\/ ([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    bitch_sesh = bitch_sesh[pd.notnull(bitch_sesh['guests'])]
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ', and ')
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ', & ')
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ', ')
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ',')
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ' & ')
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ' And ')
    bitch_sesh = splitDataFrameList(bitch_sesh, 'guests', ' and ')

    bitch_sesh['guests'] = [g.rstrip() for g in bitch_sesh['guests']]
    
    return bitch_sesh


def clean_cam_rhea(cam_rhea):

    cam_rhea = xml_to_df(cam_rhea)
        
    date_parser(cam_rhea)
    
    cam_rhea['guests'] = cam_rhea.title.str.extract(r'([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)
    
    guest_split(' and host', cam_rhea)
    
    cam_rhea = cam_rhea[pd.notnull(cam_rhea['guests'])]
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ', and ')
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ', & ')
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ', ')
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ',')
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ' & ')
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ' And ')
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ' and ')

    replace('Paul F. Tompkins as "Cake Boss," Rory Scovel', 'Paul F. Tompkins, Rory Scovel', cam_rhea)
    replace('The Sklar Brothers', 'Jason Sklar, Randy Sklar', cam_rhea)
    replace('The Walsh Brothers', 'Dave Walsh, Chris Walsh', cam_rhea)
    cam_rhea = splitDataFrameList(cam_rhea, 'guests', ', ')

    cam_rhea['guests'] = [g.rstrip() for g in cam_rhea['guests']]
    
    return cam_rhea


def clean_snoop(snoop):

    snoop = xml_to_df(snoop)
        
    date_parser(snoop)
    
    snoop['guests'] = snoop.title.str.extract(r'Ep. \d+ - ([\w\s\.\,\'\`\’\&\"\-\$]+)',expand=True)
    
    snoop = snoop[pd.notnull(snoop['guests'])]
    snoop = splitDataFrameList(snoop, 'guests', ', and ')
    snoop = splitDataFrameList(snoop, 'guests', ', & ')
    snoop = splitDataFrameList(snoop, 'guests', ', ')
    snoop = splitDataFrameList(snoop, 'guests', ',')
    snoop = splitDataFrameList(snoop, 'guests', ' & ')
    snoop = splitDataFrameList(snoop, 'guests', ' And ')
    snoop = splitDataFrameList(snoop, 'guests', ' and ')

    replace("Key", 'Keegan-Michael Key', snoop)
    replace('Peele', 'Jordan Peele', snoop)
    replace('Pharrell', 'Pharrell Williams', snoop)

    replace('Cheech', 'Cheech Marin', snoop)
    replace('Chong', 'Tommy Chong', snoop)
    
    snoop = snoop[snoop.guests.str.contains(r'Special') == False]

    snoop['guests'] = [g.rstrip() for g in snoop['guests']]
    
    return snoop


def clean_andy_cohen(andy_cohen):

    andy_cohen = xml_to_df(andy_cohen)
        
    date_parser(andy_cohen)
    
    andy_cohen['guests'] = andy_cohen.title.str.extract(r'(?:[\d\/] [-–] )?([^\d^\/]+)(?: [-–] [\d\/])?',expand=True)

    guest_split(' (', andy_cohen)
    guest_split(' - ', andy_cohen)
    
    andy_cohen = andy_cohen[pd.notnull(andy_cohen['guests'])]
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ', and ')
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ', & ')
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ', ')
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ',')
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ' & ')
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ' And ')
    andy_cohen = splitDataFrameList(andy_cohen, 'guests', ' and ')
    
    andy_cohen = andy_cohen[andy_cohen.guests.str.contains(r'the N') == False]
    andy_cohen = andy_cohen[andy_cohen.guests.str.contains(r'Special') == False]
    andy_cohen = andy_cohen[andy_cohen.guests.str.contains(r' Live') == False]
    andy_cohen = andy_cohen[andy_cohen.guests.str.contains(r' Cast') == False]
    
    andy_cohen['guests'] = [g.rstrip() for g in andy_cohen['guests']]
    
    return andy_cohen


def clean_rap_radar(rap_radar):

    rap_radar = xml_to_df(rap_radar)
        
    date_parser(rap_radar)
    
    rap_radar['guests'] = rap_radar.title.str.extract(r'E[Pp] \d+: ([\w\s\.\,\'\`\’\&\"\-\$]+)',expand=True)
    
    replace('The Breakfast Club', 'DJ Envy, Angela Yee, Charlamagne Tha God', rap_radar)
    
    rap_radar = rap_radar[pd.notnull(rap_radar['guests'])]
    rap_radar = splitDataFrameList(rap_radar, 'guests', ', and ')
    rap_radar = splitDataFrameList(rap_radar, 'guests', ', & ')
    rap_radar = splitDataFrameList(rap_radar, 'guests', ', ')
    rap_radar = splitDataFrameList(rap_radar, 'guests', ',')
    rap_radar = splitDataFrameList(rap_radar, 'guests', ' & ')
    rap_radar = splitDataFrameList(rap_radar, 'guests', ' And ')
    rap_radar = splitDataFrameList(rap_radar, 'guests', ' and ')

    rap_radar['guests'] = [g.rstrip() for g in rap_radar['guests']]
    
    return rap_radar


def clean_vlad_couch(vlad_couch):

    vlad_couch = xml_to_df(vlad_couch)
        
    date_parser(vlad_couch)
    
    vlad_couch['guests'] = vlad_couch.title.str.extract(r'([^(]+)',expand=True)
    
    guest_split(' of ', vlad_couch)
    guest_split(' Talks ', vlad_couch)
    guest_split("writer' ", vlad_couch)
    
    vlad_couch = vlad_couch[vlad_couch.guests.str.contains(r' Details ') == False]
    
    vlad_couch = vlad_couch[pd.notnull(vlad_couch['guests'])]
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ', and ')
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ', & ')
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ', ')
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ',')
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ' & ')
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ' And ')
    vlad_couch = splitDataFrameList(vlad_couch, 'guests', ' and ')

    vlad_couch['guests'] = [g.rstrip() for g in vlad_couch['guests']]
    
    replace('Charlamagne', 'Charlamagne Tha God', vlad_couch)
    
    return vlad_couch


def clean_allegedly(allegedly):

    allegedly = xml_to_df(allegedly)
        
    date_parser(allegedly)
    
    allegedly['guests'] = allegedly['title']  #.title.str.extract(r'([^(]+)',expand=True)

    guest_split_last('"', allegedly)
    
    allegedly = allegedly[allegedly.guests.str.contains(r'Best Of ') == False]
    
    allegedly = allegedly[pd.notnull(allegedly['guests'])]
    allegedly = splitDataFrameList(allegedly, 'guests', ', and ')
    allegedly = splitDataFrameList(allegedly, 'guests', ', & ')
    allegedly = splitDataFrameList(allegedly, 'guests', ', ')
    allegedly = splitDataFrameList(allegedly, 'guests', ',')
    allegedly = splitDataFrameList(allegedly, 'guests', ' & ')
    allegedly = splitDataFrameList(allegedly, 'guests', ' And ')
    allegedly = splitDataFrameList(allegedly, 'guests', ' and ')

    allegedly['guests'] = [g.rstrip() for g in allegedly['guests']]
    
    return allegedly


def clean_this_life(this_life):

    this_life = xml_to_df(this_life)
        
    date_parser(this_life)
    
    this_life['guests'] = this_life.title.str.extract(r'\d+(?:\s?: | - )([^(]+)',expand=True)
    
    guest_split(' Returns', this_life)
    guest_split(' VS. PTSD', this_life)
    guest_split(' PTSD', this_life)
    guest_split(' Talks', this_life)
    
    guest_split_last(' - ', this_life)
    guest_split_last('With ', this_life)
    guest_split_last('Soberoctobert ', this_life)
    guest_split_last('Interventionist ', this_life)
    
    this_life = this_life[this_life.guests.str.contains(r'This ') == False]
    this_life = this_life[this_life.guests.str.contains(r'Facing ') == False]
    this_life = this_life[this_life.guests.str.contains(r'At The ') == False]
    this_life = this_life[this_life.guests.str.contains(r' Guys') == False]
    
    this_life = this_life[pd.notnull(this_life['guests'])]
    this_life = splitDataFrameList(this_life, 'guests', ', and ')
    this_life = splitDataFrameList(this_life, 'guests', ', & ')
    this_life = splitDataFrameList(this_life, 'guests', ', ')
    this_life = splitDataFrameList(this_life, 'guests', ',')
    this_life = splitDataFrameList(this_life, 'guests', ' & ')
    this_life = splitDataFrameList(this_life, 'guests', ' And ')
    this_life = splitDataFrameList(this_life, 'guests', ' and ')
    this_life = splitDataFrameList(this_life, 'guests', ' / ')
    this_life = splitDataFrameList(this_life, 'guests', ' /')
    this_life = splitDataFrameList(this_life, 'guests', ' Meets ')

    this_life['guests'] = [g.rstrip() for g in this_life['guests']]
    
    replace('Emily', 'Emily Morse', this_life)
    replace('Christina P', 'Christina Pazsitzky', this_life)
    
    return this_life


def clean_friends_like_these(friends_like_these):

    friends_like_these = xml_to_df(friends_like_these)
        
    date_parser(friends_like_these)
    
    friends_like_these['guests'] = friends_like_these['title']  #.title.str.extract(r'(?:\"[^\"]+\"\s)(?:w\/ |with )([^(]+)',expand=True)
    
    guest_split_last('with ', friends_like_these)
    guest_split_last('w/ ', friends_like_these)
    
    guest_split('"', friends_like_these)
    guest_split('“', friends_like_these)
    
    friends_like_these.replace('', np.nan, inplace=True)
    
    friends_like_these = friends_like_these[friends_like_these.guests.str.contains(r'Episode') == False]
    friends_like_these = friends_like_these[friends_like_these.guests.str.contains(r'EPISODE') == False]
    friends_like_these = friends_like_these[friends_like_these.guests.str.contains(r'Special') == False]
    friends_like_these = friends_like_these[friends_like_these.guests.str.contains(r'pitchforks') == False]
    friends_like_these = friends_like_these[friends_like_these.guests.str.contains(r' a ') == False]
    
    friends_like_these = friends_like_these[pd.notnull(friends_like_these['guests'])]
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ', and ')
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ', & ')
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ', ')
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ',')
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ' & ')
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ' And ')
    friends_like_these = splitDataFrameList(friends_like_these, 'guests', ' and ')

    friends_like_these['guests'] = [g.rstrip() for g in friends_like_these['guests']]
    
    return friends_like_these


def clean_axe_files(axe_files):

    axe_files = xml_to_df(axe_files)
        
    date_parser(axe_files)
    
    axe_files['guests'] = axe_files.title.str.extract(r'Ep. \d+ - ([^(]+)',expand=True)
    
    axe_files = axe_files[pd.notnull(axe_files['guests'])]

    replace('SE Cupp', 'S.E. Cupp', axe_files)

    axe_files['guests'] = [g.rstrip() for g in axe_files['guests']]
    
    return axe_files


def clean_politically_reactive(politically_reactive):

    politically_reactive = xml_to_df(politically_reactive)
        
    date_parser(politically_reactive)
    
    politically_reactive['guests1'] = politically_reactive.title.str.extract(r'([\w\s\.\,\'\`\’\&\"\-\$]+) on ',expand=True)
    politically_reactive['guests2'] = politically_reactive.title.str.extract(r' with ([\w\s\.\,\'\`\’\&\"\-\$]+)',expand=True)

    politically_reactive.replace(np.nan, '', regex=True, inplace=True)
    politically_reactive['guests'] = politically_reactive['guests1'] + politically_reactive['guests2']  
    politically_reactive = politically_reactive.drop('guests1', 1)
    politically_reactive = politically_reactive.drop('guests2', 1)
    politically_reactive.replace('', np.nan, regex=True, inplace=True)
    
    guest_split(' of ', politically_reactive)

    guest_split_last('Journalist ', politically_reactive)
    guest_split_last("YouTube's ", politically_reactive)
    guest_split_last("CNN’s ", politically_reactive)
    guest_split_last('Comedian ', politically_reactive)
    
    for index, row in politically_reactive.iterrows():
        if(pd.notnull(row['guests'])):
            politically_reactive.at[index, 'guests'] = row['guests'].title()
    
    politically_reactive = politically_reactive[politically_reactive.guests.str.contains(r'Truth ') == False]
    
    politically_reactive = politically_reactive[pd.notnull(politically_reactive['guests'])]
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ', and ')
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ', & ')
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ', ')
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ',')
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ' & ')
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ' And ')
    politically_reactive = splitDataFrameList(politically_reactive, 'guests', ' and ')

    politically_reactive['guests'] = [g.rstrip() for g in politically_reactive['guests']]

    replace('S. E. Cupp', 'S.E. Cupp', politically_reactive)
    
    politically_reactive = politically_reactive[politically_reactive.guests.str.contains(r'Talking ') == False]
    politically_reactive = politically_reactive[politically_reactive.guests.str.contains(r' The ') == False]
    
    return politically_reactive


def clean_james_altucher(james_altucher):

    james_altucher = xml_to_df(james_altucher)
        
    date_parser(james_altucher)
    
    james_altucher['guests'] = james_altucher.title.str.extract(r'\d+ - ([^(]+): ',expand=True)
    
    guest_split(': ', james_altucher)
    guest_split(' - ', james_altucher)
    guest_split(' [', james_altucher)
    
    james_altucher = james_altucher[james_altucher.guests.str.contains(r'Anxiety') == False]
    
    james_altucher = james_altucher[pd.notnull(james_altucher['guests'])]
    james_altucher = splitDataFrameList(james_altucher, 'guests', ', and ')
    james_altucher = splitDataFrameList(james_altucher, 'guests', ', & ')
    james_altucher = splitDataFrameList(james_altucher, 'guests', ', ')
    james_altucher = splitDataFrameList(james_altucher, 'guests', ',')
    james_altucher = splitDataFrameList(james_altucher, 'guests', ' & ')
    james_altucher = splitDataFrameList(james_altucher, 'guests', ' And ')
    james_altucher = splitDataFrameList(james_altucher, 'guests', ' and ')

    james_altucher['guests'] = [g.rstrip() for g in james_altucher['guests']]
    
    return james_altucher


def clean_bulletproof_radio(bulletproof_radio):

    bulletproof_radio = xml_to_df(bulletproof_radio)
        
    date_parser(bulletproof_radio)
    
    bulletproof_radio['guests'] = bulletproof_radio.title.str.extract(r'(?: [Ww]ith | - )([^(]+)',expand=True)
    
    guest_split('#', bulletproof_radio)
    guest_split(', Ph.D', bulletproof_radio)
    guest_split(', MD', bulletproof_radio)
    guest_split_last('," ', bulletproof_radio)
    guest_split_last('! ', bulletproof_radio)
    
    guest_split_last(' - ', bulletproof_radio)
    guest_split_last('with ', bulletproof_radio)
    
    guest_split(' -', bulletproof_radio)
    guest_split_last(' – ', bulletproof_radio)
    
    replace('Jayson & Mira Calton', 'Jayson Calton & Mira Calton', bulletproof_radio)
    replace('Mira & Jayson Calton', 'Jayson Calton & Mira Calton', bulletproof_radio)
    replace('The Bare Minimum From NY Times Best-Selling Author  James Altucher ', 'James Altucher', bulletproof_radio)
    
    bulletproof_radio.replace('', np.nan, regex=True, inplace=True)
    bulletproof_radio.replace('', np.nan, regex=True, inplace=True)
    
    bulletproof_radio = bulletproof_radio[bulletproof_radio.guests.str.contains(r' Oil') == False]
    
    bulletproof_radio = bulletproof_radio[pd.notnull(bulletproof_radio['guests'])]
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ', and ')
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ', & ')
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ', ')
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ',')
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ' & ')
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ' And ')
    bulletproof_radio = splitDataFrameList(bulletproof_radio, 'guests', ' and ')

    bulletproof_radio['guests'] = [g.rstrip() for g in bulletproof_radio['guests']]
    bulletproof_radio['guests'] = [g.rstrip('.') for g in bulletproof_radio['guests']]

    bulletproof_radio.replace('', np.nan, regex=True, inplace=True)
    bulletproof_radio = bulletproof_radio[pd.notnull(bulletproof_radio['guests'])]
    
    return bulletproof_radio


def clean_chris_kresser(chris_kresser):

    chris_kresser = xml_to_df(chris_kresser)
        
    date_parser(chris_kresser)
    
    chris_kresser['guests'] = chris_kresser.title.str.extract(r'[Ww]ith ([^(]+)',expand=True)
    
    guest_split_last('with ', chris_kresser)
    
    chris_kresser = chris_kresser[chris_kresser.guests.str.contains(r' the ') == False]
    
    chris_kresser = chris_kresser[pd.notnull(chris_kresser['guests'])]
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ', and ')
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ', & ')
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ', ')
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ',')
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ' & ')
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ' And ')
    chris_kresser = splitDataFrameList(chris_kresser, 'guests', ' and ')

    chris_kresser['guests'] = [g.rstrip() for g in chris_kresser['guests']]
    
    return chris_kresser


def clean_ufc_unfiltered(ufc_unfiltered):

    ufc_unfiltered = xml_to_df(ufc_unfiltered)
        
    date_parser(ufc_unfiltered)
    
    ufc_unfiltered['guests'] = ufc_unfiltered.title.str.extract(r'UF\d+: ([^(]+)',expand=True)
    
    guest_split(' Talks', ufc_unfiltered)
    guest_split(' Sounds', ufc_unfiltered)
    guest_split(' Joins', ufc_unfiltered)
    guest_split(' Is ', ufc_unfiltered)
    guest_split(' on ', ufc_unfiltered)
    guest_split(' Fights', ufc_unfiltered)
    guest_split(' Predicts', ufc_unfiltered)
    guest_split(' Finds', ufc_unfiltered)
    guest_split(' Discusses', ufc_unfiltered)
    guest_split(' Says', ufc_unfiltered)
    guest_split(' Taps', ufc_unfiltered)
    guest_split(' Sets', ufc_unfiltered)
    guest_split(' Feels', ufc_unfiltered)
    guest_split(' In-', ufc_unfiltered)
    guest_split(' Loves', ufc_unfiltered)
    
    guest_split_last('with ', ufc_unfiltered)
    guest_split_last('The Great ', ufc_unfiltered)
    
    replace('Roy Jones, Jr.', 'Roy Jones Jr.', ufc_unfiltered)
    
    ufc_unfiltered = ufc_unfiltered[pd.notnull(ufc_unfiltered['guests'])]
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ', and ')
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ', & ')
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ', ')
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ',')
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ' & ')
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ' And ')
    ufc_unfiltered = splitDataFrameList(ufc_unfiltered, 'guests', ' and ')

    ufc_unfiltered['guests'] = [g.rstrip() for g in ufc_unfiltered['guests']]
    
    ufc_unfiltered = ufc_unfiltered[ufc_unfiltered.guests.str.contains(r'UFC') == False]
    
    return ufc_unfiltered


def clean_dan_harris(dan_harris):

    dan_harris = xml_to_df(dan_harris)
        
    date_parser(dan_harris)
    
    dan_harris['guests'] = dan_harris.title.str.extract(r'\#\d+: ([^(]+)',expand=True)
    
    guest_split(', ', dan_harris)
    
    dan_harris = dan_harris[dan_harris.guests.str.contains(r'Your ') == False]
    
    dan_harris = dan_harris[pd.notnull(dan_harris['guests'])]
    dan_harris = splitDataFrameList(dan_harris, 'guests', ', and ')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ', & ')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ', ')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ',')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ' &amp; ')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ' & ')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ' And ')
    dan_harris = splitDataFrameList(dan_harris, 'guests', ' and ')

    dan_harris['guests'] = [g.rstrip() for g in dan_harris['guests']]
    
    return dan_harris


def clean_supersoul(supersoul):

    supersoul = xml_to_df(supersoul)
        
    date_parser(supersoul)
    
    supersoul['guests'] = supersoul.title.str.extract(r'([^:]+): ',expand=True)
    
    guest_split(', Part', supersoul)
    guest_split(' Part', supersoul)
    
    guest_split_last('The ', supersoul)
    
    replace('India.Arie', 'India Arie', supersoul)
    replace('RuPaul Charles', 'RuPaul', supersoul)
    
    supersoul = supersoul[supersoul.guests.str.contains(r'Your ') == False]
    supersoul = supersoul[supersoul.guests.str.contains(r' the ') == False]
    
    supersoul = supersoul[pd.notnull(supersoul['guests'])]
    supersoul = splitDataFrameList(supersoul, 'guests', ', and ')
    supersoul = splitDataFrameList(supersoul, 'guests', ', & ')
    supersoul = splitDataFrameList(supersoul, 'guests', ', ')
    supersoul = splitDataFrameList(supersoul, 'guests', ',')
    supersoul = splitDataFrameList(supersoul, 'guests', ' &amp; ')
    supersoul = splitDataFrameList(supersoul, 'guests', ' & ')
    supersoul = splitDataFrameList(supersoul, 'guests', ' And ')
    supersoul = splitDataFrameList(supersoul, 'guests', ' and ')

    supersoul = supersoul[supersoul.guests.str.contains(r'New ') == False]

    supersoul['guests'] = [g.rstrip() for g in supersoul['guests']]
    
    return supersoul


def clean_conv_tyler(conv_tyler):

    conv_tyler = xml_to_df(conv_tyler)

    date_parser(conv_tyler)
    
    conv_tyler['guests'] = conv_tyler.title.str.extract(r' - ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    guest_split(' on ', conv_tyler)
    guest_split(' talk ', conv_tyler)
    guest_split(' has ', conv_tyler)
    guest_split(' Wants ', conv_tyler)
    guest_split(' Live ', conv_tyler)
    
    conv_tyler = conv_tyler[pd.notnull(conv_tyler['guests'])]
    conv_tyler = splitDataFrameList(conv_tyler, 'guests', ', and ')
    conv_tyler = splitDataFrameList(conv_tyler, 'guests', ', ')
    conv_tyler = splitDataFrameList(conv_tyler, 'guests', ' & ')
    conv_tyler = splitDataFrameList(conv_tyler, 'guests', ' And ')
    conv_tyler = splitDataFrameList(conv_tyler, 'guests', ' and ')
    

    return conv_tyler


def clean_macro_musings(macro_musings):

    macro_musings = xml_to_df(macro_musings)

    date_parser(macro_musings)
    
    macro_musings['guests'] = macro_musings.title.str.extract(r' - ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    guest_split(' on ', macro_musings)
    guest_split(' talk ', macro_musings)
    guest_split(' has ', macro_musings)
    guest_split(' Wants ', macro_musings)
    guest_split(' Live ', macro_musings)
    guest_split(' Defends ', macro_musings)
    
    macro_musings = macro_musings[pd.notnull(macro_musings['guests'])]
    macro_musings = splitDataFrameList(macro_musings, 'guests', ', and ')
    macro_musings = splitDataFrameList(macro_musings, 'guests', ', ')
    macro_musings = splitDataFrameList(macro_musings, 'guests', ' & ')
    macro_musings = splitDataFrameList(macro_musings, 'guests', ' And ')
    macro_musings = splitDataFrameList(macro_musings, 'guests', ' and ')
    

    return macro_musings



def clean_who_makes_cents(who_makes_cents):

    who_makes_cents = xml_to_df(who_makes_cents)

    date_parser(who_makes_cents)
    
    who_makes_cents['guests'] = who_makes_cents.title.str.extract(r'([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    guest_split(' on ', who_makes_cents)
    guest_split(' talk ', who_makes_cents)
    guest_split(' has ', who_makes_cents)
    guest_split(' Wants ', who_makes_cents)
    guest_split(' Live ', who_makes_cents)
    guest_split(' Defends ', who_makes_cents)
    
    who_makes_cents = who_makes_cents[pd.notnull(who_makes_cents['guests'])]
    who_makes_cents = splitDataFrameList(who_makes_cents, 'guests', ', and ')
    who_makes_cents = splitDataFrameList(who_makes_cents, 'guests', ', ')
    who_makes_cents = splitDataFrameList(who_makes_cents, 'guests', ' & ')
    who_makes_cents = splitDataFrameList(who_makes_cents, 'guests', ' And ')
    who_makes_cents = splitDataFrameList(who_makes_cents, 'guests', ' and ')
    
    return who_makes_cents


def clean_new_books_econ(new_books_econ):

    new_books_econ = xml_to_df(new_books_econ)

    date_parser(new_books_econ)
    
    new_books_econ['guests'] = new_books_econ.title.str.extract(r'([\w\s\.\'\`\’\-\/]+), ',expand=True)

    guest_split(' et.', new_books_econ)
    
    new_books_econ = new_books_econ[pd.notnull(new_books_econ['guests'])]
    new_books_econ = splitDataFrameList(new_books_econ, 'guests', ', and ')
    new_books_econ = splitDataFrameList(new_books_econ, 'guests', ', ')
    new_books_econ = splitDataFrameList(new_books_econ, 'guests', ' & ')
    new_books_econ = splitDataFrameList(new_books_econ, 'guests', ' And ')
    new_books_econ = splitDataFrameList(new_books_econ, 'guests', ' and ')
    
    return new_books_econ


def clean_new_books_science(new_books_science):

    new_books_science = xml_to_df(new_books_science)

    date_parser(new_books_science)
    
    new_books_science['guests'] = new_books_science.title.str.extract(r'([\w\s\.\'\`\’\-\/]+), ',expand=True)
    
    new_books_science = new_books_science[pd.notnull(new_books_science['guests'])]
    new_books_science = splitDataFrameList(new_books_science, 'guests', ', and ')
    new_books_science = splitDataFrameList(new_books_science, 'guests', ', ')
    new_books_science = splitDataFrameList(new_books_science, 'guests', ' & ')
    new_books_science = splitDataFrameList(new_books_science, 'guests', ' And ')
    new_books_science = splitDataFrameList(new_books_science, 'guests', ' and ')
    
    return new_books_science


def clean_new_books_history(new_books_history):

    new_books_history = xml_to_df(new_books_history)

    date_parser(new_books_history)
    
    new_books_history['guests'] = new_books_history.title.str.extract(r'([\w\s\.\'\`\’\-\/]+), ',expand=True)
    
    new_books_history = new_books_history[pd.notnull(new_books_history['guests'])]
    new_books_history = splitDataFrameList(new_books_history, 'guests', ', and ')
    new_books_history = splitDataFrameList(new_books_history, 'guests', ', ')
    new_books_history = splitDataFrameList(new_books_history, 'guests', ' & ')
    new_books_history = splitDataFrameList(new_books_history, 'guests', ' And ')
    new_books_history = splitDataFrameList(new_books_history, 'guests', ' and ')
    
    return new_books_history


def clean_new_books_biography(new_books_biography):

    new_books_biography = xml_to_df(new_books_biography)

    date_parser(new_books_biography)
    
    new_books_biography['guests'] = new_books_biography.title.str.extract(r'([\w\s\.\'\`\’\-\/]+), ',expand=True)
    
    new_books_biography = new_books_biography[pd.notnull(new_books_biography['guests'])]
    new_books_biography = splitDataFrameList(new_books_biography, 'guests', ', and ')
    new_books_biography = splitDataFrameList(new_books_biography, 'guests', ', ')
    new_books_biography = splitDataFrameList(new_books_biography, 'guests', ' & ')
    new_books_biography = splitDataFrameList(new_books_biography, 'guests', ' And ')
    new_books_biography = splitDataFrameList(new_books_biography, 'guests', ' and ')
    
    return new_books_biography


def clean_new_books_american(new_books_american):

    new_books_american = xml_to_df(new_books_american)

    date_parser(new_books_american)
    
    new_books_american['guests'] = new_books_american.title.str.extract(r'([\w\s\.\'\`\’\-\/]+), ',expand=True)
    
    new_books_american = new_books_american[pd.notnull(new_books_american['guests'])]
    new_books_american = splitDataFrameList(new_books_american, 'guests', ', and ')
    new_books_american = splitDataFrameList(new_books_american, 'guests', ', ')
    new_books_american = splitDataFrameList(new_books_american, 'guests', ' & ')
    new_books_american = splitDataFrameList(new_books_american, 'guests', ' And ')
    new_books_american = splitDataFrameList(new_books_american, 'guests', ' and ')
    
    return new_books_american


def clean_dr_gameshow(dr_gameshow):

    dr_gameshow = xml_to_df(dr_gameshow)

    date_parser(dr_gameshow)
    
    dr_gameshow['guests'] = dr_gameshow.title.str.extract(r'\(w\/ ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    replace('Hello From The Magic Tavern', 'Adal Rifai, Arnie Niekamp and Matt Young', dr_gameshow)
    
    dr_gameshow = dr_gameshow[pd.notnull(dr_gameshow['guests'])]
    dr_gameshow = splitDataFrameList(dr_gameshow, 'guests', ', and ')
    dr_gameshow = splitDataFrameList(dr_gameshow, 'guests', ', ')
    dr_gameshow = splitDataFrameList(dr_gameshow, 'guests', ' & ')
    dr_gameshow = splitDataFrameList(dr_gameshow, 'guests', ' And ')
    dr_gameshow = splitDataFrameList(dr_gameshow, 'guests', ' and ')
    

    return dr_gameshow

def clean_homophilia(homophilia):

    homophilia = xml_to_df(homophilia)

    date_parser(homophilia)
    
    homophilia['guests'] = homophilia.title.str.extract(r'\d+. ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
        
    homophilia = homophilia[pd.notnull(homophilia['guests'])]
    homophilia = splitDataFrameList(homophilia, 'guests', ', and ')
    homophilia = splitDataFrameList(homophilia, 'guests', ', ')
    homophilia = splitDataFrameList(homophilia, 'guests', ' & ')
    homophilia = splitDataFrameList(homophilia, 'guests', ' And ')
    homophilia = splitDataFrameList(homophilia, 'guests', ' and ')
    

    return homophilia


def clean_throwing_shade(throwing_shade):

    throwing_shade = xml_to_df(throwing_shade)

    date_parser(throwing_shade)
    
    throwing_shade['guests'] = throwing_shade.title.str.extract(r'Guest(?:s)? ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
        
    throwing_shade = throwing_shade[pd.notnull(throwing_shade['guests'])]
    throwing_shade = splitDataFrameList(throwing_shade, 'guests', ', and ')
    throwing_shade = splitDataFrameList(throwing_shade, 'guests', ', ')
    throwing_shade = splitDataFrameList(throwing_shade, 'guests', ' & ')
    throwing_shade = splitDataFrameList(throwing_shade, 'guests', ' And ')
    throwing_shade = splitDataFrameList(throwing_shade, 'guests', ' and ')
    

    return throwing_shade


def clean_womp_it_up(womp_it_up):

    womp_it_up = xml_to_df(womp_it_up)

    date_parser(womp_it_up)
    
    womp_it_up['guests'] = womp_it_up.title.str.extract(r'([\w\s\.\,\'\`\’\-\/]+) - ',expand=True)
        
    womp_it_up = womp_it_up[pd.notnull(womp_it_up['guests'])]
    womp_it_up = splitDataFrameList(womp_it_up, 'guests', ', and ')
    womp_it_up = splitDataFrameList(womp_it_up, 'guests', ', ')
    womp_it_up = splitDataFrameList(womp_it_up, 'guests', ' & ')
    womp_it_up = splitDataFrameList(womp_it_up, 'guests', ' And ')
    womp_it_up = splitDataFrameList(womp_it_up, 'guests', ' and ')
    

    return womp_it_up


def clean_off_book(off_book):

    off_book = xml_to_df(off_book)

    date_parser(off_book)
    
    off_book['guests'] = off_book.title.str.extract(r'\(w\/ ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    replace('Hello From The Magic Tavern', 'Adal Rifai, Arnie Niekamp and Matt Young', off_book)
    
    off_book = off_book[pd.notnull(off_book['guests'])]
    off_book = splitDataFrameList(off_book, 'guests', ', and ')
    off_book = splitDataFrameList(off_book, 'guests', ', ')
    off_book = splitDataFrameList(off_book, 'guests', ' & ')
    off_book = splitDataFrameList(off_book, 'guests', ' And ')
    off_book = splitDataFrameList(off_book, 'guests', ' and ')
    

    return off_book


def clean_get_up_on_this(get_up_on_this):

    get_up_on_this = xml_to_df(get_up_on_this)

    date_parser(get_up_on_this)
    
    get_up_on_this['guests'] = get_up_on_this.title.str.extract(r'w\/ ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    get_up_on_this = get_up_on_this[pd.notnull(get_up_on_this['guests'])]
    get_up_on_this = splitDataFrameList(get_up_on_this, 'guests', ', and ')
    get_up_on_this = splitDataFrameList(get_up_on_this, 'guests', ', ')
    get_up_on_this = splitDataFrameList(get_up_on_this, 'guests', ' & ')
    get_up_on_this = splitDataFrameList(get_up_on_this, 'guests', ' And ')
    get_up_on_this = splitDataFrameList(get_up_on_this, 'guests', ' and ')
    
    return get_up_on_this


def clean_there_too(there_too):

    there_too = xml_to_df(there_too)

    date_parser(there_too)
    
    there_too['guests'] = there_too.title.str.extract(r'with ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    there_too = there_too[pd.notnull(there_too['guests'])]
    there_too = splitDataFrameList(there_too, 'guests', ', and ')
    there_too = splitDataFrameList(there_too, 'guests', ', ')
    there_too = splitDataFrameList(there_too, 'guests', ' & ')
    there_too = splitDataFrameList(there_too, 'guests', ' And ')
    there_too = splitDataFrameList(there_too, 'guests', ' and ')
    
    guest_split_last('Trainer ', there_too)
    guest_split_last('Co-host ', there_too)
    
    return there_too


def clean_queery(queery):

    queery = xml_to_df(queery)

    date_parser(queery)
    
    queery['guests'] = queery['title']
    
    guest_split_last('Live: ', queery)
    
    queery = queery[pd.notnull(queery['guests'])]
    queery = splitDataFrameList(queery, 'guests', ', and ')
    queery = splitDataFrameList(queery, 'guests', ', ')
    queery = splitDataFrameList(queery, 'guests', ' & ')
    queery = splitDataFrameList(queery, 'guests', ' And ')
    queery = splitDataFrameList(queery, 'guests', ' and ')
    
    guest_split_last('Trainer ', queery)
    guest_split_last('Co-host ', queery)
    
    return queery


def clean_canon(canon):

    canon = xml_to_df(canon)

    date_parser(canon)
    
    canon['guests'] = canon.title.str.extract(r'w\/ ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    canon = canon[pd.notnull(canon['guests'])]
    canon = splitDataFrameList(canon, 'guests', ', and ')
    canon = splitDataFrameList(canon, 'guests', ', ')
    canon = splitDataFrameList(canon, 'guests', ' & ')
    canon = splitDataFrameList(canon, 'guests', ' And ')
    canon = splitDataFrameList(canon, 'guests', ' and ')
    
    return canon


def clean_james_bonding(james_bonding):

    james_bonding = xml_to_df(james_bonding)

    date_parser(james_bonding)
    
    james_bonding['guests'] = james_bonding.title.str.extract(r'with ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    james_bonding = james_bonding[pd.notnull(james_bonding['guests'])]
    james_bonding = splitDataFrameList(james_bonding, 'guests', ', and ')
    james_bonding = splitDataFrameList(james_bonding, 'guests', ', ')
    james_bonding = splitDataFrameList(james_bonding, 'guests', ' & ')
    james_bonding = splitDataFrameList(james_bonding, 'guests', ' And ')
    james_bonding = splitDataFrameList(james_bonding, 'guests', ' and ')
    
    return james_bonding



def clean_kevin_pollak(kevin_pollak):

    kevin_pollak = xml_to_df(kevin_pollak)

    date_parser(kevin_pollak)
    
    kevin_pollak['guests'] = kevin_pollak.title.str.extract(r'(?:\d+|-) ([\w\s\.\,\'\`\’\-\/]+)',expand=True)
    
    kevin_pollak = kevin_pollak[pd.notnull(kevin_pollak['guests'])]
    kevin_pollak = splitDataFrameList(kevin_pollak, 'guests', ', and ')
    kevin_pollak = splitDataFrameList(kevin_pollak, 'guests', ', ')
    kevin_pollak = splitDataFrameList(kevin_pollak, 'guests', ' & ')
    kevin_pollak = splitDataFrameList(kevin_pollak, 'guests', ' And ')
    kevin_pollak = splitDataFrameList(kevin_pollak, 'guests', ' and ')
    
    return kevin_pollak


def clean_lauren_lapkus(lauren_lapkus):

    lauren_lapkus = xml_to_df(lauren_lapkus)

    date_parser(lauren_lapkus)
    
    lauren_lapkus['guests'] = lauren_lapkus.title.str.extract(r'([\w\s\.\,\'\`\’\-\/]+): ',expand=True)
    
    replace('Ronna and Beverly', 'Jessica Chaffin, Jamie Denbo', lauren_lapkus)
    
    lauren_lapkus = lauren_lapkus[pd.notnull(lauren_lapkus['guests'])]
    lauren_lapkus = splitDataFrameList(lauren_lapkus, 'guests', ', and ')
    lauren_lapkus = splitDataFrameList(lauren_lapkus, 'guests', ', ')
    lauren_lapkus = splitDataFrameList(lauren_lapkus, 'guests', ' & ')
    lauren_lapkus = splitDataFrameList(lauren_lapkus, 'guests', ' And ')
    lauren_lapkus = splitDataFrameList(lauren_lapkus, 'guests', ' and ')
    
    lauren_lapkus = lauren_lapkus[lauren_lapkus.guests.str.contains(r'Threedom') == False]
    
    return lauren_lapkus





