import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import re
import networkx as nx
import datetime as dt
import time

from cleaning_functions import *
from cleaners import *

joe_rogan = xml_to_df('rss_files/joe_rogan.xml')
joe_rogan = clean_joe_rogan(joe_rogan)
joe_rogan['hosts'] = 'Joe Rogan'
joe_rogan['podcast'] = 'The Joe Rogan Experience'

duncan_trussel = xml_to_df('rss_files/duncan_trussel.xml')
duncan_trussel = clean_duncan_trussel(duncan_trussel)
duncan_trussel['hosts'] = 'Duncan Trussell'
duncan_trussel['podcast'] = 'The Duncan Trussell Family Hour'

bert_kreischer = xml_to_df('rss_files/bert_kreischer.xml')
bert_kreischer = clean_bert_kreischer(bert_kreischer)
bert_kreischer['hosts'] = 'Bert Kreischer'
bert_kreischer['podcast'] = "Bertcast's podcast"

tfatk = xml_to_df('rss_files/fighter-and-the-kid.xml')
tfatk = clean_tfatk(tfatk)
tfatk['hosts'] = 'Bryan Callen, Brendan Schaub'
tfatk['podcast'] = 'The Fighter and the Kid'

ari_shaffir = xml_to_df('rss_files/ari_shaffir.xml')
ari_shaffir = clean_ari_shaffir(ari_shaffir)
ari_shaffir['hosts'] = 'Ari Shaffir'
ari_shaffir['podcast'] = "Ari Shaffir's Skeptic Tank"

russell_brand = xml_to_df('rss_files/russell_brand.xml')
russell_brand = clean_russell_brand(russell_brand)
russell_brand['hosts'] = 'Russell Brand'
russell_brand['podcast'] = 'Under The Skin with Russell Brand'

kevin_pereira = xml_to_df('rss_files/kevin_pereira.xml')
kevin_pereira = clean_kevin_pereira(kevin_pereira)
kevin_pereira['hosts'] = 'Kevin Pereira'
kevin_pereira['podcast'] = 'Pointless: with Kevin Pereira'

chris_hardwick = xml_to_df('rss_files/chris_hardwick.xml')
chris_hardwick = clean_chris_hardwick(chris_hardwick) 
chris_hardwick['hosts'] = 'Chris Hardwick'
chris_hardwick['podcast'] = 'ID10T with Chris Hardwick'

sam_harris = xml_to_df_desc('rss_files/sam_harris.xml')
sam_harris = clean_sam_harris(sam_harris)
sam_harris['hosts'] = 'Sam Harris'
sam_harris['podcast'] = 'Waking Up with Sam Harris'

kill_tony = xml_to_df_subt('rss_files/kill_tony.xml')
kill_tony = clean_kill_tony(kill_tony)
kill_tony['hosts'] = 'Tony Hinchcliffe, Brian Redban'
kill_tony['podcast'] = 'Kill Tony'

dave_rubin = xml_to_df_summ('rss_files/dave-rubin.xml')
dave_rubin = clean_dave_rubin(dave_rubin)
dave_rubin['hosts'] = 'Dave Rubin'
dave_rubin['podcast'] = 'The Rubin Report'

comedy_bang = xml_to_df('rss_files/comedy-bang-bang.xml')
comedy_bang = clean_comedy_bang(comedy_bang)
comedy_bang['hosts'] = 'Scott Aukerman'
comedy_bang['podcast'] = 'Comedy Bang Bang'

h3 = xml_to_df('rss_files/h3.xml')
h3 = clean_h3(h3)
h3['hosts'] = 'Ethan Klein'
h3['podcast'] = 'H3 Podcast'

marc_maron = xml_to_df('rss_files/marc_maron.xml')
marc_maron = clean_marc_maron(marc_maron)
marc_maron['hosts'] = 'Marc Maron'
marc_maron['podcast'] = 'WTF with Marc Maron Podcast'

joey_diaz = xml_to_df('rss_files/joey_diaz.xml')
joey_diaz = clean_joey_diaz(joey_diaz)
joey_diaz['hosts'] = 'Joey Diaz'
joey_diaz['podcast'] = "The Church of What's Happening Now: With Joey Coco Diaz"

your_moms_house = xml_to_df('rss_files/your_moms_house.xml')
your_moms_house = clean_your_moms_house(your_moms_house)
your_moms_house['hosts'] = 'Tom Segura, Christina Pazsitzky'
your_moms_house['podcast'] = "Your Mom's House with Christina P. and Tom Segura"

harmontown = xml_to_df_summ('rss_files/harmontown.xml')
harmontown = clean_harmontown(harmontown)
harmontown['hosts'] = 'Dan Harmon'
harmontown['podcast'] = 'Harmontown'

stefan_molyneux = xml_to_df('rss_files/stefan_molyneux.xml')#archives
stefan_molyneux = clean_stefan_molyneux(stefan_molyneux)
stefan_molyneux['hosts'] = 'Stefan Molyneux'
stefan_molyneux['podcast'] = 'Freedomain Radio with Stefan Molyneux'

econtalk = xml_to_df('rss_files/econtalk.xml')#archives
econtalk = clean_econtalk(econtalk)
econtalk['hosts'] = 'Russ Roberts'
econtalk['podcast'] = 'Econtalk'

bill_maher = xml_to_df_subt('rss_files/bill_maher.xml')
bill_maher = clean_bill_maher(bill_maher)
bill_maher['hosts'] = 'Bill Maher'
bill_maher['podcast'] = 'Real Time with Bill Maher'

pete_holmes = xml_to_df('rss_files/pete_holmes.xml')
pete_holmes = clean_pete_holmes(pete_holmes)
pete_holmes['hosts'] = 'Pete Holmes'
pete_holmes['podcast'] = 'You Made It Weird with Pete Holmes'

anna_faris = xml_to_df('rss_files/anna_faris.xml')
anna_faris = clean_anna_faris(anna_faris)
anna_faris['hosts'] = 'Anna Faris'
anna_faris['podcast'] = 'Anna Faris Is Unqualified'

dax_shepard = xml_to_df('rss_files/dax_shepard.xml')
dax_shepard = clean_dax_shepard(dax_shepard)
dax_shepard['hosts'] = 'Dax Shepard'
dax_shepard['podcast'] = 'Armchair Expert with Dax Shepard'

grapefruit_simmons = xml_to_df('rss_files/grapefruit_simmons.xml')
grapefruit_simmons = clean_grapefruit_simmons(grapefruit_simmons)
grapefruit_simmons['hosts'] = 'Greg Fitzsimmons'
grapefruit_simmons['podcast'] = 'Fitzdog Radio'

sam_tripoli = xml_to_df('rss_files/sam_tripoli.xml')
sam_tripoli = clean_sam_tripoli(sam_tripoli)
sam_tripoli['hosts'] = 'Sam Tripoli'
sam_tripoli['podcast'] = 'Tin Foil Hat With Sam Tripoli'

alison_rosen = xml_to_df('rss_files/alison_rosen.xml')
alison_rosen = clean_alison_rosen(alison_rosen)
alison_rosen['hosts'] = 'Alison Rosen'
alison_rosen['podcast'] = 'Alison Rosen Is Your New Best Friend'

chris_ryan = xml_to_df('rss_files/christopher_ryan.xml')
chris_ryan = clean_chris_ryan(chris_ryan)
chris_ryan['hosts'] = 'Christopher Ryan'
chris_ryan['podcast'] = 'Tangentially Speaking with Christopher Ryan'

hdtgm = xml_to_df('rss_files/how-did-this-get-made.xml')
hdtgm = clean_hdtgm(hdtgm)
hdtgm['hosts'] = 'Paul Scheer, June Diane Raphael, Jason Mantzoukas'
hdtgm['podcast'] = 'How Did This Get Made?'

todd_glass = xml_to_df('rss_files/todd_glass.xml')
todd_glass = clean_todd_glass(todd_glass)
todd_glass['hosts'] = 'Todd Glass'
todd_glass['podcast'] = 'The Todd Glass Show'

dumb_people_town = xml_to_df('rss_files/dumb_people_town.xml')
dumb_people_town = clean_dumb_people_town(dumb_people_town)
dumb_people_town['hosts'] = 'Jason Sklar, Randy Sklar'
dumb_people_town['podcast'] = 'Dumb People Town'

doug_loves_movies = xml_to_df('rss_files/doug_loves_movies.xml')
doug_loves_movies = clean_doug_loves_movies(doug_loves_movies)
doug_loves_movies['hosts'] = 'Doug Benson'
doug_loves_movies['podcast'] = 'Doug Loves Movies'

getting_doug_with_high = xml_to_df('rss_files/getting_doug_with_high.xml')
getting_doug_with_high = clean_getting_doug_with_high(getting_doug_with_high)
getting_doug_with_high['hosts'] = 'Doug Benson'
getting_doug_with_high['podcast'] = 'Getting Doug with High'

who_charted = xml_to_df('rss_files/who-charted.xml')
who_charted = clean_who_charted(who_charted)
who_charted['hosts'] = 'Howard Kremer, Kulap Vilaysack'
who_charted['podcast'] = 'Who Charted?'

the_indoor_kids = xml_to_df('rss_files/the_indoor_kids.xml')
the_indoor_kids = clean_the_indoor_kids(the_indoor_kids)
the_indoor_kids['hosts'] = 'Kumail Nanjiani, Emily V. Gordon'
the_indoor_kids['podcast'] = 'The Indoor Kids with Kumail Nanjiani and Emily V. Gordon'

comedy_film_nerds = xml_to_df('rss_files/comedy_film_nerds.xml')
comedy_film_nerds = clean_comedy_film_nerds(comedy_film_nerds)
comedy_film_nerds['hosts'] = 'Graham Elwood, Chris Mancini'
comedy_film_nerds['podcast'] = 'Comedy Film Nerds'

df = pd.concat([joe_rogan, duncan_trussel, bert_kreischer, tfatk, ari_shaffir,
               russell_brand, kevin_pereira, chris_hardwick, sam_harris,
               kill_tony, dave_rubin, comedy_bang, h3, marc_maron,
               joey_diaz, your_moms_house, harmontown, stefan_molyneux,
               econtalk, bill_maher, pete_holmes, anna_faris, dax_shepard,
               grapefruit_simmons, sam_tripoli, alison_rosen, chris_ryan,
               hdtgm, todd_glass, dumb_people_town, doug_loves_movies,
               getting_doug_with_high, who_charted, the_indoor_kids,
               comedy_film_nerds], ignore_index=True)


df.to_csv('cleaned_podcasts.csv', sep='\t')


