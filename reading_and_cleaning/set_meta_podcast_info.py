from pandas import DataFrame


podcast_info = DataFrame(columns=['Podcast Name', 'Hosts', 'feedURL', 'imageURL', 'categories','keywords', 'cleaner'])

podcast_info.loc[1] = ['The Joe Rogan Experience', ['Joe Rogan'], 'http://joeroganexp.joerogan.libsynpro.com/rss', 
                       'http://static.libsyn.com/p/assets/7/1/f/3/71f3014e14ef2722/JREiTunesImage2.jpg',
                       ['Comedy', 'Society and Culture', 'Technology'], 'comedian,joe,monkey,redban,rogan,talking,ufc',
                       'clean_joe_rogan']

podcast_info.loc[2] = ['The Duncan Trussell Family Hour', ['Duncan Trussell'], 'http://feeds.feedburner.com/DuncanTrussell',
                       'https://dfkfj8j276wwv.cloudfront.net/images/a5/61/da/36/a561da36-4f52-4e99-8dd8-39327127d1a4/5da29f0114e2bd9452a227692e5b6a128325544f2bf8d3eccac16f0989ae4202d9cacd3c462a1e2cff821dc6d38e279aa756834b237b3c83714c0b0a8e9130f9.jpeg',
                       ['Comedy', 'Arts', 'Religion and Spirituality'], '',
                       'clean_duncan_trussel']

podcast_info.loc[3] = ["Bertcast's podcast", ['Bert Kreischer'], 'http://bertcast.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/0/c/7/c/0c7ceaa632f83139/1400x1400Bertcast.jpg',
                      ['Comedy'], 'bert,kreischer,machine,the',
                      'clean_bert_kreischer']

podcast_info.loc[4] = ['The Fighter & The Kid', ['Brendan Schaub', 'Bryan Callen'], 'https://rss.art19.com/fighter-and-the-kid',
                       'https://dfkfj8j276wwv.cloudfront.net/images/b8/c5/2e/ce/b8c52ece-79d2-46f9-81bf-6cce4dc77800/bfd625393db10277d5c303ca78375af9e7c5bb59da46752add461ef74adfdf555b1c523849be889ec5ad88756e46b38944d985093671fd95fcbc03ed697d4129.jpeg',
                      ['Sports & Recreation', 'Society & Culture', 'Comedy'], 'bellator,ufcfightnight,mixed martial arts,ufc fight night,fight night,ufc event,funny,Comedy,Brendan Schaub,Bryan Callen,Ultimate Fighting Championship,ufc,MMA',
                      'clean_tfatk']

podcast_info.loc[5] = ["Ari Shaffir's Skeptic Tank", ['Ari Shaffir'], 'http://shaffir1.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/b/4/2/5/b4254b9d8fe44416/SkepticTank_cover4.jpg',
                      ['Comedy', 'Education'], 'allthingscomedy,ari,arithegreat,burr,comedy,death,deathsquad,diaz,duncan,freak,joe,joey,kreischer,party,punchdrunk,rogan,sceptic,segura,septic,shaffir,shafir,skeptic,squad,store,tank,thisisnothappening,trussell',
                      'clean_ari_shaffir']

podcast_info.loc[6] = ['Under The Skin with Russell Brand', ['Russell Brand'], 'https://rss.art19.com/under-the-skin',
                       'https://dfkfj8j276wwv.cloudfront.net/images/96/ea/83/97/96ea8397-cf58-431e-8dd9-52076598956f/116d59ed2835d58004391beaa0d2642c26f3739452e996f20b13384f54eee5db752a71c1a70e0922941daf8b746395f6bf4758a6d593654fd595aaa04c4234af.jpeg',
                      ['Comedy', 'Society & Culture', 'Philosophy'], '',
                      'clean_russell_brand']

podcast_info.loc[7] = ['Pointless: with Kevin Pereira', ['Kevin Pereira'], 'http://pointlesspod.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/b/c/b/c/bcbccaff844fdfb6/Pointless_Logo.png',
                      ['Comedy'], 'attack,attackoftheshow,g4,hackmylife,kevinpereira,pointless',
                      'clean_kevin_pereira']

podcast_info.loc[8] = ['ID10T with Chris Hardwick', ['Chris Hardwick'], 'https://rss.art19.com/id10t',
                      'https://dfkfj8j276wwv.cloudfront.net/images/58/a1/cf/f4/58a1cff4-2127-476f-a386-eb043b863a7a/577d912b5d1f36c085da75e9b1590c392669d508757552874e76c4d4d1fe8d0143ed8b003d90b5a6e8eb5ef72763a9f889c5ca7818e8d5dc4740ffab7e19d414.jpeg',
                      ['Comedy'], 'ID10T,hardwick',
                      'clean_chris_hardwick']

podcast_info.loc[9] = ['Waking Up with Sam Harris', ['Sam Harris'], 'http://wakingup.libsyn.com/rss',
                      'http://static.libsyn.com/p/assets/0/b/e/4/0be4dc9e0fc61265/podcast_art_alt_1.5.18.jpg',
                      ['Science & Medicine', 'Society & Culture', 'Religion & Spirituality'], 'currentevents,ethics,neuroscience,philosophy,politics,religion,samharris,science',
                      'clean_sam_harris']

podcast_info.loc[10] = ['Kill Tony', ['Tony Hinchcliffe', 'Brian Redban'], 'http://www.deathsquad.tv/feed/',
                       'http://is1.mzstatic.com/image/thumb/Music62/v4/a2/28/46/a22846be-aa37-a34f-b0b1-82f2eda98fff/source/1200x630bb.jpg',
                       ['Comedy', 'Technology', 'TV & Film'], '',
                       'clean_kill_tony']

podcast_info.loc[11] = ['The Rubin Report', ['Dave Rubin'], 'https://rss.art19.com/the-rubin-report',
                       'https://dfkfj8j276wwv.cloudfront.net/images/26/c5/8b/5a/26c58b5a-3265-47af-baa3-8fcb03552e8b/1667b2b70b03d6be83ea88721bba31e5a3b1163b34be18d15dc871ab51ec406353f7fa688c37e521bd87211ad78acc268c0cc7b860c196b611674f2dd0b3786e.jpeg',
                       ['News & Politics', 'Comedy', 'Society & Culture'], 'world news,real time,political news,bill maher,the daily show,the rubin report,political comedy,Rubin Report ,Interview Politics,Dave Rubin,news channel,Talk Show,political correctness,joe rogan,celebrity,breaking news,free speech,current events,technology,entertainment,news',
                       'clean_dave_rubin']

podcast_info.loc[12] = ['Comedy Bang Bang', ['Scott Aukerman'], 'http://rss.earwolf.com/comedy-bang-bang',
                       'https://dfkfj8j276wwv.cloudfront.net/images/9f/09/33/49/9f093349-89d6-436b-ad97-1e6de2bc95e4/f5549c7f8f4b94c14765e5d186cbd701a8e30673abe6afc4cd8d3e3280a60b403371cc6c53dd99c5a96c091f5d8f052a7034d3f1c3532078a7b494b62094ce0f.jpeg',
                       ['Comedy'], '',
                       'clean_comedy_bang']

podcast_info.loc[13] = ['H3 Podcast', ['Ethan Klein'], 'http://h3h3roost.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/4/4/3/c/443cb5e4b2df7938/NEW_Podcast_Logo_SQUARE.png',
                       ['Comedy'], 'comedy,entertainment,ethan,ethanklein,h3,h3h3,h3h3productions,h3podcast,hila,hilaklein,interview,klein',
                       'clean_h3']

podcast_info.loc[14] = ['WTF with Marc Maron Podcast', ['Marc Maron'], 'http://wtfpod.libsyn.com/rss', 
                       'http://static.libsyn.com/p/assets/6/c/a/3/6ca38c2fefa1e989/WTF_-_new_larger_cover.jpg',
                       ['Comedy', 'Arts', 'Performing Arts', 'TV & Film'], '',
                       'clean_marc_maron']

podcast_info.loc[15] = ["The Church of What's Happening Now: With Joey Coco Diaz", ['Joey Diaz'], 'http://thechurchofwhatshappeningnow.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/0/9/2/b/092b6071107e1f7d/itunes.jpg',
                       ['Comedy'], 'comedy,diaz,joey,music',
                       'clean_joey_diaz']

podcast_info.loc[16] = ["Your Mom's House with Christina P. and Tom Segura", ['Tom Segura', 'Christina Pazsitzky'], 'http://feeds.feedburner.com/YourMomsHouseWithChristinaPazsitzkyAndTomSegura',
                       'http://static.libsyn.com/p/assets/f/a/9/9/fa99383b96617676/YMH_ATCcover_1.jpg',
                       ['Comedy'], 'tom,segura,christina,pazsitzky,dry,sarcastic,philosophy,wipe,dumps,coffee,teeth,dental,dudes,balls,gay,fart',
                       'clean_your_moms_house']

podcast_info.loc[17] = ['Harmontown', ['Dan Harmon'], 'http://feeds.feedburner.com/HarmontownPodcast',
                       'https://dfkfj8j276wwv.cloudfront.net/images/89/a3/a0/38/89a3a038-05d1-494d-b1e1-0c4767fccdd8/675f78e08433fc7acfa1d068f9455065988e39d6676f6570e99b295f832fe96c8a6df5bb8d06873a33266c5f66b47cce870543d99e9bf3e7d88d780d6475a373.jpeg',
                       ['Comedy'], '',
                       'clean_harmontown']

podcast_info.loc[18] = ['Freedomain Radio with Stefan Molyneux', ['Stefan Molyneux'], 'http://feeds.feedburner.com/FreedomainRadioVolume6',
                       'http://www.freedomainradio.com/images/xmlfeed/iTunes_Podcast_Avatar_Latest.png',
                       ['News & Politics', 'Education/Higher Education', 'Religion & Spirituality', 'Society & Culture/Philosophy', 'Society & Culture/History', 'News & Politics', 'Education', 'Higher Education', 'Religion & Spirituality', 'Society & Culture', 'Philosophy', 'Society & Culture', 'History'], 'state,god,family,atheism,atheist,anarchy,anarchism,government,freedomain,libertarian,podcast,podcasts,radio,stefan,stephen,stephan,molyneux,violence,philosophy,history,economics,classical,liberalism,capitalism,freedom,free,market,joe,rogan,ron,paul',
                       'clean_stefan_molyneux']

podcast_info.loc[19] = ['Econtalk', ['Russ Roberts'], 'http://files.libertyfund.org/econtalk/EconTalk.xml',
                       'http://files.libertyfund.org/econtalk/EconTalkCDcover1400.jpg',
                       ['Education', 'Higher Education', 'Science & Medicine', 'Social Sciences', 'Business'], '',
                       'clean_econtalk']

podcast_info.loc[20] = ['Real Time with Bill Maher', ['Bill Maher'], 'http://billmaher.hbo.libsynpro.com/rss',
                       'http://static.libsyn.com/p/assets/a/0/6/1/a061ceb8595319af/billmaher_logo1400.jpg',
                       ['News & Politics'], 'time,news,real,politics,bill,jokes,with,maher,overtime',
                       'clean_bill_maher']

podcast_info.loc[21] = ['You Made It Weird with Pete Holmes', ['Pete Holmes'], 'http://feeds.feedburner.com/YouMadeItWeird',
                       'http://static.libsyn.com/p/assets/c/9/6/4/c96469ee482d87aa/YMIW_logo.jpg',
                       ['Comedy', 'Society & Culture', 'Health', 'Self-Help'], 'peteholmes',
                       'clean_pete_holmes']

podcast_info.loc[22] = ['Anna Faris Is Unqualified', ['Anna Faris'], 'http://annafarisisunqualified.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/c/1/6/e/c16e77f29f309dce/Podcast_Cover_Artwork.jpg',
                       ['Comedy', 'Society & Culture', 'Personal Journals', 'TV & Film'], 'annafaris,annafarispodcast,unqualifed',
                       'clean_anna_faris']

podcast_info.loc[23] = ['Armchair Expert with Dax Shepard', ['Dax Shepard'], 'https://rss.simplecast.com/podcasts/4123/rss',
                       'https://media.simplecast.com/podcast/image/4123/1517966385-artwork.jpg',
                       ['Comedy', 'TV & Film', 'Music'], 'armchair expert, dax shepard, armchair expert with dax shepard',
                       'clean_dax_shepard']

podcast_info.loc[24] = ['Fitzdog Radio', ['Greg Fitzsimmons'], 'http://feeds.feedburner.com/FitzdogRadio',
                       'http://static.libsyn.com/p/assets/c/a/2/0/ca20a50bab0ab60a/FitzDog-Podcast-Art300.jpg',
                       ['Comedy'], 'comedy,comics,fitzsimmons,greg,howard,radio,siriusxm,standup,stern',
                       'clean_grapefruit_simmons']

podcast_info.loc[25] = ['Tin Foil Hat With Sam Tripoli', ['Sam Tripoli'], 'http://feeds.soundcloud.com/users/soundcloud:users:26726895/sounds.rss',
                       'http://i1.sndcdn.com/avatars-000318107190-ct1zbx-original.jpg',
                       ['Comedy'], '',
                       'clean_sam_tripoli']

podcast_info.loc[26] = ['Alison Rosen Is Your New Best Friend', ['Alison Rosen'], 'http://ariynbf.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/9/6/e/0/96e0d3a1dc828eca/Alison_Cover_Art_V04_-01bf_violet_sm.jpg',
                       ['Comedy'], '',
                       'clean_alison_rosen']

podcast_info.loc[27] = ['Tangentially Speaking with Christopher Ryan', ['Christopher Ryan'], 'http://tangent.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/b/0/8/e/b08ee47c18c371a7/drchrisryanpodcast1389127900.jpg',
                       ['Arts', 'Society & Culture'], 'christopherryan,sexatdawn,tangentiallyspeaking',
                       'clean_chris_ryan']

podcast_info.loc[28] = ['How Did This Get Made?', ['Paul Scheer', 'June Diane Raphael', 'Jason Mantzoukas'], 'http://rss.earwolf.com/how-did-this-get-made',
                       'https://dfkfj8j276wwv.cloudfront.net/images/1c/74/3b/e9/1c743be9-1820-49ad-b13c-f8554a37698f/ec7e4935400484879bef5009764cce98bf015f3f314369b3962409886a36b6065cc46d7d434c07c1966864e267505f8911d8f00331ace1b9368bc9f770578554.jpeg',
                       ['Comedy'], '',
                       'clean_hdtgm']

podcast_info.loc[29] = ['The Todd Glass Show', ['Todd Glass'], 'http://toddglassshow.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/5/6/1/0/5610162170129e01/toddlogo.jpg',
                       ['Comedy'], 'toddglass',
                       'clean_todd_glass']

podcast_info.loc[30] = ['Dumb People Town', ['Jason Sklar', 'Randy Sklar'], 'http://feeds.feedburner.com/DumbPeopleTown',
                       'https://dfkfj8j276wwv.cloudfront.net/images/d1/f0/9e/47/d1f09e47-98ee-4a81-a842-0a5b02e09873/c09de8c8847d3461cd5665c0556ae2c5e076db7996f9e17c492391b905c6569e0a870b2763313797cd6a7690d6a57e78275313185242280ba0dd0fe36950fac9.jpeg',
                       ['Comedy', 'Society & Culture', 'News & Politics'], 'feral audio,Adam Carolla,Earwolf,Sklarbro Country,sklarbro,Sklarbro County,Dan Van Kirk,Jason Sklar,Dumb People Town,news,Randy Sklar,sklar brothers',
                       'clean_dumb_people_town']

podcast_info.loc[31] = ['Doug Loves Movies', ['Doug Benson'], 'http://feeds.feedburner.com/DougLovesMovies',
                       'https://dfkfj8j276wwv.cloudfront.net/images/82/2f/79/e8/822f79e8-722d-4a6b-8647-8cc9741e87a9/f933e361a2ab293aa85d74f63a4ea343522012cae57c6efa04c518b09d5ad28201c3312b452e93b09b6e349f33b211553dedcf0b7ab4da2702d3680700b416ec.jpeg',
                       ['Comedy', 'TV & Film'], 'DLM',
                       'clean_doug_loves_movies']

podcast_info.loc[32] = ['Getting Doug with High', ['Doug Benson'], 'https://feeds.megaphone.fm/JSH3263641959',
                       'http://static.megaphone.fm/podcasts/40d5b304-bb47-11e7-9b72-cb2def99ce30/image/ItunesCover2.jpeg',
                       ['Comedy'], '',
                       'clean_getting_doug_with_high']

podcast_info.loc[33] = ['Who Charted?', ['Howard Kremer', 'Kulap Vilaysack'], 'http://rss.earwolf.com/who-charted',
                       'https://dfkfj8j276wwv.cloudfront.net/images/4b/cb/49/e0/4bcb49e0-21f1-4c91-a32d-1fcc9aaf7cea/2d71321d1eb0408a42003caf2addf797c7a613b8f59399cd3941e0c5d597d559b3bbc6ebe80da127b9f77e51c5e26dc0501c2e204960efbde7516de7b8379ccf.jpeg',
                       ['Comedy'], '',
                       'clean_who_charted']

podcast_info.loc[34] = ['The Indoor Kids with Kumail Nanjiani and Emily V. Gordon', ['Kumail Nanjiani', 'Emily V. Gordon'], 'http://theindoorkids.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/0/5/c/8/05c8dcb6a18e64c7/IK_logo.jpg',
                       ['Comedy', 'Games & Hobbies', 'Video Games'], 'comedy,emilyvgordon,games,kumail,kumailnanjiani,nanjiani,nerdist,video',
                       'clean_the_indoor_kids']

podcast_info.loc[35] = ['Comedy Film Nerds', ['Graham Elwood', 'Chris Mancini'], 'http://comedyfilmnerds.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/c/f/6/7/cf67b16af95c5dd6/ComedyFilmNerds_ATC.jpg',
                       ['Comedy', 'TV & Film', 'Arts', 'Visual Arts'], 'chris,comedians,comedy,elwood,film,graham,mancini,movie,nerds,reviews',
                       'clean_comedy_film_nerds']

podcast_info.loc[36] = ['The Champs with Neal Brennan + Moshe Kasher', ['Neal Brennan', 'Moshe Kasher'], 'http://thechamps.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/b/e/7/4/be743cc736d9e060/Champs_ATCcover2.jpg',
                        ['Comedy', 'Arts', 'Performing Arts', 'TV & Film'], '',
                        'clean_the_champs']

podcast_info.loc[37] = ['Julian Loves Music', ['Julian McCullough'], 'http://feeds.feedburner.com/JulianLovesMusic',
                        'https://dfkfj8j276wwv.cloudfront.net/images/57/3d/08/52/573d0852-23e1-4b73-91fb-87921f41f549/40acc1a120d790aa6e5aea5547f7ae933592ac9783c0fd29b2cb7f832d4d2886319e4b1d9b6da1b2ad1cfda1044d340abc0462e35b35f3b9f7beac602d3fbb87.jpeg',
                        ['Comedy', 'Music'], 'comedy,Music',
                        'clean_julian_loves_music']

podcast_info.loc[38] = ['Canceled', ['Chris Cubas'], 'https://chriscubas.podbean.com/feed/',
                        'http://deow9bq0xqvbj.cloudfront.net/image-logo/726722/CanceledLogo.jpg',
                        ['Comedy'], '',
                        'clean_chris_cubas']

podcast_info.loc[39] = ['Stand By Your Band', ['Thomas Thakkar', 'Tommy McNamara'], 'http://standbyyourband.podomatic.com/rss2.xml',
                        'https://assets.podomatic.net/ts/53/5a/a7/tomathakkar/pro/1400x1400_12053959.jpg',
                        ['Comedy'], 'tom,thakkar,tommy,mcnamara,comedy,music,guilty,pleasure,bands,coldplay,dave,matthews,band,john,mayer,barenaked,ladies',
                        'clean_thomas_thakkar']

podcast_info.loc[40] = ['Truth & Iliza', ['Iliza Shlesinger'], 'https://rss.art19.com/truth-iliza',
                        'https://dfkfj8j276wwv.cloudfront.net/images/bd/e2/6e/62/bde26e62-29a3-4774-8c29-875c60d33a43/e410a837f6ef34ff1bc0960bdbbffd2da5498cf9922ec45f21d987009f6df0de840a9f1e6a901e6fb56a71b3881288fb78c5ec2b305e29fb29516d462a6d8443.jpeg',
                        ['Comedy', 'Business', 'News & Politics'], 'comedy,Iliza Shlesinger,politics',
                        'clean_iliza']

podcast_info.loc[41] = ['Race Wars', ['Kurt Metzger', 'Sherrod Small'], 'http://feeds.feedburner.com/RaceWarsPodcast', 
                        'http://i1.sndcdn.com/avatars-000116363259-s7xsz1-original.jpg',
                        ['Comedy'], '',
                        'clean_race_wars']

podcast_info.loc[42] = ['The Todd Barry Podcast', ['Todd Barry'], 'http://feeds.feedburner.com/TheToddBarryPodcast',
                        'https://dfkfj8j276wwv.cloudfront.net/images/81/c4/84/5a/81c4845a-4439-4603-9a25-9da4aad24bc4/d40c3bfe15c68ed577cd24af10b69e9a87e90d6c26601b0aa92fe9b53fbbf05416b40b531262c6ad7386cdd58abb50b0810c7a92f478b186ec7e9df579cc2412.jpeg',
                        ['Comedy'], 'comedy',
                        'clean_todd_barry']

podcast_info.loc[43] = ['My Dumb Friends', ['Dan St. Germain', 'Sean Donnelly'], 'http://feeds.soundcloud.com/users/soundcloud:users:66989075/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000225140756-t0z7qh-original.jpg',
                        ['Comedy'], '',
                        'clean_my_dumb_friends']

podcast_info.loc[44] = ['Pleasure Monkey Podcast', ['Conner Moore'], 'http://pleasuremonkey.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/b/1/4/7/b1470697c8f3fe34/PMP_LOGO_1440.png',
                        ['Health', 'Self-Help', 'Fitness & Nutrition', 'Society & Culture', 'Philosophy'], '',
                        'clean_pleasure_monkey']

podcast_info.loc[45] = ['Louder With Crowder', ['Steven Crowder'], 'http://feeds.feedburner.com/LouderWithCrowderPodcasts',
                        'http://louderwithcrowder.com/wp-content/uploads/2014/10/steven-podcast.jpg', 
                        ['News & Politics', 'Comedy'], 'Steven,Crowder,Steven,Crowder,Louder,With,Crowder,Conservative,Comedy,News,Pop,Culture,Politics,Republican,Libertarian,Entertainment,Radio,Fun,Dip,Debate,Guests,Callers,Pranks,Rowdy',
                        'clean_steven_crowder']

podcast_info.loc[46] = ['Doughboys', ['Nick Wiger', 'Mike Mitchell'], 'https://rss.art19.com/doughboys',
                        'https://dfkfj8j276wwv.cloudfront.net/images/16/d5/d9/b2/16d5d9b2-112b-44de-9f9d-dbbef0ea091a/59256c2c15b5aefee93d4aada1d4954fce5199dea9ae73e6a186c94e237b8becb6dec329ec34ce40e50456ba6ecdad67df4ea18e66a95f620934c0af9ecb3c7f.jpeg',
                        ['Comedy', 'Arts'], 'snacks,restaurants,healthfitness,fastfood,chains,mike mitchell,Spoonman,doughboys,nick wiger,fast food,ucb',
                        'clean_doughboys']

podcast_info.loc[47] = ['The Bill Simmons Podcast', ['Bill Simmons'], 'https://rss.art19.com/the-bill-simmons-podcast',
                        'https://dfkfj8j276wwv.cloudfront.net/images/f3/b2/15/7a/f3b2157a-6c3b-4851-83bb-74a9f9e51acb/032d72a5537ea8cbe4116e2f56c929c3c14ef6f0b6659eee2cd974e394793134ed59a2c3261203ba5f9648fe51af6eda43a11e0590e764b45c45a31391777bc6.jpeg',
                        ['Sports & Recreation'], '',
                        'clean_bill_simmons']

podcast_info.loc[48] = ['Legion of Skanks Podcast', ['Big Jay Oakerson', 'Luis J. Gomez', 'Dave Smith'], 'http://legionofskanks.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/e/3/4/9/e349fe6b63c036b6/Untitled_design-7.jpg', 
                        ['Comedy'], 'big,comedy,dave,gomez,j,jay,luis,oakerson,smith',
                        'clean_legion_of_skanks']

podcast_info.loc[49] = ['Punch Drunk Sports', ['Ari Shaffir', 'Sam Tripoli', 'Jayson Thibault'], 'http://feeds.feedburner.com/Punchdrunksports',
                        'http://i1.sndcdn.com/avatars-000060349991-s96mh2-original.jpg',
                        ['Comedy'], 'Ari,Shaffir,Sam,Tripoli,Jayson,Thibault,Sports,Comedy,Hot,Chicks,Weed,and,Ethnic,People,Lesbians,Reach,Arounds,Lob,City,Prison,Sex,Sam,Tripoli,Again',
                        'clean_punch_drunk_sports']

podcast_info.loc[50] = ['Hannibal Buress: Handsome Rambler', ['Hannibal Buress'], 'http://feeds.soundcloud.com/users/soundcloud:users:259698570/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000292437283-dr2wmd-original.jpg',
                        ['Comedy'], '',
                        'clean_hannibal']

podcast_info.loc[51] = ['Pirate Life Radio with Tait Fletcher', ['Tait Fletcher'], 'http://taitfletcher.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/3/7/a/b/37ab08d96355a92b/Tait_Face_Logo.jpg',
                        ['Health', 'Fitness & Nutrition'], '0th,bulletproof,coffee,community,excellence,fletcher,health,healthy,jitsu,jiu,mma,nibiru,planet,staybulletproof,tait,transcendence,tribe,unity',
                        'clean_tait_fletcher']

podcast_info.loc[52] = ['Hear Me This Book', ['Steve Rannazzisi'], 'http://neverreadit.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/d/0/f/7/d0f709d5086ee4b4/Hear_This_Me_Book.jpg',
                        ['Comedy', 'Arts', 'Literature', 'Society & Culture'], 'hearmethisbook',
                        'clean_steve_rannazzisi']

podcast_info.loc[53] = ['The Jim Rome Podcast', ['Jim Rome'], 'https://www.omnycontent.com/d/playlist/4b5f9d6d-9214-48cb-8455-a73200038129/a7c446d6-29da-43ba-bbe5-a7da00ecda4a/a65603a6-cf22-4150-91c1-a7da00ed5220/podcast.rss',
                        'https://www.omnycontent.com/d/playlist/4b5f9d6d-9214-48cb-8455-a73200038129/a7c446d6-29da-43ba-bbe5-a7da00ecda4a/a65603a6-cf22-4150-91c1-a7da00ed5220/image.jpg?t=1506004800&amp;size=Large',
                        ['Sports & Recreation'], '',
                        'clean_jim_rome']

podcast_info.loc[54] = ['View from the Cheap Seats with the Sklar Brothers', ['Jason Sklar', 'Randy Sklar'], 'http://feeds.feedburner.com/ViewFromTheCheapSeatsWithTheSklarBrothers',
                        'https://dfkfj8j276wwv.cloudfront.net/images/f2/67/1d/22/f2671d22-a8fa-4875-9ed7-634b92dae372/68494d2c44f14d2a261a960e7597804e618268961ce5edd573e20d387a9e0eb6ebf721f704d2206092ec6e4df675e16ffe7208a2184f0b4d9763cc58c383f7d3.jpeg',
                        ['Sports & Recreation', 'Professional'], 'an van kirk,dvk,henderson,Earwolf,jim rome,View from the Cheap Seats with the Sklar Brothers,Bill Simmons,View from the Cheap Seats,Seats,DPT,Sklarbro,Cheap,Sklarbro Country,barstool sports,Sklarbro County,Yahoo Sports,Sports,Randy Sklar,NBC Sports,Dumb People Town,sklar brothers,Jason Sklar',
                        'clean_sklar_brothers']

podcast_info.loc[55] = ['All Things Comedy Live', ['Bill Burr', 'Al Madrigal'], 'http://feeds.soundcloud.com/users/soundcloud:users:25905339/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000098077444-pqafza-original.jpg',
                        ['Comedy'], '',
                        'clean_all_things_comedy']

podcast_info.loc[56] = ['Dom Irrera Live from the Laugh Factory', ['Dom Irrera'], 'http://thelaughfactory.libsyn.com/domirrera',
                        'http://static.libsyn.com/p/assets/c/3/4/a/c34a5d67c32736d4/Dom_Irrera_NewpodcastImage.jpg',
                        ['Comedy', 'Technology', 'Podcasting'], '',
                        'clean_dom_irrera']

podcast_info.loc[57] = ['Aubrey Marcus Podcast', ['Aubrey Marcus'], 'https://rss.art19.com/aubrey-marcus-podcast',
                        'https://dfkfj8j276wwv.cloudfront.net/images/de/0d/91/ae/de0d91ae-e2cb-438a-9782-3fd552ae1a11/d88c366c64b948b068e6eee292b10c289387befa3dfff591a8af6e2ec04f338d9cb9f4f7c0980b59403546a9dd342a3ba6571e34c6714cc4c4de899481963a67.jpeg',
                        ['Health', 'Self-Help', 'Society & Culture', 'Philosophy'], 'warriorpoetus,Utopia,spirituality,Religion,psychedelics,poet,philosophy,joerogan,iboga,aubreymarcus,aubrey',
                        'clean_aubrey_marcus']

podcast_info.loc[58] = ['Happy Sad Confused', ['Josh Horowitz'], 'http://feeds.feedburner.com/HappySadConfused', 
                        'http://static.megaphone.fm/podcasts/d7b6c080-6321-11e6-9fb3-37bd74105fce/image/uploads_2F1501696135341-lhgtj69tl98-fc632e520d4c0aa4ca41033c6377dd64_2FHappySadConfused_Cover_1600x1600.jpg',
                        ['TV & Film'], '',
                        'clean_happy_sad_confused']

podcast_info.loc[59] = ['Off Camera with Sam Jones', ['Sam Jones'], 'http://feeds.soundcloud.com/users/soundcloud:users:67972713/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000151317521-0w0bxp-original.jpg',
                        ['Arts'], '',
                        'clean_sam_jones']

podcast_info.loc[60] = ['Maltin on Movies', ['Leonard Maltin', 'Jessie Maltin'], 'http://maltinonmovies.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/1/1/7/4/1174f928af06597c/maltinONmovies_logo-01.jpg',
                        ['TV & Film', 'Comedy'], '',
                        'clean_maltin']

podcast_info.loc[61] = ['How I Built This with Guy Raz', ['Guy Raz'], 'https://www.npr.org/rss/podcast.php?id=510313',
                        'https://media.npr.org/assets/img/2016/08/31/hibt_podcast_tile_sq-8d9498b292dc7a759bf4b7fc776dfe0e4c09da68.png?s=1400',
                        ['Business'], '',
                        'clean_guy_raz']

podcast_info.loc[62] = ['Modern Love', ['Meghna Chakrabarti'], 'http://feeds.feedburner.com/modernlove/podcast',
                        'https://d279m997dpfwgl.cloudfront.net/wp/2016/10/tile-modern-love.jpg',
                        ['Society & Culture'], 'Modern,love',
                        'clean_modern_love']

podcast_info.loc[63] = ['The School of Greatness', ['Lewis Howes'], 'http://feeds.soundcloud.com/users/soundcloud:users:4135366/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000049189658-q7zh56-original.jpg',
                        ['Business'], '',
                        'clean_lewis_howes']

podcast_info.loc[64] = ['The Ringer NBA Show', ['Chris Ryan', 'Justin Verrier', 'Kevin O’Connor', 'Jonathan Tjarks', 'Juliet Litman', 'Chris Vernon', 'John Gonzalez', 'Jonathan Tjarks'], 'https://rss.art19.com/the-ringer-nba-show',
                        'https://dfkfj8j276wwv.cloudfront.net/images/cd/d1/0f/40/cdd10f40-f02c-4cb0-ab87-8ccb70e7838f/c56a49fc95a85538c4f6c90a705ae3e52105e597e6582d2b68ba3dc825ea1a2b3a4c79bc4d4fe2c7720413fb6284979763a21c0b3135a67368a3b19479885158.jpeg',
                        ['Sports & Recreation'], 'Basketball,The Ringer,NBA,Sports',
                        'clean_ringer_nba']

podcast_info.loc[65] = ['The Mike Lupica Show', ['Mike Lupica'], 'http://feeds.feedburner.com/MikeLupicaShow',
                        'http://podcast.compassmedianetworks.com/images/podcast/MikeLupicaPodcast1600px.jpg',
                        ['Sports & Recreation', 'Professional', 'News & Politics', 'Talk Radio'], '',
                        'clean_mike_lupica']

podcast_info.loc[66] = ['Ask Me Another', ['Ophira Eisenberg'], 'https://www.npr.org/rss/podcast.php?id=510299',
                        'https://media.npr.org/assets/img/2015/04/06/askmeanother_sq-ed74d1b32e360a54992e327bf3620365f7d80df7.jpg?s=1400',
                        ['Comedy', 'Games & Hobbies', 'Society & Culture'], '',
                        'clean_ask_me_another']

podcast_info.loc[67] = ['Dear Sugars', ['Cheryl Strayed', 'Steve Almond'], 'https://rss.art19.com/dear-sugars',
                        'https://dfkfj8j276wwv.cloudfront.net/images/c5/7f/52/e5/c57f52e5-a9a3-40b6-897e-f0d39a693a46/315e799bc79e7e2d1d77ae1ee3186711af8a9abf4fbe225e0bc1b7d90d448bfaeca4e84ed82e850ebc6cd6beb822ad7e40a544e00aeee27a53c20d8736cd5b1e.jpeg',
                        ['Society & Culture'], 'Sugar,Boston,Dear,WBUR,Advice',
                        'clean_dear_sugars']

podcast_info.loc[68] = ['The Bugle',  ['Andy Zaltzman'], 'http://feeds.thebuglepodcast.com/thebuglefeed',
                        'https://pbs.twimg.com/profile_images/790620693536866304/6xMusIl3_400x400.jpg',
                        ['Comedy'], '',
                        'clean_bugle']

podcast_info.loc[69] = ['The Daily Zeitgeist', ['Jack O’Brien'], 'https://feeds.megaphone.fm/dailyzeitgeist',
                        'http://static.megaphone.fm/podcasts/052418f4-2d44-11e8-805b-9780d43c8144/image/uploads_2F1521663074285-ayw5ru3yj4p-ce4a614fc6624e78ce25c33eb8273e88_2Fdaily-zeitgeist-hero.png',
                        ['News & Politics'], '',
                        'clean_daily_zeitgeist']

podcast_info.loc[70] = ['SModcast', ['Kevin Smith', 'Scott Mosier'], 'http://feeds.feedburner.com/SModcasts',
                        'https://static1.squarespace.com/static/55c25a62e4b0030db3b1280e/t/58990e4f2e69cfa42a23f585/1486425684970/smodcast-10th.png',
                        ['Comedy', 'TV & Film', 'News & Politics', 'Religion & Spirituality', 'Arts', 'Performing Arts'], '',
                        'clean_smodcast']

podcast_info.loc[71] = ['I AM RAPAPORT: STEREO PODCAST', ['Michael Rapaport'], 'http://iamrapaportpodcast.iamrapaport.libsynpro.com/rss',
                        'http://static.libsyn.com/p/assets/7/f/1/6/7f16ceb1efd7876f/0c8e54cdcfeb684ba796fa9a3dd093ca5a4bfe9a2268e040ce2b627d932d3f9797a47753c57e30ce4530a68f267888b99482b1bf2e6a65ac5d313eb2795016c8.jpeg',
                        ['Sports & Recreation'], '',
                        'clean_rapaport']

podcast_info.loc[72] = ['Never Not Funny: The Jimmy Pardo Podcast', ['Jimmy Pardo'], 'http://rss.earwolf.com/never-not-funny',
                        'https://dfkfj8j276wwv.cloudfront.net/images/c4/6d/c5/5c/c46dc55c-501d-4a51-a158-daaefbf6f563/3f5a8803bbc984256649aeab7f02fc2029fe44da17f0da0e0007c9b96c31c158a6e4fd5fb6efc19c5a568ba0bd36eac467cc98a54b565863757d4d1c0940e878.jpeg',
                        ['Comedy'], '',
                        'clean_jimmy_pardo']

podcast_info.loc[73] = ['The CrabFeast with Ryan Sickler and Jay Larson', ['Ryan Sickler', 'Jay Larson'], 'http://crabfeast.fakemustache.libsynpro.com/rss',
                        'http://static.libsyn.com/p/assets/7/8/a/2/78a2fd04c84d8788/CrabFeast_2017_1400x.jpg',
                        ['Comedy'], 'all,comedy,crab,crabfeast,feast,jay,larson,podcast,ryan,sickler,storytelling,the,things',
                        'clean_crabfeast']

podcast_info.loc[74] = ['improv4humans with Matt Besser', ['Matt Besser'], 'http://rss.earwolf.com/improv4humans',
                        'https://dfkfj8j276wwv.cloudfront.net/images/e9/c5/03/92/e9c50392-6b05-4095-96bb-b953a256ec76/68487ff2ed59c0af8d8339cb3a7e3d5ac0dca8055af8daaf22741e21f63a5cdad8864ff346f14489e93e769025eb3453fd43e1c1bfaa0950e65c172e476f7efb.jpeg',
                        ['Comedy'], '',
                        'clean_matt_besser']

# podcast_info.loc[75] = ["Gilbert Gottfried's Amazing Colossal Podcast", ['Gilbert Gottfried'], 'http://rss.earwolf.com/gilbert-gottfried',
#                         'https://dfkfj8j276wwv.cloudfront.net/images/31/29/12/7b/3129127b-005b-4661-bf9d-5754058ff6db/36fec7b40ec8c53a335499b2ef6fd5adc93a9ae42644459efa8effbfd75d6dc09d78487855096c3d5428b64443a8da1865c0b7927915f154e3354dc0c67a1b36.jpeg',
#                         ['Visual Arts'], '']

podcast_info.loc[75] = ["Gilbert Gottfried's Amazing Colossal Podcast", ['Gilbert Gottfried'], 'http://rss.earwolf.com/gilbert-gottfried',
                        'https://dfkfj8j276wwv.cloudfront.net/images/31/29/12/7b/3129127b-005b-4661-bf9d-5754058ff6db/36fec7b40ec8c53a335499b2ef6fd5adc93a9ae42644459efa8effbfd75d6dc09d78487855096c3d5428b64443a8da1865c0b7927915f154e3354dc0c67a1b36.jpeg',
                        ['TV & Film'], '',
                        'clean_gilbert_gottfried']

podcast_info.loc[76] = ['Jordan, Jesse GO!', ['Jesse Thorn', 'Jordan Morris'], 'http://feeds.feedburner.com/thornmorris',
                        'http://static.libsyn.com/p/assets/0/b/e/3/0be3e67ee172f720/JJGoCoverArt1600px.jpg',
                        ['Comedy', 'Arts', 'Society & Culture'], '',
                        'clean_jordan_jesse_go']

podcast_info.loc[77] = ['Bullseye with Jesse Thorn', ['Jesse Thorn'], 'https://www.npr.org/rss/podcast.php?id=510309',
                        'https://media.npr.org/images/podcasts/primary/icon_510309-5255be024ad86521bf9a9fc391fecfc6c5a2c3ef.jpg?s=1400',
                        ['Society & Culture'], '',
                        'clean_jesse_thorn']

podcast_info.loc[78] = ['Stop Podcasting Yourself', ['Graham Clark', 'Dave Shumka'], 'http://stoppodcastingyourself.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/b/f/8/8/bf887c72706273f9/spybrakes1400.jpg',
                        ['Comedy'], '',
                        'clean_stop_podcasting_yourself']

podcast_info.loc[79] = ['SPONTANEANATION with Paul F. Tompkins', ['Paul F. Tompkins'], 'http://rss.earwolf.com/spontaneanation-with-paul-f-tompkins',
                        'https://dfkfj8j276wwv.cloudfront.net/images/39/3e/aa/19/393eaa19-4f85-4bac-a21d-98a5629cc3a4/6b9f56a78de996193cf2c177295b4a4a5714c9e79dc5aed9e09c3d370102725f18ea13e00e64cf26e3e9dcadfdde9bf867e17594684f8de9800977fcd4b07b17.jpeg',
                        ['Comedy'], '',
                        'clean_spontaneanation']

podcast_info.loc[80] = ['The Pod F. Tompkast', ['Paul F. Tompkins'], 'http://pft.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/6/a/c/4/6ac4df39a9268cda/Pod_F_Tompkast_Final.JPG',
                        ['Comedy', 'Arts', 'Performing Arts', 'TV & Film'], 'alternative,angeles,at,brainwash,cake,comedy,coronet,f,friend,garry,herzog,huffington,ice,largo,lithgow,los,of,paul,reilly,schletter,show,the,tom,tompkins,variety,webber',
                        'clean_tompkast']

podcast_info.loc[81] = ['The Dead Authors Podcast', ['Paul F. Tompkins'], 'http://thedeadauthorspodcast.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/9/6/d/a/96da81c415a1076d/DALogo-v2.jpg',
                        ['Comedy', 'Arts', "Literature", 'Performing Arts'], '826,andy,conan,daly,machine,maya,mcsweeneys,rudolph,snl,superego,time,tompkast,tompkins,travel,ucb',
                        'clean_dead_authors']

podcast_info.loc[82] = ['The Bone Zone', ['Brendon Walsh', 'Randy Liedtke'], 'http://feeds.feedburner.com/TheBoneZone',
                        'https://cdn.shopify.com/s/files/1/2292/0133/products/A_BoneZone_640x640.jpg?v=1507318704',
                        ['Comedy'], 'Bonezone,Doorknockers,Leidtke,Bonehead,Brandon,drdavey,Brendon,Walsh,Randy,Liedtke,and,David,Johnson,Brian,Redban,Deathsquad,bonezone',
                        'clean_bone_zone']

podcast_info.loc[83] = ['Economic Rockstar', ['Frank Conway'], 'http://economicrockstar.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/e/a/5/9/ea597327b7a0ac20/Economic_Rockstar_iTunes.png',
                        ['Education', 'Higher Education', 'Business', 'Investing', 'Society & Culture'], 'behavioraleconomics,bitcoin,careers,college,economics,economists,education,finance,freakonomics,gold,investment,money,psychology,stockmarket,university,wealth',
                        'clean_economic_rockstar']

podcast_info.loc[84] = ["Don't Ever Change with John Roy", ['John Roy'], 'http://feeds.feedburner.com/DontEverChangeWithJohnRoy',
                        'https://dfkfj8j276wwv.cloudfront.net/images/95/9f/d3/c2/959fd3c2-a376-404c-b6e5-19eccdc68813/2547048bfd02adcc9cc8d3e836d7248608615217d8c14bfc6f83e69c89ff23219e40b7f8cc71528fe25e883d000cc64627de86df3d4ee8426d0426a8be07e901.jpeg',
                        ['Comedy'], 'Comedy,feral audio',
                        'clean_john_roy']

podcast_info.loc[85] = ['The K Ohle with Kurt Braunohler', ['Kurt Braunohler'], 'http://feeds.feedburner.com/TheKOhleWithKurtBraunohler',
                        'http://static.libsyn.com/p/assets/8/3/2/8/83285b3c97764c11/k-ohle.jpg',
                        ['Comedy'], 'braunohler,k,kurt,ohle',
                        'clean_kurt_braunohler']

podcast_info.loc[86] = ['Steve Agee: Uhhh', ['Steve Agee'], 'http://feeds.feedburner.com/SteveAgeeUhhhPodcast',
                        'https://dfkfj8j276wwv.cloudfront.net/images/6a/0e/11/b0/6a0e11b0-671f-4afb-823a-56248cfd1c0b/40c2c612c052a55eb55203a9c570e37aeac847289ececc7e0057d5ab2cba29b1a6e3bed0e01377689501c3d6c93dac6315ce779eb101e5bd94b79a9bab79d8af.jpeg',
                        ['Comedy'], 'comedy',
                        'clean_steve_agee']

podcast_info.loc[87] = ['High and Mighty', ['Jon Gabrus'], 'https://rss.art19.com/high-and-mighty',
                        'https://dfkfj8j276wwv.cloudfront.net/images/1d/19/5f/12/1d195f12-2a29-47e7-8df8-99060b1a516e/f0b55d3e5495d430eb3e9d5aca15456bba9f6d2685b7ce7564b324d112c0eebd7e55e20ddf54749970c05202af6ba981b908915ff7b90db8b46fc57d90e97dcb.jpeg',
                        ['Comedy', 'Society & Culture'], 'pop culture,things,Improv,comedy,culture,interests,jon gabrus',
                        'clean_jon_gabrus']

podcast_info.loc[88] = ["Kumail Nanjiani's The X-Files Files", ['Kumail Nanjiani'], 'http://feeds.feedburner.com/KumailNanjianisTheX-filesFiles',
                        'https://assets.pippa.io/shows/59b897881c2b00cd37dedf8a/show-cover.jpeg',
                        ['TV & Film'], 'feral audio, comedy, x-files, Kumail Nanjiani, Silicon Valley, Indoor Kids, sci-fi',
                        'clean_x_files']

podcast_info.loc[89] = ['Getting Curious with Jonathan Van Ness', ['Jonathan Van Ness'], 'http://gettingcurious.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/b/0/6/4/b064141dc36d01f5/GettingCurious2018.jpg',
                        ['Society & Culture', 'Science & Medicine', 'Comedy'], 'curious,discovery,eye,funny,gay,hair,interview,jonathanvanness,netflix,queer,thrones',
                        'clean_jonathan_van_ness']

podcast_info.loc[90] = ['Hollywood Handbook', ['Hayes Davenport', 'Sean Clements'], 'http://rss.earwolf.com/hollywood-handbook',
                        'https://dfkfj8j276wwv.cloudfront.net/images/49/38/9e/00/49389e00-c2a9-4333-aff5-af6e292e68df/05941754bef183c463c0af94dfa0f830242e721c0c88d47993334b5669880c52bcef937ef6e148d333c2505855c06a72e5faa349967a26ce726ef1e3a82e0ab4.jpeg',
                        ['Comedy'], '',
                        'clean_hollywood_handbook']

podcast_info.loc[91] = ["RuPaul: What's The Tee with Michelle Visage", ['RuPaul', 'Michelle Visage'], 'http://rupaul.libsyn.com/rupaul.rss',
                        'http://static.libsyn.com/p/assets/e/c/3/5/ec353555172c3b04/Whats_the_Tee_Ru.jpg',
                        ['Comedy', 'Health', 'Self-Help', 'Society & Culture'], 'beauty,dragrace,fashion,fashionpopculture,michelle,michellevisage,nails,rupaul,rupaulsdragrace,visage',
                        'clean_rupaul']

podcast_info.loc[92] = ['Shane And Friends', ['Shane Dawson'], 'http://feeds.feedburner.com/ShaneAndFriends',
                        'http://i1.sndcdn.com/avatars-000278104111-80h0da-original.jpg',
                        ['Comedy'], 'shane,dawson,shane,dawson,lauren,schnipper,podcast,youtube,s,deezy,shananay,paris,hilton,aunt,hilda,comedy,epic',
                        'clean_shane_dawson']

podcast_info.loc[93] = ['Not Too Deep with Grace Helbig', ['Grace Helbig', 'Jack Ferry'], 'http://feeds.feedburner.com/NotTooDeepWithGraceHelbig',
                        'http://jackferry.com/files/NotTooDeepWithGraceHelbigNew.jpg',
                        ['Comedy'], 'Grace,Helbig,YouTube,Comedy',
                        'clean_grace_helbig']

podcast_info.loc[94] = ['Think Again – a Big Think Podcast', ['Jason Gots'], 'http://feeds.feedburner.com/ThinkAgainABigThinkPodcast',
                        'http://static.megaphone.fm/podcasts/fe024f40-bedd-11e5-9f03-1b69bc6dac84/image/uploads_2F1483454339284-6701ea5my00ax831-8bbf983a3fcd75bacd63795df2eb1098_2FThinkAgainLogoFinal3000x3000.png',
                        ['Arts', 'Society & Culture', 'Science & Medicine'], '',
                        'clean_think_again']

podcast_info.loc[95] = ['Rationally Speaking', ['Julia Galef'], 'http://nycskeptics.org/storage/feeds/rs.xml',
                        'http://skepticmedia.org/images/rs/itunesimage.jpg',
                        ['Science & Medicine', 'Natural Sciences', 'Social Sciences', 'Society & Culture', 'Philosophy'], 'skeptic, science, philosophy, skeptics, skepticism, rational',
                        'clean_rationally_speaking']

podcast_info.loc[96] = ['Skepticality: The Official Podcast of Skeptic Magazine', ['Derek Colanduno', 'Robynn McCarthy'], 'http://skepticality.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/3/6/1/1/3611be4136340596/Skepticality-iTunes-1200-Cover.jpg',
                        ['Science & Medicine', 'Society & Culture', 'News & Politics'], '',
                        'clean_skepticality']

podcast_info.loc[97] = ['Friendly Atheist Podcast', ['Hemant Mehta'], 'http://feeds.soundcloud.com/users/soundcloud:users:126685326/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000118968396-6x0y94-original.jpg',
                        ['Religion & Spirituality'], '',
                        'clean_friendly_atheist']

podcast_info.loc[98] = ["Snoop Dogg's GGN Podcast", ['Snoop Dogg'], 'http://feeds.soundcloud.com/users/soundcloud:users:213836126/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000224515771-mt0v0w-original.jpg',
                        ['Society & Culture'], '',
                        'clean_snoop']

podcast_info.loc[99] = ['Katie Couric', ['Katie Couric'], 'https://rss.art19.com/katie-couric',
                        'https://dfkfj8j276wwv.cloudfront.net/images/b3/01/47/be/b30147be-db0b-4014-81b3-54d2bdccb36a/e7ba4c6cb1ac8917a3d0fb1a89750e954d401e28c15a063dea620e29f05ca38766be387d5720ac3cfda6c514044be1197e65400b1d11f15111514b8c0ff7f250.jpeg',
                        ['News & Politics'], '',
                        'clean_katie_couric']

podcast_info.loc[100] = ['Entrepreneurial Thought Leaders', ['Tina Seelig'], 'http://www.kaltura.com/api_v3/getFeed.php?partnerId=2279881&feedId=0_nqpv5nig&ver=2',
                        'https://stvp-static-prod.s3.amazonaws.com/uploads/sites/2/2018/01/ETL_Podcast_CoverArt.jpg',
                        ['Education', 'Higher Education', 'Business', 'Management & Marketing'], 'Entrepreneurship,Stanford,STVP,568853',
                        'clean_etl']

podcast_info.loc[101] = ['The Ezra Klein Show', ['Ezra Klein'], 'http://feeds.feedburner.com/TheEzraKleinShow',
                        'https://dfkfj8j276wwv.cloudfront.net/images/f3/6e/09/4f/f36e094f-bfab-4452-ab97-de1049734705/3f4ccf0cd20631174d55cb7bf19b06c3db86f730456b137607cbebe688454e1337bf0f65739c052905c6af0fa96c435d1ca870e86dc6cdb1479ed1bfc9c2a755.jpeg',
                        ['News & Politics'], '',
                        'clean_ezra_klein']

podcast_info.loc[102] = ['The Talk Show With John Gruber', ['John Gruber'], 'https://daringfireball.net/thetalkshow/rss',
                        'https://daringfireball.net/thetalkshow/graphics/df-the-talk-show-album-art.png',
                        ['Technology', 'Tech News'], '',
                        'clean_john_gruber']

podcast_info.loc[103] = ['Here We Are', ['Shane Mauss'], 'http://feeds.feedburner.com/herewearepodcast',
                        'https://dfkfj8j276wwv.cloudfront.net/images/5d/50/8e/ea/5d508eea-3ba3-478a-bf24-84a01f47f7af/2fdc54332a57826b74074e268ebca1e2261ab3b41180d5f2aa9c389c069cfc4fa309a807eeb4af1bbd46096d78666d5a73ebe2fc94fd567fe63e8e15b8245ac1.jpeg',
                        ['Comedy', 'Science & Medicine'], 'science,Comedy,here we are,shane mauss',
                        'clean_shane_mauss']

podcast_info.loc[104] = ['Double Date Podcast', ['Shane Mauss', 'April Macie'], 'http://feeds.soundcloud.com/users/soundcloud:users:35132083/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000282348275-itfvgl-original.jpg',
                        ['Comedy'], '',
                        'clean_double_date']

podcast_info.loc[105] = ["It's All Happening", ['Zach Leary'], 'http://itsallhappeningshow.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/0/5/3/7/0537b8a8c7c30f3e/iTunes.jpeg',
                        ['Society & Culture', 'News & Politics', 'Comedy'], 'art,consciousness,culture,music,news,politics',
                        'clean_zach_leary']

podcast_info.loc[106] = ['The Astral Hustle with Cory Allen', ['Cory Allen'], 'http://coryallen.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/6/2/e/9/62e9d1eb1212a170/new_TAH_cover_face_no_eye.jpg',
                        ['Science & Medicine', 'Natural Sciences', 'Society & Culture', 'Philosophy', 'Health', 'Self-Help'], 'consciousness,creativity,meditation,mindfulness,music,spirituality',
                        'clean_cory_allen']

podcast_info.loc[107] = ['Mindrolling with Raghu Markus', ['Raghu Markus'], 'https://rss.art19.com/mindrolling-with-raghu-markus',
                        'https://dfkfj8j276wwv.cloudfront.net/images/8e/91/7f/7b/8e917f7b-2a79-4105-8d0d-a8e46dbb259f/9ff1e7a54ed8150c605a29f26dd7c907f7abbaaf4074105f91b7b695a19b6598aa9651e0ef91ba0b963d3007a969d99fb6c2417b63258112310ba0946340a2ab.jpeg',
                        ['Religion & Spirituality', 'Society & Culture', 'News & Politics'], 'spirituality,Religion,psychedelics,mindrollingpodcast,mindrolling,mindpodnetwork,mindpod,meditation,consciousness',
                        'clean_raghu_markus']

podcast_info.loc[108] = ['Chris Grosso The Indie Spiritualist', ['Chris Grosso'], 'https://rss.art19.com/chris-grosso-the-indie-spiritualist',
                        'https://dfkfj8j276wwv.cloudfront.net/images/33/b3/cb/3b/33b3cb3b-fc89-4fc7-b9df-e17536ee52fa/8d61fb53d11b098552c355a2ae37a38c8a4ef64901e1f0ec386c3ee17ff2848f317925e5a82776823b0dda6201ffdcbc6ecdd420f40c9ddfccdb970ccd5d52df.jpeg',
                        ['Religion & Spirituality', 'Society & Culture'], 'theindiespiritualist,recovery,indiespiritualist,compassion,chrisgrosso,buddhist,author,addiction',
                        'clean_chris_grosso']

podcast_info.loc[109] = ['London Real', ['Brian Rose'], 'http://shoutengine.com/LondonReal.xml',
                        'http://media.cdn.shoutengine.com/cache/d9/6d/d96d8d2d008b56645438144a5a03e5a5.jpg',
                        ['Health', 'Self-Help'], 'fitness,london real,mma,ufc,success,health,drugs,tai lopez,business,london,talk show,bryan callen,dave asprey,joey diaz,self development,money,joe rogan,silicon real,self help,brian rose,talkshow,eric thomas,wealth,tim ferriss',
                        'clean_london_real']

podcast_info.loc[110] = ['Onnit Podcast', ['Aubrey Marcus'], 'https://rss.art19.com/onnit',
                        'https://dfkfj8j276wwv.cloudfront.net/images/ce/e2/6b/53/cee26b53-acbe-4ed5-9070-7e8f91fcac5c/4a1d26b7a387f99d32025def1cc4725e7421fa3a39cca92bf8fc9d6def93b2196831f449fd2c42cae9694bfb84464d978062f2f4b1685690abce54b73ce8f771.jpeg',
                        ['Sports & Recreation', 'Health'], 'hemp,UFC,supplements,organic,onnit,natural,mma,kettlebell,joerogan,Health,GMO,Fitness,crossfit,bjj',
                        'clean_onnit']

podcast_info.loc[111] = ['Brody Stevens Festival Of Sports', ['Brody Stevens'], 'http://festivalofsports.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/5/a/a/2/5aa270810d300fbd/FOS4_1.jpg',
                        ['Comedy', 'Sports & Recreation', 'Health', 'Fitness & Nutrition'], '',
                        'clean_festival_of_sports']

podcast_info.loc[112] = ['The Steven Brody Stevens Festival Of Friendship', ['Brody Stevens'], 'http://feeds.feedburner.com/StevenBrodyFOF',
                        'http://static.libsyn.com/p/assets/5/a/a/2/5aa270810d300fbd/FOS4_1.jpg',
                        ['Comedy'], 'comedy',
                        'clean_brody_stevens']

podcast_info.loc[113] = ["Wait Wait... Don't Tell Me!", ['Peter Sagal'], 'https://www.npr.org/rss/podcast.php?id=344098539',
                        'https://media.npr.org/images/podcasts/primary/icon_344098539-f089cf02094b52708d0979b026a157aa5a1e3ac1.jpg?s=1400',
                        ['Comedy', 'Games & Hobbies', 'Other Games'], '',
                        'clean_wwdtm']

podcast_info.loc[114] = ['Superego', ['Matt Gourley', 'Jeremy Carter', 'Mark McConville', 'Paul F. Tompkins'], 'http://www.gosuperego.com/podcast.xml',
                        'http://www.gosuperego.com/superego-season-4-logo-1400.jpg',
                        ['Comedy', 'Arts', 'Performing Arts', 'Health', 'Self-Help', 'Science & Medicine', 'Social Sciences', 'Alternative Health', 'Medicine'],
                        'superego, matt gourley, jeremy carter, mark mcconville, paul f. tompkins, Patton Oswalt, Neko Case, John Hodgman, Jason Sudeikis, Greg Proops, Erinn Hayes, Andy Daly, Kristen Schaal, jen kirkman, Thomas Lennon, gosuperego.com',
                        'clean_superego']

podcast_info.loc[115] = ['Savage Lovecast', ['Dan Savage'], 'http://savagelove.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/f/9/3/a/f93ab6a788f27e7a/SavageLovecast_1400-compressor.jpg',
                        ['Health', 'Sexuality', 'Comedy', 'News & Politics'], '',
                        'clean_dan_savage']

podcast_info.loc[116] = ['Tom Rhodes Radio Smart Camp', ['Tom Rhodes'], 'http://trr.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/5/b/8/0/5b8002129cb70b89/Lybsyn-1400x1400.jpg',
                        ['Comedy', 'Society & Culture', 'Health'], 'all,central,comedian,comedy,educational,funny,international,knowledge,laughspin,learn,people,personal,podcast,reflection,rhodes,smart,smartcamp,standup,stanhope,things,tom,travel,wisdom,world',
                        'clean_tom_rhodes']

podcast_info.loc[117] = ['The Full Charge Power Hour featuring Matt Fulchiron', ['Matt Fulchiron'], 'http://thefullcharge.com/?feed=podcast',
                        'http://thefullcharge.com/wp-content/uploads/2014/02/securedownload-1.jpg', 
                        ['Comedy', 'Performing Arts', 'News & Politics', 'Society & Culture', 'Philosophy'], '',
                        'clean_full_charge']

podcast_info.loc[118] = ['The 31 with Brandt Tobler', ['Brandt Tobler'], 'http://feeds.soundcloud.com/users/soundcloud:users:80994216/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000162018336-le8m86-original.jpg',
                        ['Comedy'], '',
                        'clean_brandt_tobler']

podcast_info.loc[119] = ['Good Times: With Steve Simeone', ['Steve Simeone'], 'http://goodtimeswithstevesimeone.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/0/c/e/1/0ce13024e96c9cb3/ATC_goodtimes_cover1.jpg',
                        ['Comedy'], 'comedy,friends,help,self,simeone,steve',
                        'clean_steve_simeone']

podcast_info.loc[120] = ['Twisting The Wind with Johnny Pemberton', ['Johnny Pemberton'], 'http://rss.art19.com/twisting-the-wind',
                        'https://assets.pippa.io/shows/59ee7e546a56eba371b694b7/show-cover.jpeg',
                        ['Comedy'], 'feral audio,comedy',
                        'clean_johnny_pemberton']

podcast_info.loc[121] = ['LIVE TO TAPE with Johnny Pemberton', ['Johnny Pemberton'], 'http://rss.art19.com/live-to-tape-with-johnny-pemberton-fb',
                        'https://dfkfj8j276wwv.cloudfront.net/images/da/9c/9f/74/da9c9f74-1cc2-4a0a-8496-dd9f50b2079e/6e502f1b994b067ce60e87e644f6c49b6ec9782ad9f0bfd8dcb712a8a674cc2538547ec5c936660e6f30384e7e2c6cf84541c7c21a8ab9aa7a892f4e4fd76fea.jpeg',
                        ['Comedy', 'Arts'], 'starburns,starburns audio,podcasts,podcast,johnny pemberton',
                        'clean_live_to_tape']

podcast_info.loc[122] = ['Mohr Stories with Jay Mohr', ['Jay Mohr'], 'http://origin.podcastone.com/podcast?categoryID2=331',
                        'http://www.PodcastOne.com/images/logos/mohrstories_1400_4_10.jpg',
                        ['Comedy', 'TV & Film', 'Sports & Recreation'], 'Mohr Stories with Jay Mohr, Jay Mohr',
                        'clean_jay_mohr']

podcast_info.loc[123] = ['The Pony Hour', ['Tony Hinchcliffe'], 'http://feeds.soundcloud.com/users/soundcloud:users:212832286/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000310577091-m7tor3-original.jpg',
                        ['Comedy'], '',
                        'clean_pony_hour']

podcast_info.loc[124] = ['Jocko Podcast', ['Jocko Willink', 'Echo Charles'], 'http://jockopodcast.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/2/b/e/b/2bebbe9aaa40969a/Cover_Art1.jpg',
                        ['Business', 'Management & Marketing'], '',
                        'clean_jocko']

podcast_info.loc[125] = ['The Tim Ferriss Show', ['Tim Ferriss'], 'https://rss.art19.com/tim-ferriss-show',
                        'https://dfkfj8j276wwv.cloudfront.net/images/69/10/10/fb/691010fb-625e-4abe-993c-a57228b28dbe/91cb53ae0d5dbb379b9dffecf0a772593891d0d09bbe6d90ee746edbdb79e3ec75584f2ceb8260e9f675a90c05419b9b99842a76905b686f0f51c1a9d3e227ab.jpeg',
                        ['Business', 'Health', 'Education'], 'workweek,timothyferriss,timothyferris,timferriss,timferris,podcast,fourhour,4hour',
                        'clean_tim_ferriss']

podcast_info.loc[126] = ['StarTalk Radio', ['Neil deGrasse Tyson'], 'http://feeds.soundcloud.com/users/soundcloud:users:38128127/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000100403534-873grd-original.jpg',
                        ['Science & Medicine'], '',
                        'clean_star_talk']

podcast_info.loc[127] = ['The Doug Stanhope Podcast', ['Doug Stanhope'], 'https://audioboom.com/channels/4880830.rss',
                        'https://d15mj6e6qmt1na.cloudfront.net/i/26375217.jpg',
                        ['Comedy', 'Arts', 'Performing Arts'], '',
                        'clean_doug_stanhope']

podcast_info.loc[128] = ['Bitch Sesh: A Real Housewives Breakdown', ['Casey Wilson', 'Danielle Schneider'], 'http://rss.earwolf.com/bitch-sesh',
                        'https://dfkfj8j276wwv.cloudfront.net/images/32/4c/41/76/324c4176-9c17-489f-a891-ba0436be4aaa/3c23471407d3b9dda01d83e30d9eff7e134e418c6bb710844286ded13abf1b74dc5ef99c273e1af851e0ac65e15c7a96692c79381fc6bbaa1ef63c5258b6c5e4.jpeg',
                        ['Comedy'], '',
                        'clean_bitch_sesh']

podcast_info.loc[129] = ['Put Your Hands Together with Cam and Rhea', ['Cameron Esposito', 'Rhea Butcher'], 'https://rss.art19.com/pyht-fb',
                        'https://dfkfj8j276wwv.cloudfront.net/images/22/bb/fc/a0/22bbfca0-6331-4522-bacf-6dd766a70850/539a3286e54ba61fd97ce31d2c6b72c20f605d49dea6c13d3ff6440837232b3c23509a1a1fe978de9bd50c0f1b65384cf35cd3681291c0daa713d7f960d78ce2.jpeg',
                        ['Comedy'], 'Cameron Esposito,Rhea Butcher,records,ast,aspecialthing,ast records,theatre,ucb,comedy,standup,podcast',
                        'clean_cam_rhea']

podcast_info.loc[130] = ['Watch What Happens Live with Andy Cohen', ['Andy Cohen'], 'https://rss.art19.com/watch-what-happens-live-with-andy-cohen',
                        'https://dfkfj8j276wwv.cloudfront.net/images/f2/d0/74/14/f2d07414-8487-44f1-a6ad-793bf398f708/7e4e900f9c390f8833db6d545bfd41ce3cfb90ff2b4674a0233f2ed024eb036eb9a3910ddd70965e59ccf8654b3a48dc87228e8a9b94dc9326a7a46434dedd1f.jpeg',
                        ['TV & Film'], 'wwhl,the real housewives,the real housewives of beverly hills,the real housewives of potomac,shahs of sunset,the real housewives of new york city,below deck,vanderpump rules,the real housewives of dallas,the real housewives of new jersey,the real housewives of orange county,housewives,andy cohen,The Real Housewives Of Orange County,bravo tv,the real housewives of atlanta,reality tv,bravo',
                        'clean_andy_cohen']

podcast_info.loc[131] = ['Rap Radar Podcast', ['Elliott Wilson', 'Brian Miller'], 'https://www.omnycontent.com/d/playlist/4b5f9d6d-9214-48cb-8455-a73200038129/76f26848-76db-42d9-83bf-a78e0075127f/5d1a6abb-fdfe-4c3e-a6cb-a78e00751284/podcast.rss',
                        'https://www.omnycontent.com/d/playlist/4b5f9d6d-9214-48cb-8455-a73200038129/76f26848-76db-42d9-83bf-a78e0075127f/5d1a6abb-fdfe-4c3e-a6cb-a78e00751284/image.jpg?t=1505920529&amp;size=Large',
                        ['Music'], '',
                        'clean_rap_radar']

podcast_info.loc[132] = ['The Vlad Couch', ['DJ Vlad'], 'http://feeds.soundcloud.com/users/soundcloud:users:150303766/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000145573324-otc9rs-original.jpg',
                        ['Society & Culture'], '',
                        'clean_vlad_couch']

podcast_info.loc[133] = ['Allegedly with Theo Von & Matthew Cole Weiss', ['Theo Von', 'Matthew Cole Weiss'], 'http://feeds.soundcloud.com/users/soundcloud:users:157798900/sounds.rss',
                        'http://i1.sndcdn.com/avatars-000200383338-sqqr92-original.jpg',
                        ['Comedy'], '',
                        'clean_allegedly']

podcast_info.loc[134] = ['This Life #YOULIVE With Dr Drew', ['Dr. Drew', 'Bob Forrest'], 'http://thislifewithdrdrewandbobforrest.libsyn.com/rss',
                        'http://static.libsyn.com/p/assets/4/7/4/d/474d2c1b207716d0/this_life_podcast_-_itunes_album_art_-_1500x1500.jpg',
                        ['Health', 'Sexuality', 'Fitness & Nutrition'], '',
                        'clean_this_life']

podcast_info.loc[135] = ['With Friends Like These', ['Ana Marie Cox'], 'http://feeds.feedburner.com/with-friends-like-these',
                        'https://dfkfj8j276wwv.cloudfront.net/images/03/ff/ae/eb/03ffaeeb-1c01-4fe1-9793-b61f4ad2b012/def210f885d1f4a2f2c141749edff2d530e53acb1aa8057d4b1e05ff995c842a790f185a236bb1e86ddf1f5afdbedf0257601701f44f8a1af754495cd22101d9.jpeg',
                        ['News & Politics', 'Society & Culture'], 'empathy,culture,conservatives,liberals,understanding,With Friends Like These,Congress,SCOTUS,Ana Marie Cox,Pod Save America,POTUS,politics',
                        'clean_friends_like_these']

podcast_info.loc[136] = ['The Axe Files with David Axelrod', ['David Axelrod'], 'https://rss.art19.com/axe-files',
                        'https://dfkfj8j276wwv.cloudfront.net/images/0e/5b/88/dc/0e5b88dc-3ca0-4888-bded-d82bff9d7f96/59ca6499223774bbd5fe55cafe24e025b5121e15488933444e407af5aad1897a41c7bc8ed03632cdc2383592aa5de9dd4eb4a80f7178ac60eebd35a2a07a42b9.jpeg',
                        ['News & Politics'], '',
                        'clean_axe_files']

podcast_info.loc[137] = ['Politically Re-Active with W. Kamau Bell & Hari Kondabolu', ['W. Kamau Bell', 'Hari Kondabolu'], 'https://rss.art19.com/politically-re-active',
                        'https://dfkfj8j276wwv.cloudfront.net/images/d1/ea/52/49/d1ea5249-4a4c-4f76-935d-dff474fcda12/d5065446f1cef2e691120a8733bb523b7b039a66c7f952a301a06eafd1e560ba36abccb1ee33076032093678a508edd22b6996425554b7c1dcfa0cba1ce8cd35.jpeg',
                        ['News & Politics'], '',
                        'clean_politically_reactive']

podcast_info.loc[138] = ['The James Altucher Show', ['James Altucher'], 'http://altucher.stansberry.libsynpro.com/rss',
                        'http://static.libsyn.com/p/assets/b/4/6/3/b463232a6b0b641c/James-Altucher-iTunes.jpg',
                        ['Business', 'Investing', 'Health', 'Self-Help'], 'altucher,chooseyourself,entrepreneur,help,investing,podcast,selfpublishing',
                        'clean_james_altucher']

podcast_info.loc[139] = ['Bulletproof Radio', ['Dave Asprey'], 'https://rss.art19.com/bulletproof-radio',
                        'https://dfkfj8j276wwv.cloudfront.net/images/68/ff/3c/56/68ff3c56-288b-462a-b0d7-b11f18a0e6f9/1ca0b29aff230c5c2893f8b40b5f7ab06f9a381c937e0c3a0a15161a25194e69f1079716c77d9d6ad6b7dffbb875fbf29db30d3e981d5b79f38bec0064ee6851.jpeg',
                        ['Health', 'Business', 'Technology'], 'wellness,weight,Sports,paleo,nutrition,muscle,meditation,loss,lifestyle,intermittent,hacking,gain,fitness,fat,fasting,diet,bulletproofexec,brain,biohacking',
                        'clean_bulletproof_radio']

podcast_info.loc[140] = ['Revolution Health Radio', ['Chris Kresser'], 'https://chriskresser.com/feed/podcast',
                        'https://chriskresser.com/wp-content/uploads/powerpress/RHR-new-cover.jpg',
                        ['Health', 'Alternative Health'], '',
                        'clean_chris_kresser']

podcast_info.loc[141] = ['UFC Unfiltered with Jim Norton and Matt Serra', ['Jim Norton', 'Matt Serra'], 'http://feeds.feedburner.com/UFC-Unfiltered',
                        'https://dfkfj8j276wwv.cloudfront.net/images/7a/d1/70/30/7ad17030-56a6-4781-b3b1-47129b1618a4/5a2961a00914cddb306a74575438df5a08eb303634dbddae89c9bdb6c710076f7cd4d6c380cc4c41dff3ea6e467f5686d772fcc9957cc276623bfa10e8830291.jpeg',
                        ['Sports & Recreation', 'Professional'], '',
                        'clean_ufc_unfiltered']

podcast_info.loc[142] = ['10% Happier with Dan Harris', ['Dan Harris'], 'http://feeds.feedburner.com/abcradio/10percenthappier',
                        'http://www.abcradio.com/ppt/10-happier-podcast.jpg',
                        ['Health'], '',
                        'clean_dan_harris']

podcast_info.loc[143] = ["Oprah’s SuperSoul Conversations", ['Oprah Winfrey'], 'https://feeds.megaphone.fm/MRM9077223370',
                        'http://static.megaphone.fm/podcasts/d14b05a0-b2a6-11e7-9296-bbfc944381a8/image/OWN_SuperSoul_Podcast_Logo_FINAL.jpg',
                        ['Society & Culture', 'Health', 'Religion & Spirituality'], '',
                        'clean_supersoul']





podcast_info.to_csv('meta_podcast_info.csv', sep='\t')


