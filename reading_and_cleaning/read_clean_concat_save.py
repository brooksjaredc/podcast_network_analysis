import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import re
import networkx as nx
import datetime as dt
import time

from cleaning_functions import *
from cleaners import *

joe_rogan = 'rss_files/joe_rogan.xml'
joe_rogan = clean_joe_rogan(joe_rogan)
joe_rogan['hosts'] = 'Joe Rogan'
joe_rogan['podcast'] = 'The Joe Rogan Experience'

duncan_trussel = 'rss_files/duncan_trussel.xml'
duncan_trussel = clean_duncan_trussel(duncan_trussel)
duncan_trussel['hosts'] = 'Duncan Trussell'
duncan_trussel['podcast'] = 'The Duncan Trussell Family Hour'

bert_kreischer = 'rss_files/bert_kreischer.xml'
bert_kreischer = clean_bert_kreischer(bert_kreischer)
bert_kreischer['hosts'] = 'Bert Kreischer'
bert_kreischer['podcast'] = "Bertcast's podcast"

tfatk = 'rss_files/fighter-and-the-kid.xml'
tfatk = clean_tfatk(tfatk)
tfatk['hosts'] = 'Bryan Callen, Brendan Schaub'
tfatk['podcast'] = 'The Fighter & The Kid'

ari_shaffir = 'rss_files/ari_shaffir.xml'
ari_shaffir = clean_ari_shaffir(ari_shaffir)
ari_shaffir['hosts'] = 'Ari Shaffir'
ari_shaffir['podcast'] = "Ari Shaffir's Skeptic Tank"

russell_brand = 'rss_files/russell_brand.xml'
russell_brand = clean_russell_brand(russell_brand)
russell_brand['hosts'] = 'Russell Brand'
russell_brand['podcast'] = 'Under The Skin with Russell Brand'

kevin_pereira = 'rss_files/kevin_pereira.xml'
kevin_pereira = clean_kevin_pereira(kevin_pereira)
kevin_pereira['hosts'] = 'Kevin Pereira'
kevin_pereira['podcast'] = 'Pointless: with Kevin Pereira'

chris_hardwick = 'rss_files/chris_hardwick.xml'
chris_hardwick = clean_chris_hardwick(chris_hardwick) 
chris_hardwick['hosts'] = 'Chris Hardwick'
chris_hardwick['podcast'] = 'ID10T with Chris Hardwick'

sam_harris = 'rss_files/sam_harris.xml'
sam_harris = clean_sam_harris(sam_harris)
sam_harris['hosts'] = 'Sam Harris'
sam_harris['podcast'] = 'Waking Up with Sam Harris'

kill_tony = 'rss_files/kill_tony.xml'
kill_tony = clean_kill_tony(kill_tony)
kill_tony['hosts'] = 'Tony Hinchcliffe, Brian Redban'
kill_tony['podcast'] = 'Kill Tony'

dave_rubin = 'rss_files/dave-rubin.xml'
dave_rubin = clean_dave_rubin(dave_rubin)
dave_rubin['hosts'] = 'Dave Rubin'
dave_rubin['podcast'] = 'The Rubin Report'

comedy_bang = 'rss_files/comedy-bang-bang.xml'
comedy_bang = clean_comedy_bang(comedy_bang)
comedy_bang['hosts'] = 'Scott Aukerman'
comedy_bang['podcast'] = 'Comedy Bang Bang'

h3 = 'rss_files/h3.xml'
h3 = clean_h3(h3)
h3['hosts'] = 'Ethan Klein'
h3['podcast'] = 'H3 Podcast'

marc_maron = 'rss_files/marc_maron.xml'
marc_maron = clean_marc_maron(marc_maron)
marc_maron['hosts'] = 'Marc Maron'
marc_maron['podcast'] = 'WTF with Marc Maron Podcast'

joey_diaz = 'rss_files/joey_diaz.xml'
joey_diaz = clean_joey_diaz(joey_diaz)
joey_diaz['hosts'] = 'Joey Diaz'
joey_diaz['podcast'] = "The Church of What's Happening Now: With Joey Coco Diaz"

your_moms_house = 'rss_files/your_moms_house.xml'
your_moms_house = clean_your_moms_house(your_moms_house)
your_moms_house['hosts'] = 'Tom Segura, Christina Pazsitzky'
your_moms_house['podcast'] = "Your Mom's House with Christina P. and Tom Segura"

harmontown = 'rss_files/harmontown.xml'
harmontown = clean_harmontown(harmontown)
harmontown['hosts'] = 'Dan Harmon'
harmontown['podcast'] = 'Harmontown'

stefan_molyneux = 'rss_files/stefan_molyneux.xml'#archives
stefan_molyneux = clean_stefan_molyneux(stefan_molyneux)
stefan_molyneux['hosts'] = 'Stefan Molyneux'
stefan_molyneux['podcast'] = 'Freedomain Radio with Stefan Molyneux'

econtalk = 'rss_files/econtalk.xml'#archives
econtalk = clean_econtalk(econtalk)
econtalk['hosts'] = 'Russ Roberts'
econtalk['podcast'] = 'Econtalk'

econtalk2007 = 'rss_files/econtalk2007.xml'#archives
econtalk2007 = clean_econtalk_archive(econtalk2007)
econtalk2007['hosts'] = 'Russ Roberts'
econtalk2007['podcast'] = 'Econtalk'

econtalk2008 = 'rss_files/econtalk2008.xml'#archives
econtalk2008 = clean_econtalk_archive(econtalk2008)
econtalk2008['hosts'] = 'Russ Roberts'
econtalk2008['podcast'] = 'Econtalk'

econtalk2009 = 'rss_files/econtalk2009.xml'#archives
econtalk2009 = clean_econtalk_archive(econtalk2009)
econtalk2009['hosts'] = 'Russ Roberts'
econtalk2009['podcast'] = 'Econtalk'

econtalk2010 = 'rss_files/econtalk2010.xml'#archives
econtalk2010 = clean_econtalk_archive(econtalk2010)
econtalk2010['hosts'] = 'Russ Roberts'
econtalk2010['podcast'] = 'Econtalk'

econtalk2011 = 'rss_files/econtalk2011.xml'#archives
econtalk2011 = clean_econtalk_archive(econtalk2011)
econtalk2011['hosts'] = 'Russ Roberts'
econtalk2011['podcast'] = 'Econtalk'

econtalk2012 = 'rss_files/econtalk2012.xml'#archives
econtalk2012 = clean_econtalk_archive(econtalk2012)
econtalk2012['hosts'] = 'Russ Roberts'
econtalk2012['podcast'] = 'Econtalk'

econtalk2013 = 'rss_files/econtalk2013.xml'#archives
econtalk2013 = clean_econtalk_archive(econtalk2013)
econtalk2013['hosts'] = 'Russ Roberts'
econtalk2013['podcast'] = 'Econtalk'


bill_maher = 'rss_files/bill_maher.xml'
bill_maher = clean_bill_maher(bill_maher)
bill_maher['hosts'] = 'Bill Maher'
bill_maher['podcast'] = 'Real Time with Bill Maher'

pete_holmes = 'rss_files/pete_holmes.xml'
pete_holmes = clean_pete_holmes(pete_holmes)
pete_holmes['hosts'] = 'Pete Holmes'
pete_holmes['podcast'] = 'You Made It Weird with Pete Holmes'

anna_faris = 'rss_files/anna_faris.xml'
anna_faris = clean_anna_faris(anna_faris)
anna_faris['hosts'] = 'Anna Faris'
anna_faris['podcast'] = 'Anna Faris Is Unqualified'

dax_shepard = 'rss_files/dax_shepard.xml'
dax_shepard = clean_dax_shepard(dax_shepard)
dax_shepard['hosts'] = 'Dax Shepard'
dax_shepard['podcast'] = 'Armchair Expert with Dax Shepard'

grapefruit_simmons = 'rss_files/grapefruit_simmons.xml'
grapefruit_simmons = clean_grapefruit_simmons(grapefruit_simmons)
grapefruit_simmons['hosts'] = 'Greg Fitzsimmons'
grapefruit_simmons['podcast'] = 'Fitzdog Radio'

sam_tripoli = 'rss_files/sam_tripoli.xml'
sam_tripoli = clean_sam_tripoli(sam_tripoli)
sam_tripoli['hosts'] = 'Sam Tripoli'
sam_tripoli['podcast'] = 'Tin Foil Hat With Sam Tripoli'

alison_rosen = 'rss_files/alison_rosen.xml'
alison_rosen = clean_alison_rosen(alison_rosen)
alison_rosen['hosts'] = 'Alison Rosen'
alison_rosen['podcast'] = 'Alison Rosen Is Your New Best Friend'

chris_ryan = 'rss_files/christopher_ryan.xml'
chris_ryan = clean_chris_ryan(chris_ryan)
chris_ryan['hosts'] = 'Christopher Ryan'
chris_ryan['podcast'] = 'Tangentially Speaking with Christopher Ryan'

hdtgm = 'rss_files/how-did-this-get-made.xml'
hdtgm = clean_hdtgm(hdtgm)
hdtgm['hosts'] = 'Paul Scheer, June Diane Raphael, Jason Mantzoukas'
hdtgm['podcast'] = 'How Did This Get Made?'

todd_glass = 'rss_files/todd_glass.xml'
todd_glass = clean_todd_glass(todd_glass)
todd_glass['hosts'] = 'Todd Glass'
todd_glass['podcast'] = 'The Todd Glass Show'

dumb_people_town = 'rss_files/dumb_people_town.xml'
dumb_people_town = clean_dumb_people_town(dumb_people_town)
dumb_people_town['hosts'] = 'Jason Sklar, Randy Sklar'
dumb_people_town['podcast'] = 'Dumb People Town'

doug_loves_movies = 'rss_files/doug_loves_movies.xml'
doug_loves_movies = clean_doug_loves_movies(doug_loves_movies)
doug_loves_movies['hosts'] = 'Doug Benson'
doug_loves_movies['podcast'] = 'Doug Loves Movies'

getting_doug_with_high = 'rss_files/getting_doug_with_high.xml'
getting_doug_with_high = clean_getting_doug_with_high(getting_doug_with_high)
getting_doug_with_high['hosts'] = 'Doug Benson'
getting_doug_with_high['podcast'] = 'Getting Doug with High'

who_charted = 'rss_files/who-charted.xml'
who_charted = clean_who_charted(who_charted)
who_charted['hosts'] = 'Howard Kremer, Kulap Vilaysack'
who_charted['podcast'] = 'Who Charted?'

the_indoor_kids = 'rss_files/the_indoor_kids.xml'
the_indoor_kids = clean_the_indoor_kids(the_indoor_kids)
the_indoor_kids['hosts'] = 'Kumail Nanjiani, Emily V. Gordon'
the_indoor_kids['podcast'] = 'The Indoor Kids with Kumail Nanjiani and Emily V. Gordon'

comedy_film_nerds = 'rss_files/comedy_film_nerds.xml'
comedy_film_nerds = clean_comedy_film_nerds(comedy_film_nerds)
comedy_film_nerds['hosts'] = 'Graham Elwood, Chris Mancini'
comedy_film_nerds['podcast'] = 'Comedy Film Nerds'

the_champs = 'rss_files/the_champs.xml'
the_champs = clean_the_champs(the_champs)
the_champs['hosts'] = 'Neal Brennan, Moshe Kasher'
the_champs['podcast'] = 'The Champs with Neal Brennan + Moshe Kasher'

julian_loves_music = 'rss_files/julian_loves_music.xml'
julian_loves_music = clean_julian_loves_music(julian_loves_music)
julian_loves_music['hosts'] = 'Julian McCullough'
julian_loves_music['podcast'] = 'Julian Loves Music'

chris_cubas = 'rss_files/chris_cubas.xml'
chris_cubas = clean_chris_cubas(chris_cubas)
chris_cubas['hosts'] = 'Chris Cubas'
chris_cubas['podcast'] = 'Canceled'

thomas_thakkar = 'rss_files/thomas_thakkar.xml'
thomas_thakkar = clean_thomas_thakkar(thomas_thakkar)
thomas_thakkar['hosts'] = 'Thomas Thakkar, Tommy McNamara'
thomas_thakkar['podcast'] = 'Stand By Your Band'

iliza = 'rss_files/iliza.xml'
iliza = clean_iliza(iliza)
iliza['hosts'] = 'Iliza Shlesinger'
iliza['podcast'] = 'Truth & Iliza'

race_wars = 'rss_files/race_wars.xml'
race_wars = clean_race_wars(race_wars)
race_wars['hosts'] = 'Kurt Metzger, Sherrod Small'
race_wars['podcast'] = 'Race Wars'

todd_barry = 'rss_files/todd_barry.xml'
todd_barry = clean_todd_barry(todd_barry)
todd_barry['hosts'] = 'Todd Barry'
todd_barry['podcast'] = 'The Todd Barry Podcast'

my_dumb_friends = 'rss_files/my_dumb_friends.xml'
my_dumb_friends = clean_my_dumb_friends(my_dumb_friends)
my_dumb_friends['hosts'] = 'Dan St. Germain, Sean Donnelly'
my_dumb_friends['podcast'] = 'My Dumb Friends'

pleasure_monkey = 'rss_files/pleasure_monkey.xml'
pleasure_monkey = clean_pleasure_monkey(pleasure_monkey)
pleasure_monkey['hosts'] = 'Conner Moore'
pleasure_monkey['podcast'] = 'Pleasure Monkey Podcast'

steven_crowder = 'rss_files/steven_crowder.xml'
steven_crowder = clean_steven_crowder(steven_crowder)
steven_crowder['hosts'] = 'Steven Crowder'
steven_crowder['podcast'] = 'Louder With Crowder'

doughboys = 'rss_files/doughboys.xml'
doughboys = clean_doughboys(doughboys)
doughboys['hosts'] = 'Nick Wiger, Mike Mitchell'
doughboys['podcast'] = 'Doughboys'

bill_simmons = 'rss_files/bill_simmons.xml'
bill_simmons = clean_bill_simmons(bill_simmons)
bill_simmons['hosts'] = 'Bill Simmons'
bill_simmons['podcast'] = 'The Bill Simmons Podcast'

legion_of_skanks = 'rss_files/legion_of_skanks.xml'
legion_of_skanks = clean_legion_of_skanks(legion_of_skanks)
legion_of_skanks['hosts'] = 'Big Jay Oakerson, Luis J. Gomez, Dave Smith'
legion_of_skanks['podcast'] = 'Legion of Skanks Podcast'

punch_drunk_sports = 'rss_files/punch_drunk_sports.xml'
punch_drunk_sports = clean_punch_drunk_sports(punch_drunk_sports)
punch_drunk_sports['hosts'] = 'Ari Shaffir, Sam Tripoli, Jayson Thibault'
punch_drunk_sports['podcast'] = 'Punch Drunk Sports'

hannibal = 'rss_files/hannibal.xml'
hannibal = clean_hannibal(hannibal)
hannibal['hosts'] = 'Hannibal Buress'
hannibal['podcast'] = 'Hannibal Buress: Handsome Rambler'

tait_fletcher = 'rss_files/tait_fletcher.xml'
tait_fletcher = clean_tait_fletcher(tait_fletcher)
tait_fletcher['hosts'] = 'Tait Fletcher'
tait_fletcher['podcast'] = 'Pirate Life Radio with Tait Fletcher'

steve_rannazzisi = 'rss_files/steve_rannazzisi.xml'
steve_rannazzisi = clean_steve_rannazzisi(steve_rannazzisi)
steve_rannazzisi['hosts'] = 'Steve Rannazzisi'
steve_rannazzisi['podcast'] = 'Hear Me This Book'

jim_rome = 'rss_files/jim_rome.xml'
jim_rome = clean_jim_rome(jim_rome)
jim_rome['hosts'] = 'Jim Rome'
jim_rome['podcast'] = 'The Jim Rome Podcast'

sklar_brothers = 'rss_files/sklar_brothers.xml'
sklar_brothers = clean_sklar_brothers(sklar_brothers)
sklar_brothers['hosts'] = 'Jason Sklar, Randy Sklar'
sklar_brothers['podcast'] = 'View from the Cheap Seats with the Sklar Brothers'

all_things_comedy = 'rss_files/all_things_comedy.xml'
all_things_comedy = clean_all_things_comedy(all_things_comedy)
all_things_comedy['hosts'] = 'Bill Burr, Al Madrigal'
all_things_comedy['podcast'] = 'All Things Comedy Live'

dom_irrera = 'rss_files/dom_irrera.xml'
dom_irrera = clean_dom_irrera(dom_irrera)
dom_irrera['hosts'] = 'Dom Irrera'
dom_irrera['podcast'] = 'Dom Irrera Live from the Laugh Factory'

aubrey_marcus = 'rss_files/aubrey_marcus.xml'
aubrey_marcus = clean_aubrey_marcus(aubrey_marcus)
aubrey_marcus['hosts'] = 'Aubrey Marcus'
aubrey_marcus['podcast'] = 'Aubrey Marcus Podcast'

happy_sad_confused = 'rss_files/happy_sad_confused.xml'
happy_sad_confused = clean_happy_sad_confused(happy_sad_confused)
happy_sad_confused['hosts'] = 'Josh Horowitz'
happy_sad_confused['podcast'] = 'Happy Sad Confused'

sam_jones = 'rss_files/sam_jones.xml'
sam_jones = clean_sam_jones(sam_jones)
sam_jones['hosts'] = 'Sam Jones'
sam_jones['podcast'] = 'Off Camera with Sam Jones'

maltin = 'rss_files/maltin.xml'
maltin = clean_maltin(maltin)
maltin['hosts'] = 'Leonard Maltin, Jessie Maltin'
maltin['podcast'] = 'Maltin on Movies'

guy_raz = 'rss_files/guy_raz.xml'
guy_raz = clean_guy_raz(guy_raz)
guy_raz['hosts'] = 'Guy Raz'
guy_raz['podcast'] = 'How I Built This with Guy Raz'

modern_love = 'rss_files/modern_love.xml'
modern_love = clean_modern_love(modern_love)
modern_love['hosts'] = 'Meghna Chakrabarti'
modern_love['podcast'] = 'Modern Love'

lewis_howes = 'rss_files/lewis_howes.xml'
lewis_howes = clean_lewis_howes(lewis_howes)
lewis_howes['hosts'] = 'Lewis Howes'
lewis_howes['podcast'] = 'The School of Greatness'

ringer_nba = 'rss_files/ringer_nba.xml'
ringer_nba = clean_ringer_nba(ringer_nba)
ringer_nba['hosts'] = 'Chris Ryan, Justin Verrier, Kevin O’Connor, Jonathan Tjarks, Juliet Litman, Chris Vernon, John Gonzalez, Jonathan Tjarks'
ringer_nba['podcast'] = 'The Ringer NBA Show'

mike_lupica = 'rss_files/mike_lupica.xml'
mike_lupica = clean_mike_lupica(mike_lupica)
mike_lupica['hosts'] = 'Mike Lupica'
mike_lupica['podcast'] = 'The Mike Lupica Show'

ask_me_another = 'rss_files/ask_me_another.xml'
ask_me_another = clean_ask_me_another(ask_me_another)
ask_me_another['hosts'] = 'Ophira Eisenberg'
ask_me_another['podcast'] = 'Ask Me Another'

dear_sugars = 'rss_files/dear_sugars.xml'
dear_sugars = clean_dear_sugars(dear_sugars)
dear_sugars['hosts'] = 'Cheryl Strayed, Steve Almond'
dear_sugars['podcast'] = 'Dear Sugars'

bugle = 'rss_files/bugle.xml'
bugle = clean_bugle(bugle)
bugle['hosts'] = 'Andy Zaltzman'
bugle['podcast'] = 'The Bugle'

daily_zeitgeist = 'rss_files/daily_zeitgeist.xml'
daily_zeitgeist = clean_daily_zeitgeist(daily_zeitgeist)
daily_zeitgeist['hosts'] = 'Jack O’Brien'
daily_zeitgeist['podcast'] = 'The Daily Zeitgeist'

smodcast = 'rss_files/smodcast.xml'
smodcast = clean_smodcast(smodcast)
smodcast['hosts'] = 'Kevin Smith, Scott Mosier'
smodcast['podcast'] = 'SModcast'

rapaport = 'rss_files/rapaport.xml'
rapaport = clean_rapaport(rapaport)
rapaport['hosts'] = 'Michael Rapaport'
rapaport['podcast'] = 'I AM RAPAPORT: STEREO PODCAST'

jimmy_pardo = 'rss_files/jimmy_pardo.xml'
jimmy_pardo = clean_jimmy_pardo(jimmy_pardo)
jimmy_pardo['hosts'] = 'Jimmy Pardo'
jimmy_pardo['podcast'] = 'Never Not Funny: The Jimmy Pardo Podcast'

crabfeast = 'rss_files/crabfeast.xml'
crabfeast = clean_crabfeast(crabfeast)
crabfeast['hosts'] = 'Ryan Sickler, Jay Larson'
crabfeast['podcast'] = 'The CrabFeast with Ryan Sickler and Jay Larson'

matt_besser = 'rss_files/matt_besser.xml'
matt_besser = clean_matt_besser(matt_besser)
matt_besser['hosts'] = 'Matt Besser'
matt_besser['podcast'] = 'improv4humans with Matt Besser'

gilbert_gottfried = 'rss_files/gilbert_gottfried.xml'
gilbert_gottfried = clean_gilbert_gottfried(gilbert_gottfried)
gilbert_gottfried['hosts'] = 'Gilbert Gottfried'
gilbert_gottfried['podcast'] = "Gilbert Gottfried's Amazing Colossal Podcast"

jordan_jesse_go = 'rss_files/jordan_jesse_go.xml'
jordan_jesse_go = clean_jordan_jesse_go(jordan_jesse_go)
jordan_jesse_go['hosts'] = 'Jesse Thorn, Jordan Morris'
jordan_jesse_go['podcast'] = 'Jordan, Jesse GO!'

jesse_thorn = 'rss_files/jesse_thorn.xml'
jesse_thorn = clean_jesse_thorn(jesse_thorn)
jesse_thorn['hosts'] = 'Jesse Thorn'
jesse_thorn['podcast'] = 'Bullseye with Jesse Thorn'

stop_podcasting_yourself = 'rss_files/stop_podcasting_yourself.xml'
stop_podcasting_yourself = clean_stop_podcasting_yourself(stop_podcasting_yourself)
stop_podcasting_yourself['hosts'] = 'Graham Clark, Dave Shumka'
stop_podcasting_yourself['podcast'] = 'Stop Podcasting Yourself'

spontaneanation = 'rss_files/spontaneanation.xml'
spontaneanation = clean_spontaneanation(spontaneanation)
spontaneanation['hosts'] = 'Paul F. Tompkins'
spontaneanation['podcast'] = 'SPONTANEANATION with Paul F. Tompkins'

tompkast = 'rss_files/tompkast.xml'
tompkast = clean_tompkast(tompkast)
tompkast['hosts'] = 'Paul F. Tompkins'
tompkast['podcast'] = 'The Pod F. Tompkast'

dead_authors = 'rss_files/dead_authors.xml'
dead_authors = clean_dead_authors(dead_authors)
dead_authors['hosts'] = 'Paul F. Tompkins'
dead_authors['podcast'] = 'The Dead Authors Podcast'

bone_zone = 'rss_files/bone_zone.xml'
bone_zone = clean_bone_zone(bone_zone)
bone_zone['hosts'] = 'Brendon Walsh, Randy Liedtke'
bone_zone['podcast'] = 'The Bone Zone'

economic_rockstar = 'rss_files/economic_rockstar.xml'
economic_rockstar = clean_economic_rockstar(economic_rockstar)
economic_rockstar['hosts'] = 'Frank Conway'
economic_rockstar['podcast'] = 'Economic Rockstar'

john_roy = 'rss_files/john_roy.xml'
john_roy = clean_john_roy(john_roy)
john_roy['hosts'] = 'John Roy'
john_roy['podcast'] = "Don't Ever Change with John Roy"

kurt_braunohler = 'rss_files/kurt_braunohler.xml'
kurt_braunohler = clean_kurt_braunohler(kurt_braunohler)
kurt_braunohler['hosts'] = 'Kurt Braunohler'
kurt_braunohler['podcast'] = "The K Ohle with Kurt Braunohler"

steve_agee = 'rss_files/steve_agee.xml'
steve_agee = clean_steve_agee(steve_agee)
steve_agee['hosts'] = 'Steve Agee'
steve_agee['podcast'] = 'Steve Agee: Uhhh'

jon_gabrus = 'rss_files/jon_gabrus.xml'
jon_gabrus = clean_jon_gabrus(jon_gabrus)
jon_gabrus['hosts'] = 'Jon Gabrus'
jon_gabrus['podcast'] = 'High and Mighty'

x_files = 'rss_files/x_files.xhtml'
x_files = clean_x_files(x_files)
x_files['hosts'] = 'Kumail Nanjiani'
x_files['podcast'] = "Kumail Nanjiani's The X-Files Files"

jonathan_van_ness = 'rss_files/jonathan_van_ness.xml'
jonathan_van_ness = clean_jonathan_van_ness(jonathan_van_ness)
jonathan_van_ness['hosts'] = 'Jonathan Van Ness'
jonathan_van_ness['podcast'] = "Getting Curious with Jonathan Van Ness"

hollywood_handbook = 'rss_files/hollywood-handbook.xml'
hollywood_handbook = clean_hollywood_handbook(hollywood_handbook)
hollywood_handbook['hosts'] = 'Hayes Davenport, Sean Clements'
hollywood_handbook['podcast'] = 'Hollywood Handbook'

rupaul = 'rss_files/rupaul.xml'
rupaul = clean_rupaul(rupaul)
rupaul['hosts'] = 'RuPaul, Michelle Visage'
rupaul['podcast'] = "RuPaul: What's The Tee with Michelle Visage"

shane_dawson = 'rss_files/shane_dawson.xml'
shane_dawson = clean_shane_dawson(shane_dawson)
shane_dawson['hosts'] = 'Shane Dawson'
shane_dawson['podcast'] = 'Shane And Friends'

grace_helbig = 'rss_files/grace_helbig.xml'
grace_helbig = clean_grace_helbig(grace_helbig)
grace_helbig['hosts'] = 'Grace Helbig, Jack Ferry'
grace_helbig['podcast'] = 'Not Too Deep with Grace Helbig'

think_again = 'rss_files/think_again.xml'
think_again = clean_think_again(think_again)
think_again['hosts'] = 'Jason Gots'
think_again['podcast'] = 'Think Again – a Big Think Podcast'

rationally_speaking = 'rss_files/rationally_speaking.xml'
rationally_speaking = clean_rationally_speaking(rationally_speaking)
rationally_speaking['hosts'] = 'Julia Galef'
rationally_speaking['podcast'] = 'Rationally Speaking'

rationally_speaking = 'rss_files/rationally_speaking.xml'
rationally_speaking = clean_rationally_speaking(rationally_speaking)
rationally_speaking['hosts'] = 'Julia Galef'
rationally_speaking['podcast'] = 'Rationally Speaking'

skepticality = 'rss_files/skepticality.xml'
skepticality = clean_skepticality(skepticality)
skepticality['hosts'] = 'Derek Colanduno, Robynn McCarthy'
skepticality['podcast'] = 'Skepticality: The Official Podcast of Skeptic Magazine'

friendly_atheist = 'rss_files/friendly_atheist.xml'
friendly_atheist = clean_friendly_atheist(friendly_atheist)
friendly_atheist['hosts'] = 'Hemant Mehta'
friendly_atheist['podcast'] = 'Friendly Atheist Podcast'

snoop = 'rss_files/snoop.xml'
snoop = clean_snoop(snoop)
snoop['hosts'] = 'Snoop Dogg'
snoop['podcast'] = "Snoop Dogg's GGN Podcast"

katie_couric = 'rss_files/katie_couric.xml'
katie_couric = clean_katie_couric(katie_couric)
katie_couric['hosts'] = 'Katie Couric'
katie_couric['podcast'] = 'Katie Couric'

etl = 'rss_files/etl.xml'
etl = clean_etl(etl)
etl['hosts'] = 'Tina Seelig'
etl['podcast'] = 'Entrepreneurial Thought Leaders'

ezra_klein = 'rss_files/ezra_klein.xml'
ezra_klein = clean_ezra_klein(ezra_klein)
ezra_klein['hosts'] = 'Ezra Klein'
ezra_klein['podcast'] = 'The Ezra Klein Show'

john_gruber = 'rss_files/john_gruber.xml'
john_gruber = clean_john_gruber(john_gruber)
john_gruber['hosts'] = 'John Gruber'
john_gruber['podcast'] = 'The Talk Show With John Gruber'

shane_mauss = 'rss_files/shane_mauss.xml'
shane_mauss = clean_shane_mauss(shane_mauss)
shane_mauss['hosts'] = 'Shane Mauss'
shane_mauss['podcast'] = 'Here We Are'

double_date = 'rss_files/double_date.xml'
double_date = clean_double_date(double_date)
double_date['hosts'] = 'Shane Mauss, April Macie'
double_date['podcast'] = 'Double Date Podcast'

zach_leary = 'rss_files/zach_leary.xml'
zach_leary = clean_zach_leary(zach_leary)
zach_leary['hosts'] = 'Zach Leary'
zach_leary['podcast'] = "It's All Happening"

cory_allen = 'rss_files/cory_allen.xml'
cory_allen = clean_cory_allen(cory_allen)
cory_allen['hosts'] = 'Cory Allen'
cory_allen['podcast'] = 'The Astral Hustle with Cory Allen'

raghu_markus = 'rss_files/raghu_markus.xml'
raghu_markus = clean_raghu_markus(raghu_markus)
raghu_markus['hosts'] = 'Raghu Markus'
raghu_markus['podcast'] = 'Mindrolling with Raghu Markus'

chris_grosso = 'rss_files/chris_grosso.xml'
chris_grosso = clean_chris_grosso(chris_grosso)
chris_grosso['hosts'] = 'Chris Grosso'
chris_grosso['podcast'] = 'Chris Grosso The Indie Spiritualist'

london_real = 'rss_files/london_real.xml'
london_real = clean_london_real(london_real)
london_real['hosts'] = 'Brian Rose'
london_real['podcast'] = 'London Real'

onnit = 'rss_files/onnit.xml'
onnit = clean_onnit(onnit)
onnit['hosts'] = 'Aubrey Marcus'
onnit['podcast'] = 'Onnit Podcast'

festival_of_sports = 'rss_files/festival_of_sports.xml'
festival_of_sports = clean_festival_of_sports(festival_of_sports)
festival_of_sports['hosts'] = 'Brody Stevens'
festival_of_sports['podcast'] = 'Brody Stevens Festival Of Sports'

brody_stevens = 'rss_files/brody_stevens.xml'
brody_stevens = clean_brody_stevens(brody_stevens)
brody_stevens['hosts'] = 'Brody Stevens'
brody_stevens['podcast'] = 'The Steven Brody Stevens Festival Of Friendship'

wwdtm = 'rss_files/wwdtm.xml'
wwdtm = clean_wwdtm(wwdtm)
wwdtm['hosts'] = 'Peter Sagal'
wwdtm['podcast'] = "Wait Wait... Don't Tell Me!"

superego = 'rss_files/superego.xml'
superego = clean_superego(superego)
superego['hosts'] = 'Matt Gourley, Jeremy Carter, Mark McConville, Paul F. Tompkins'
superego['podcast'] = 'Superego'

dan_savage = 'rss_files/dan_savage.xml'
dan_savage = clean_dan_savage(dan_savage)
dan_savage['hosts'] = 'Dan Savage'
dan_savage['podcast'] = 'Savage Lovecast'

tom_rhodes = 'rss_files/tom_rhodes.xml'
tom_rhodes = clean_tom_rhodes(tom_rhodes)
tom_rhodes['hosts'] = 'Tom Rhodes'
tom_rhodes['podcast'] = 'Tom Rhodes Radio Smart Camp'

full_charge = 'rss_files/full_charge.xml'
full_charge = clean_full_charge(full_charge)
full_charge['hosts'] = 'Matt Fulchiron'
full_charge['podcast'] = 'The Full Charge Power Hour featuring Matt Fulchiron'

brandt_tobler = 'rss_files/brandt_tobler.xml'
brandt_tobler = clean_brandt_tobler(brandt_tobler)
brandt_tobler['hosts'] = 'Brandt Tobler'
brandt_tobler['podcast'] = 'The 31 with Brandt Tobler'

steve_simeone = 'rss_files/steve_simeone.xml'
steve_simeone = clean_steve_simeone(steve_simeone)
steve_simeone['hosts'] = 'Steve Simeone'
steve_simeone['podcast'] = 'Good Times: With Steve Simeone'

johnny_pemberton = 'rss_files/johnny_pemberton.xml'
johnny_pemberton = clean_johnny_pemberton(johnny_pemberton)
johnny_pemberton['hosts'] = 'Johnny Pemberton'
johnny_pemberton['podcast'] = 'Twisting The Wind with Johnny Pemberton'

live_to_tape = 'rss_files/live_to_tape.xml'
live_to_tape = clean_live_to_tape(live_to_tape)
live_to_tape['hosts'] = 'Johnny Pemberton'
live_to_tape['podcast'] = 'LIVE TO TAPE with Johnny Pemberton'

jay_mohr = 'rss_files/jay_mohr.xml'
jay_mohr = clean_jay_mohr(jay_mohr)
jay_mohr['hosts'] = 'Jay Mohr'
jay_mohr['podcast'] = 'Mohr Stories with Jay Mohr'

pony_hour = 'rss_files/pony_hour.xml'
pony_hour = clean_pony_hour(pony_hour)
pony_hour['hosts'] = 'Tony Hinchcliffe'
pony_hour['podcast'] = 'The Pony Hour'

jocko = 'rss_files/jocko.xml'
jocko = clean_jocko(jocko)
jocko['hosts'] = 'Jocko Willink, Echo Charles'
jocko['podcast'] = 'Jocko Podcast'

tim_ferriss = 'rss_files/tim-ferriss-show.xml'
tim_ferriss = clean_tim_ferriss(tim_ferriss)
tim_ferriss['hosts'] = 'Tim Ferriss'
tim_ferriss['podcast'] = 'The Tim Ferriss Show'

star_talk = 'rss_files/star_talk.xml'
star_talk = clean_star_talk(star_talk)
star_talk['hosts'] = 'Neil deGrasse Tyson'
star_talk['podcast'] = 'StarTalk Radio'

doug_stanhope = 'rss_files/doug_stanhope.xml'
doug_stanhope = clean_doug_stanhope(doug_stanhope)
doug_stanhope['hosts'] = 'Doug Stanhope'
doug_stanhope['podcast'] = 'The Doug Stanhope Podcast'

bitch_sesh = 'rss_files/bitch_sesh.xml'
bitch_sesh = clean_bitch_sesh(bitch_sesh)
bitch_sesh['hosts'] = 'Casey Wilson, Danielle Schneider'
bitch_sesh['podcast'] = 'Bitch Sesh: A Real Housewives Breakdown'

cam_rhea = 'rss_files/cam_rhea.xml'
cam_rhea = clean_cam_rhea(cam_rhea)
cam_rhea['hosts'] = 'Cameron Esposito, Rhea Butcher'
cam_rhea['podcast'] = 'Put Your Hands Together with Cam and Rhea'

andy_cohen = 'rss_files/andy_cohen.xml'
andy_cohen = clean_andy_cohen(andy_cohen)
andy_cohen['hosts'] = 'Andy Cohen'
andy_cohen['podcast'] = 'Watch What Happens Live with Andy Cohen'

rap_radar = 'rss_files/rap_radar.xml'
rap_radar = clean_rap_radar(rap_radar)
rap_radar['hosts'] = 'Elliott Wilson, Brian Miller'
rap_radar['podcast'] = 'Rap Radar Podcast'

vlad_couch = 'rss_files/vlad_couch.xml'
vlad_couch = clean_vlad_couch(vlad_couch)
vlad_couch['hosts'] = 'DJ Vlad'
vlad_couch['podcast'] = 'The Vlad Couch'

allegedly = 'rss_files/allegedly.xml'
allegedly = clean_allegedly(allegedly)
allegedly['hosts'] = 'Theo Von, Matthew Cole Weiss'
allegedly['podcast'] = 'Allegedly with Theo Von & Matthew Cole Weiss'

this_life = 'rss_files/this_life.xml'
this_life = clean_this_life(this_life)
this_life['hosts'] = 'Dr. Drew, Bob Forrest'
this_life['podcast'] = 'This Life #YOULIVE With Dr Drew'

friends_like_these = 'rss_files/friends_like_these.xml'
friends_like_these = clean_friends_like_these(friends_like_these)
friends_like_these['hosts'] = 'Ana Marie Cox'
friends_like_these['podcast'] = 'With Friends Like These'

axe_files = 'rss_files/axe_files.xml'
axe_files = clean_axe_files(axe_files)
axe_files['hosts'] = 'David Axelrod'
axe_files['podcast'] = 'The Axe Files with David Axelrod'

politically_reactive = 'rss_files/politically_reactive.xml'
politically_reactive = clean_politically_reactive(politically_reactive)
politically_reactive['hosts'] = 'W. Kamau Bell, Hari Kondabolu'
politically_reactive['podcast'] = 'Politically Re-Active with W. Kamau Bell & Hari Kondabolu'

james_altucher = 'rss_files/james_altucher.xml'
james_altucher = clean_james_altucher(james_altucher)
james_altucher['hosts'] = 'James Altucher'
james_altucher['podcast'] = 'The James Altucher Show'

bulletproof_radio = 'rss_files/bulletproof_radio.xml'
bulletproof_radio = clean_bulletproof_radio(bulletproof_radio)
bulletproof_radio['hosts'] = 'Dave Asprey'
bulletproof_radio['podcast'] = 'Bulletproof Radio'

chris_kresser = 'rss_files/chris_kresser.xml'
chris_kresser = clean_chris_kresser(chris_kresser)
chris_kresser['hosts'] = 'Chris Kresser'
chris_kresser['podcast'] = 'Revolution Health Radio'

ufc_unfiltered = 'rss_files/ufc_unfiltered.xml'
ufc_unfiltered = clean_ufc_unfiltered(ufc_unfiltered)
ufc_unfiltered['hosts'] = 'Jim Norton, Matt Serra'
ufc_unfiltered['podcast'] = 'UFC Unfiltered with Jim Norton and Matt Serra'

dan_harris = 'rss_files/dan_harris.xml'
dan_harris = clean_dan_harris(dan_harris)
dan_harris['hosts'] = 'Dan Harris'
dan_harris['podcast'] = '10% Happier with Dan Harris'

supersoul = 'rss_files/supersoul.xml'
supersoul = clean_supersoul(supersoul)
supersoul['hosts'] = 'Oprah Winfrey'
supersoul['podcast'] = "Oprah’s SuperSoul Conversations"

df = pd.concat([joe_rogan, duncan_trussel, bert_kreischer, tfatk, ari_shaffir,
               russell_brand, kevin_pereira, chris_hardwick, sam_harris,
               kill_tony, dave_rubin, comedy_bang, h3, marc_maron,
               joey_diaz, your_moms_house, harmontown, stefan_molyneux,
               econtalk, econtalk2007, econtalk2008, econtalk2009,
               econtalk2010, econtalk2011, econtalk2012, econtalk2013,
               bill_maher, pete_holmes, anna_faris, dax_shepard,
               grapefruit_simmons, sam_tripoli, alison_rosen, chris_ryan,
               hdtgm, todd_glass, dumb_people_town, doug_loves_movies,
               getting_doug_with_high, who_charted, the_indoor_kids,
               comedy_film_nerds, the_champs, julian_loves_music, chris_cubas,
               thomas_thakkar, iliza, race_wars, todd_barry, my_dumb_friends,
               pleasure_monkey, steven_crowder, doughboys, bill_simmons,
               legion_of_skanks, punch_drunk_sports, hannibal, tait_fletcher,
               steve_rannazzisi, jim_rome, sklar_brothers, all_things_comedy,
               dom_irrera, aubrey_marcus, happy_sad_confused, sam_jones, maltin,
               guy_raz, modern_love, lewis_howes, ringer_nba, mike_lupica,
               ask_me_another, dear_sugars, bugle, daily_zeitgeist,
               smodcast, rapaport, jimmy_pardo, crabfeast, matt_besser,
               gilbert_gottfried, jordan_jesse_go, jesse_thorn,
               stop_podcasting_yourself, spontaneanation, tompkast,
               dead_authors, bone_zone, economic_rockstar, john_roy,
               kurt_braunohler, steve_agee, jon_gabrus, x_files,
               jonathan_van_ness, hollywood_handbook, rupaul, shane_dawson,
               grace_helbig, think_again, rationally_speaking, skepticality,
               friendly_atheist, snoop, katie_couric, etl, ezra_klein,
               john_gruber, shane_mauss, double_date, zach_leary, cory_allen,
               raghu_markus, chris_grosso, london_real, onnit, festival_of_sports,
               brody_stevens, wwdtm, superego, dan_savage, tom_rhodes,
               full_charge, brandt_tobler, steve_simeone, johnny_pemberton,
               live_to_tape, jay_mohr, pony_hour, jocko, tim_ferriss,
               star_talk, doug_stanhope, bitch_sesh, cam_rhea, andy_cohen,
               rap_radar, vlad_couch, allegedly, this_life, friends_like_these,
               axe_files, politically_reactive, james_altucher, bulletproof_radio,
               chris_kresser, ufc_unfiltered, dan_harris, supersoul], ignore_index=True)


df['guests'] = [g.rstrip() for g in df['guests']]
df['guests'] = [g.lstrip() for g in df['guests']]

df['podcast_id'] = ''

podcast_info = pd.read_csv('meta_podcast_info.csv', sep='\t', index_col=0)
d = {}
for index, row in podcast_info.iterrows():
	d[row['Podcast Name']]=index-1

print(d)

for index1, row1 in df.iterrows():
	print(row1['podcast'], d[row1['podcast']])
	df.at[index1, 'podcast_id']=d[row1['podcast']]
	# row1['podcast_id']=d[row1['podcast']]

print(df['podcast_id'])


df.to_csv('cleaned_podcasts.csv', sep='\t')


