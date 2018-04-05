import numpy as np
import pandas as pd
import re
import datetime as dt
import time
from cleaning_functions import *


def clean_joe_rogan(joe_rogan):

    ## Remove Fight shows
    
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('MMA Show') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Fight Companion') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Recap') == False]
    joe_rogan = joe_rogan[joe_rogan.title.str.contains('Breakdown') == False]
    
    ## Extract episode number and guests
    
    joe_rogan['episode'] = joe_rogan.title.str.extract(r'\#(\d+)',expand=True)
    joe_rogan['guests'] = joe_rogan.title.str.extract(r'\#\d+\s-\s([\w\s.,&\'-]+)',expand=True)
    
    ## Clean guest list
    
    replace('Lewis, from Unbox Therapy', 'Lewis from Unbox Therapy', joe_rogan)
    replace('Lewis, form Unbox Therapy', 'Lewis from Unbox Therapy', joe_rogan)
    
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
    
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('From ')]
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('Live ')]
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('Ph.D')]
    joe_rogan = joe_rogan[~joe_rogan['guests'].str.startswith('Phd')]

    date_parser('\s\+0000$', joe_rogan)
    
    joe_rogan_output = joe_rogan

    return joe_rogan_output


def clean_duncan_trussel(duncan_trussel):
    from cleaning_functions import guest_split

    ## Set Episode numbers
    
    duncan_trussel['episode'] = len(duncan_trussel) - duncan_trussel.index

    date_parser('\sGMT$', duncan_trussel)
    
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
    
    #sum(duncan_trussel['guests'].str.contains('Christopher Ryan')==True)
    
    duncan_trussel_output = duncan_trussel
    
    return duncan_trussel_output  #'hello'  #duncan_trussel_output[duncan_trussel['guests']=='Paul F Tompkins'] 


pd.options.mode.chained_assignment = None  # default='warn'

#bert_kreischer = xml_to_df('bert_kreischer.xml')

def clean_bert_kreischer(bert_kreischer):
    
    bert_kreischer = bert_kreischer.loc[bert_kreischer.title.str.contains('Call In Sick To Work Show') == False]

    ## Set Episode numbers
    
    bert_kreischer['episode'] = bert_kreischer.title.str.extract(r'\#\s?([\d.]+)',expand=True)

    date_parser('\s\+0000$', bert_kreischer)
    
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

    for index, row in bert_kreischer.iterrows():
        if('W/ ' in row['guests']):
            split = row['guests'].split('W/ ')[-1]
            bert_kreischer.at[index, 'guests'] = split
            
    guest_split(' In', bert_kreischer)
            
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
    
    ## Split Guests
    
    bert_kreischer = bert_kreischer[pd.notnull(bert_kreischer['guests'])]
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ', ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ' & ')
    bert_kreischer = splitDataFrameList(bert_kreischer, 'guests', ' And ')
    
    bert_kreischer_output = bert_kreischer
    
    return bert_kreischer_output


def clean_tfatk(tfatk):

    ## Set Episode numbers
    
    tfatk['episode'] = tfatk.title.str.extract(r'\#\s?([\d.]+)',expand=True)

    date_parser('\s\-0000$', tfatk)
    
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

    ## Set Episode numbers
    
    ari_shaffir['episode'] = ari_shaffir.title.str.extract(r'\#:?([\d.\w]+)',expand=True)
    
    date_parser('\s\+0000$', ari_shaffir)
    
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
    
            
    
    return ari_shaffir


def clean_russell_brand(russell_brand):

    ## Set Episode numbers
    
    russell_brand['episode'] = russell_brand.title.str.extract(r'\#([\d]+)',expand=True)

    date_parser('\s\-0000$', russell_brand)
    
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
            russell_brand.at[index, 'guests'] = 'Dr Brad Evans'
        if(row['episode']=='012'):
            russell_brand.at[index, 'guests'] = 'Dr Brad Evans, Rabbi Dr Jonathan Romain'
        if(row['episode']=='014'):
            russell_brand.at[index, 'guests'] = 'Lindsey German and Dr Brad Evans'
        if(row['episode']=='015'):
            russell_brand.at[index, 'guests'] = 'Yanis Varoufakis'
        if(row['episode']=='018'):
            russell_brand.at[index, 'guests'] = 'Naomi Klein'
        if(row['episode']=='019'):
            russell_brand.at[index, 'guests'] = 'Frankie Boyle'
        if(row['episode']=='022'):
            russell_brand.at[index, 'guests'] = 'Dr Robin Carhart-Harris'
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

    russell_brand = russell_brand[pd.notnull(russell_brand['guests'])]
    russell_brand = splitDataFrameList(russell_brand, 'guests', ', ')
    russell_brand = splitDataFrameList(russell_brand, 'guests', ' & ')
    russell_brand = splitDataFrameList(russell_brand, 'guests', ' And ')
    russell_brand = splitDataFrameList(russell_brand, 'guests', ' and ')
    
    return russell_brand

def clean_kevin_pereira(kevin_pereira):

    ## Set Episode numbers
    
    kevin_pereira['episode'] = 185 - kevin_pereira.index

    date_parser('\s\+0000$', kevin_pereira)
    
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
            
            
    kevin_pereira = kevin_pereira[pd.notnull(kevin_pereira['guests'])]
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ', ')
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ' & ')
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ' And ')
    kevin_pereira = splitDataFrameList(kevin_pereira, 'guests', ' and ')
    
    return kevin_pereira


def clean_chris_hardwick(chris_hardwick):

    date_parser('\s\-0000$', chris_hardwick)
    
    chris_hardwick['guests'] = chris_hardwick['title']
    
    guest_split(' #', chris_hardwick)
    guest_split(' Returns', chris_hardwick)
    guest_split(' returns', chris_hardwick)
    guest_split(' LIVE', chris_hardwick)
    guest_split(' Live', chris_hardwick)
    guest_split('Live', chris_hardwick)
    guest_split(' of', chris_hardwick)

    guest_split_last('w/ ', chris_hardwick)
    
    ### Manual cleaning
    
    replace('Billy West.mp3', 'Billy West', chris_hardwick)
    
    
    chris_hardwick = chris_hardwick[pd.notnull(chris_hardwick['guests'])]
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ', ')
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ' & ')
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ' And ')
    chris_hardwick = splitDataFrameList(chris_hardwick, 'guests', ' and ')
    
    return chris_hardwick


def clean_sam_harris(sam_harris):

    date_parser('\s\+0000$', sam_harris)
    
    sam_harris['episode'] = sam_harris.title.str.extract(r'\#\s?([\d]+)',expand=True)

    sam_harris['guests'] = sam_harris.description.str.extract(r'In this episode of the Waking Up podcast, Sam Harris speaks with ([\w\s\.\']+).',expand=True)
    
    sam_harris = sam_harris.drop('description', 1)
    
    guest_split(' about', sam_harris)
    guest_split(' at', sam_harris)
    
    guest_split_last('physicist ', sam_harris)
    guest_split_last('cosmologist ', sam_harris)
    guest_split_last('scientist ', sam_harris)
    guest_split_last('author ', sam_harris)
    guest_split_last('journalist ', sam_harris)
    guest_split_last('psychologist ', sam_harris)
    guest_split_last('philosopher ', sam_harris)
    guest_split_last('filmmaker ', sam_harris) 

    replace('former SWAT operator and lead weapons and tactics instructor for the LAPD Metro Division, Scott Reitz', 'Scott Reitz', sam_harris)
    replace('retired Navy SEAL and author', 'Jocko Willink', sam_harris)
    replace('Jordan B. Peterson', 'Jordan Peterson', sam_harris)
    
    sam_harris = sam_harris[pd.notnull(sam_harris['guests'])]
    sam_harris = splitDataFrameList(sam_harris, 'guests', ', ')
    sam_harris = splitDataFrameList(sam_harris, 'guests', ' & ')
    sam_harris = splitDataFrameList(sam_harris, 'guests', ' And ')
    sam_harris = splitDataFrameList(sam_harris, 'guests', ' and ')
    
    return sam_harris


def clean_kill_tony(kill_tony):
    
    kill_tony = kill_tony[kill_tony.title.str.contains('KILL TONY') == True]

    ## Set Episode numbers
    
    kill_tony['episode'] = kill_tony.title.str.extract(r'KILL TONY \#([\d]+)',expand=True)

    date_parser('\s\+0000$', kill_tony)
    
    kill_tony['guests'] = kill_tony['subtitle']
    
    kill_tony = kill_tony.drop('subtitle', 1)
    
    kill_tony = kill_tony[pd.notnull(kill_tony['guests'])]
    kill_tony = splitDataFrameList(kill_tony, 'guests', ', ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', ' & ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', ' And ')
    kill_tony = splitDataFrameList(kill_tony, 'guests', ' and ')
    
    guest_split(' -', kill_tony)
    replace('SteveO', 'Steve-O', kill_tony)
    
    return kill_tony


def clean_dave_rubin(dave_rubin):

    ## Set Episode numbers
    
    dave_rubin['episode'] = 202 - dave_rubin.index

    date_parser('\s\-0000$', dave_rubin)
    
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
    guest_split_last('Governer ', dave_rubin)

    replace('Two years ago, Lubna Ahmed', 'Lubna Ahmed', dave_rubin)
    replace('Brothers Bret Weinstein', 'Bret Weinstein and Eric Weinstein', dave_rubin)
    
    dave_rubin = dave_rubin[pd.notnull(dave_rubin['guests'])]
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ', ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ' & ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ' And ')
    dave_rubin = splitDataFrameList(dave_rubin, 'guests', ' and ')
    
    replace('Jordan B Peterson', 'Jordan Peterson', dave_rubin)
    replace('Red Pill Black', 'Candace Owens', dave_rubin)
    
    
    return dave_rubin


def clean_comedy_bang(comedy_bang):
    
    comedy_bang = comedy_bang[comedy_bang.title.str.contains('Best of') == False]

    ## Set Episode numbers
    
    comedy_bang['episode'] = comedy_bang.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser('\s\-0[78]00$', comedy_bang)
    
    comedy_bang['guests'] = comedy_bang.title.str.extract(r'(?:[\d]+)\s([\w\s\.\,&/\’\'\-"]+)',expand=True)
    
    comedy_bang = comedy_bang[pd.notnull(comedy_bang['guests'])]
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ', ')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ',')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ' & ')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ' And ')
    comedy_bang = splitDataFrameList(comedy_bang, 'guests', ' and ')
    
    return comedy_bang

def clean_h3(h3):

    ## Set Episode numbers
    
    h3['episode'] = h3.title.str.extract(r'\#([\d]+)',expand=True)

    date_parser('\s\+0000$', h3)
    
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
    replace('Vsauce3 ', 'Jake Roper', h3)
    replace('How To Save a Life', 'Chris Betancourt, Dillon Hill', h3)
    
    for index, row in h3.iterrows():
        if(row['episode']=='15'):
            h3.at[index, 'guests'] = np.nan
        if(row['episode']=='21'):
            h3.at[index, 'guests'] = np.nan
        if(row['episode']=='20'):
            h3.at[index, 'guests'] = 'Jimmie Lee'
    
    h3 = h3[pd.notnull(h3['guests'])]
    h3 = splitDataFrameList(h3, 'guests', ', ')
    h3 = splitDataFrameList(h3, 'guests', ' & ')
    h3 = splitDataFrameList(h3, 'guests', ' And ')
    h3 = splitDataFrameList(h3, 'guests', ' and ')
    
    return h3


def clean_marc_maron(marc_maron):

    ## Set Episode numbers
    
    marc_maron['episode'] = marc_maron.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser('\s\+0000$', marc_maron)
    
    marc_maron['guests'] = marc_maron.title.str.extract(r'(?:[\d]+)\s-\s([\w\s\.\,&/\’\'\-"]+)',expand=True)
    
    replace('The President Was Here', np.nan, marc_maron)
    
    marc_maron = marc_maron[pd.notnull(marc_maron['guests'])]
    marc_maron = splitDataFrameList(marc_maron, 'guests', ' / ')
    marc_maron = splitDataFrameList(marc_maron, 'guests', ' & ')

    return marc_maron


def clean_joey_diaz(joey_diaz):

    ## Set Episode numbers
    
    joey_diaz['episode'] = joey_diaz.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser('\s\+0000$', joey_diaz)
    
    joey_diaz['guests'] = joey_diaz.title.str.extract(r'(?:[\d]+)\s-\s([\w\s\.\,&/\’\'"]+)',expand=True)
    
    replace("The Church Of What's Happening Now", np.nan, joey_diaz)
    replace("The Church Of What's Happening Now ", np.nan, joey_diaz)
    replace("The Chuch Of What's Happening Now", np.nan, joey_diaz)
    joey_diaz = joey_diaz[joey_diaz.guests.str.contains('Church') == False]
    
    joey_diaz = joey_diaz[pd.notnull(joey_diaz['guests'])]
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ', and ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ', ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' & ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' And ')
    joey_diaz = splitDataFrameList(joey_diaz, 'guests', ' and ')

    return joey_diaz


def clean_your_moms_house(your_moms_house):

    ## Set Episode numbers
    
    your_moms_house['episode'] = your_moms_house.title.str.extract(r'([\d]+)\s?-',expand=True)

    date_parser('\s\+0000$', your_moms_house)
    
    your_moms_house['guests'] = your_moms_house.title.str.extract(r'(?:[\d]+-)?([\w\s]+)-',expand=True)
    your_moms_house['guests'] = your_moms_house.guests.str.extract(r'([\D]+)',expand=True)
    
    guest_split('Live', your_moms_house)
    guest_split('LIVE ', your_moms_house)
    
    your_moms_house = your_moms_house.replace(r'', np.nan, regex=True)
    
    for index, row in your_moms_house.iterrows():
        if(row['episode']=='255'):
            your_moms_house.at[index, 'guests'] = np.nan
    
    your_moms_house = your_moms_house[pd.notnull(your_moms_house['guests'])]
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ', and ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ', ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ' & ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ' And ')
    your_moms_house = splitDataFrameList(your_moms_house, 'guests', ' and ')
    
    replace('Redban', 'Brian Redban', your_moms_house)

    return your_moms_house

def clean_harmontown(harmontown):
    from cleaning_functions import guest_split

    date_parser('\sGMT$', harmontown)
    
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
    
    return harmontown



def clean_stefan_molyneux(stefan_molyneux):

    ## Set Episode numbers
    
    stefan_molyneux['episode'] = stefan_molyneux.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser('\sGMT$', stefan_molyneux)
    
    stefan_molyneux['guests'] = stefan_molyneux.title.str.extract(r'\| ([\w\s\.]+) and Stefan Molyneux',expand=True)

    stefan_molyneux = stefan_molyneux[pd.notnull(stefan_molyneux['guests'])]
    

    return stefan_molyneux


def clean_econtalk(econtalk):

    date_parser('\sEST$', econtalk)
    
    econtalk['guests'] = econtalk.title.str.extract(r'([\w\s\.\,\']+) on',expand=True)
    guest_split(' on', econtalk)
    
    #econtalk = econtalk[pd.notnull(econtalk['guests'])]
    econtalk = splitDataFrameList(econtalk, 'guests', ', and ')
    econtalk = splitDataFrameList(econtalk, 'guests', ', ')
    econtalk = splitDataFrameList(econtalk, 'guests', ' & ')
    econtalk = splitDataFrameList(econtalk, 'guests', ' And ')
    econtalk = splitDataFrameList(econtalk, 'guests', ' and ')
    

    return econtalk


def clean_bill_maher(bill_maher):

    date_parser('\s\+0000$', bill_maher)
    
    bill_maher['guests'] = bill_maher.subtitle.str.extract(r'(?:guests\s(?:–|-)?\s?|guests are |guests \()([\w\s\.\,\'\`\’]+)(?: (?:– )?answer|. \(|\)|.$)',expand=True)
    
    guest_split('answer', bill_maher)
    guest_split_last('are ', bill_maher)

    bill_maher = bill_maher.drop('subtitle', 1)
    
    bill_maher = bill_maher[pd.notnull(bill_maher['guests'])]
    bill_maher = splitDataFrameList(bill_maher, 'guests', ', and ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ', ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ' & ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ' And ')
    bill_maher = splitDataFrameList(bill_maher, 'guests', ' and ')
    

    return bill_maher


def clean_pete_holmes(pete_holmes):

    date_parser('\s\+0000$', pete_holmes)
    
    pete_holmes['guests'] = pete_holmes['title']
    
    guest_split(' Re-Release', pete_holmes)
    guest_split(' #', pete_holmes)
    guest_split(' Returns', pete_holmes)
    guest_split_last('are ', pete_holmes)
    
    pete_holmes = pete_holmes[pd.notnull(pete_holmes['guests'])]
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ', and ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ', ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ' & ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ' And ')
    pete_holmes = splitDataFrameList(pete_holmes, 'guests', ' and ')
    

    return pete_holmes


def clean_anna_faris(anna_faris):

    date_parser('\s\+0000$', anna_faris)
    
    anna_faris['guests'] = anna_faris.title.str.extract(r'(?:ep [\d]+: )?([\w\s\.\,\'\`\’]+)',expand=True)

    guest_split(' Pt.', anna_faris)
    guest_split(' Returns', anna_faris)
    
    anna_faris = anna_faris[pd.notnull(anna_faris['guests'])]
    anna_faris = splitDataFrameList(anna_faris, 'guests', ', and ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ', ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ' & ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ' And ')
    anna_faris = splitDataFrameList(anna_faris, 'guests', ' and ')
    
    return anna_faris


def clean_dax_shepard(dax_shepard):

    date_parser('\s\-0[78]00$', dax_shepard)
    
    dax_shepard['guests'] = dax_shepard['title']
    
    guest_split_last('with ', dax_shepard)
    
    return dax_shepard


def clean_grapefruit_simmons(grapefruit_simmons):

    date_parser('\s\+0000$', grapefruit_simmons)
    
    grapefruit_simmons['guests'] = grapefruit_simmons['title']
    
    guest_split(' -', grapefruit_simmons)
    guest_split(' Is', grapefruit_simmons)
    

    grapefruit_simmons = splitDataFrameList(grapefruit_simmons, 'guests', ' and ')
    
    replace('Christina P', 'Christina Pazsitzky', grapefruit_simmons)
    
    return grapefruit_simmons


def clean_sam_tripoli(sam_tripoli):

    date_parser('\s\+0000$', sam_tripoli)
    
    sam_tripoli['guests'] = sam_tripoli.title.str.extract(r'(?:with|The Naughty Show \#[\d]+(?: - |: ))([\w\s\.\,\'\`\’\!\"]+)',expand=True)
    
    guest_split(' is', sam_tripoli)
    guest_split(' Returns', sam_tripoli)
    guest_split(' plus', sam_tripoli)
    guest_split_last('with ', sam_tripoli)
    guest_split_last('With ', sam_tripoli)
    
    sam_tripoli = sam_tripoli[pd.notnull(sam_tripoli['guests'])]
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ', and ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ', ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ' & ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ' And ')
    sam_tripoli = splitDataFrameList(sam_tripoli, 'guests', ' and ')
    
    replace("the Pirate Life Radio's Tait Fletcher", 'Tait Fletcher', sam_tripoli)
    
    guests = [g.rstrip('.') for g in sam_tripoli['guests']]
    sam_tripoli['guests'] = guests
    
    return sam_tripoli


def clean_alison_rosen(alison_rosen):
    
    date_parser('\s\+0000$', alison_rosen)
    
    alison_rosen['guests'] = alison_rosen['title']
    
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains(r'[\w]\'s') == False]

    guest_split(' - Part', alison_rosen)
    guest_split(' Returns', alison_rosen)
    guest_split(' LIVE', alison_rosen)
    guest_split(' Live', alison_rosen)
    guest_split(' aka', alison_rosen)
    guest_split(' (', alison_rosen)
    guest_split(' -', alison_rosen)
    
    alison_rosen = alison_rosen[alison_rosen.guests.str.contains('!') == False]
    
    alison_rosen = alison_rosen[pd.notnull(alison_rosen['guests'])]
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ', and ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ', ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' & ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' And ')
    alison_rosen = splitDataFrameList(alison_rosen, 'guests', ' and ')
    
    replace('Christina P', 'Christina Pazsitzky', alison_rosen)
    replace('Jason', 'Jason Sklar', alison_rosen)
    
    guests = [g.rstrip(',') for g in alison_rosen['guests']]
    alison_rosen['guests'] = guests
    
    return alison_rosen



def clean_chris_ryan(chris_ryan):
    
    chris_ryan['episode'] = chris_ryan.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser('\s\+0000$', chris_ryan)
    
    chris_ryan['guests'] = chris_ryan.title.str.extract(r'(?:[\d]+\s-\s)([^(]+)',expand=True)
    
    guest_split(' In', chris_ryan)
    guest_split(' in', chris_ryan)
    guest_split_last('with ', chris_ryan)
    guest_split_last('With ', chris_ryan)
    
    chris_ryan = chris_ryan[chris_ryan.guests.str.contains('Special') == False]
    
    chris_ryan = chris_ryan[pd.notnull(chris_ryan['guests'])]
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ', and ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ', ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ' & ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ' And ')
    chris_ryan = splitDataFrameList(chris_ryan, 'guests', ' and ')
    
    replace('Daniel Bolelli', 'Daniele Bolelli', chris_ryan)
    replace('Daniele Bolleli', 'Daniele Bolelli', chris_ryan)
    replace('Danielle Bolleli', 'Daniele Bolelli', chris_ryan)
    replace('Danielle Bolelli', 'Daniele Bolelli', chris_ryan)
    
    return chris_ryan


def clean_hdtgm(hdtgm):
    
    hdtgm['episode'] = hdtgm.title.str.extract(r'([\d]+)\s',expand=True)

    date_parser('\s\-0[78]00$', hdtgm)
    
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
    
    todd_glass['episode'] = todd_glass.title.str.extract(r'([\d\.]+)-\s',expand=True)

    date_parser('\s\+0000$', todd_glass)
    
    todd_glass['guests'] = todd_glass.title.str.extract(r'[\d\.]+-\s([\w\s\.\,\'\`\’\&\-]+)',expand=True)
    
    guest_split(' Part', todd_glass)
    guest_split('Live', todd_glass)
    
    todd_glass = todd_glass[todd_glass.guests.str.contains('HAPPY') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('Show') == False]
    todd_glass = todd_glass[todd_glass.guests.str.contains('show') == False]
    
    todd_glass = todd_glass[pd.notnull(todd_glass['guests'])]
    todd_glass = splitDataFrameList(todd_glass, 'guests', ', and ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ', ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ' & ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ' And ')
    todd_glass = splitDataFrameList(todd_glass, 'guests', ' and ')
    
    replace('', np.nan, todd_glass)
    todd_glass = todd_glass[pd.notnull(todd_glass['guests'])]
    
    return todd_glass

def clean_dumb_people_town(dumb_people_town):

    date_parser('\s\-0000$', dumb_people_town)
    
    dumb_people_town['guests'] = dumb_people_town.title.str.extract(r'(?:Minisode: )?([\w\s\.\,\'\`\’\&]+)\s-',expand=True)
    
    guest_split(' pt.', dumb_people_town)
    
    dumb_people_town = dumb_people_town[dumb_people_town.guests.str.contains(r'\d') == False]
    
    dumb_people_town = dumb_people_town[pd.notnull(dumb_people_town['guests'])]
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ', and ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ', ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ' & ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ' And ')
    dumb_people_town = splitDataFrameList(dumb_people_town, 'guests', ' and ')
    
    replace('Joey CoCo Diaz', 'Joey Diaz', dumb_people_town)
    
    return dumb_people_town


def clean_doug_loves_movies(doug_loves_movies):

    date_parser('\s\-0000$', doug_loves_movies)
    
    doug_loves_movies['guests'] = doug_loves_movies.title.str.extract(r'([\w\s\.\,\'\`\’\&\"]+)\sguest',expand=True)

    doug_loves_movies = doug_loves_movies[pd.notnull(doug_loves_movies['guests'])]
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ', and ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ', ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ' & ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ' And ')
    doug_loves_movies = splitDataFrameList(doug_loves_movies, 'guests', ' and ')

    replace('Joey CoCo Diaz', 'Joey Diaz', doug_loves_movies)
    
    return doug_loves_movies

def clean_getting_doug_with_high(getting_doug_with_high):
    
    getting_doug_with_high['episode'] = getting_doug_with_high.title.str.extract(r'E[pP] ([\d]+)',expand=True)

    date_parser('\s\-0000$', getting_doug_with_high)
    
    getting_doug_with_high['guests'] = getting_doug_with_high.title.str.extract(r'E[pP] [\d]+\s([\w\s\.\,\'\`\’\&\"\-]+)\s(?:\||\-)',expand=True)

    getting_doug_with_high = getting_doug_with_high[pd.notnull(getting_doug_with_high['guests'])]
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ', and ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ', ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' & ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' And ')
    getting_doug_with_high = splitDataFrameList(getting_doug_with_high, 'guests', ' and ')

    replace('Joey CoCo Diaz', 'Joey Diaz', getting_doug_with_high)
    
    return getting_doug_with_high

def clean_who_charted(who_charted):
    
    who_charted['episode'] = who_charted.title.str.extract(r'([\d]+)',expand=True)

    date_parser('\s\-0[78]00$', who_charted)
    
    who_charted['guests'] = who_charted.title.str.extract(r'[\d]+\s([\w\s\.\,\'\`\’\&\"\-]+)',expand=True)

    who_charted = who_charted[pd.notnull(who_charted['guests'])]
    who_charted = splitDataFrameList(who_charted, 'guests', ', and ')
    who_charted = splitDataFrameList(who_charted, 'guests', ', ')
    who_charted = splitDataFrameList(who_charted, 'guests', ' & ')
    who_charted = splitDataFrameList(who_charted, 'guests', ' And ')
    who_charted = splitDataFrameList(who_charted, 'guests', ' and ')

    return who_charted


def clean_the_indoor_kids(the_indoor_kids):
    
    the_indoor_kids['episode'] = len(the_indoor_kids) - the_indoor_kids.index
    
    date_parser('\s\+0000$', the_indoor_kids)
    
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

    
    the_indoor_kids = the_indoor_kids[pd.notnull(the_indoor_kids['guests'])]
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ', and ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ', ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ' & ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ' And ')
    the_indoor_kids = splitDataFrameList(the_indoor_kids, 'guests', ' and ')

    
    return the_indoor_kids


def clean_comedy_film_nerds(comedy_film_nerds):

    comedy_film_nerds['episode'] = comedy_film_nerds.title.str.extract(r'(Ep [\d]+)',expand=True)
    
    date_parser('\s\+0000$', comedy_film_nerds)
    
    comedy_film_nerds['guests'] = comedy_film_nerds.title.str.extract(r'(?:Ep [\d]+ - [\w\s\.\,\'\`\’\&\"\-\:]+)(?: - )([\w\s\.\,\'\`\’\&\"\-]+)$',expand=True)
    
    comedy_film_nerds = comedy_film_nerds[pd.notnull(comedy_film_nerds['guests'])]
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ', and ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ', ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ' & ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ' And ')
    comedy_film_nerds = splitDataFrameList(comedy_film_nerds, 'guests', ' and ')

    
    return comedy_film_nerds





