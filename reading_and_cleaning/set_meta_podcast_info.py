from pandas import DataFrame


podcast_info = DataFrame(columns=['Podcast Name', 'Hosts', 'feedURL', 'imageURL', 'categories','keywords'])

podcast_info.loc[1] = ['The Joe Rogan Experience', ['Joe Rogan'], 'http://joeroganexp.joerogan.libsynpro.com/rss', 
                       'http://static.libsyn.com/p/assets/7/1/f/3/71f3014e14ef2722/JREiTunesImage2.jpg',
                       ['Comdedy', 'Society and Culture', 'Technology'], 'comedian,joe,monkey,redban,rogan,talking,ufc']

podcast_info.loc[2] = ['Duncan Trussell Family Hour', ['Duncan Trussell'], 'http://feeds.feedburner.com/DuncanTrussell',
                       'https://dfkfj8j276wwv.cloudfront.net/images/a5/61/da/36/a561da36-4f52-4e99-8dd8-39327127d1a4/5da29f0114e2bd9452a227692e5b6a128325544f2bf8d3eccac16f0989ae4202d9cacd3c462a1e2cff821dc6d38e279aa756834b237b3c83714c0b0a8e9130f9.jpeg',
                       ['Comedy', 'Arts', 'Religion and Spirituality'], '']

podcast_info.loc[3] = ["Bertcast's podcast", ['Bert Kreischer'], 'http://bertcast.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/0/c/7/c/0c7ceaa632f83139/1400x1400Bertcast.jpg',
                      ['Comedy'], 'bert,kreischer,machine,the']

podcast_info.loc[4] = ['The Fighter & The Kid', ['Brendan Schaub', 'Bryan Callen'], 'https://rss.art19.com/fighter-and-the-kid',
                       'https://dfkfj8j276wwv.cloudfront.net/images/b8/c5/2e/ce/b8c52ece-79d2-46f9-81bf-6cce4dc77800/bfd625393db10277d5c303ca78375af9e7c5bb59da46752add461ef74adfdf555b1c523849be889ec5ad88756e46b38944d985093671fd95fcbc03ed697d4129.jpeg',
                      ['Sports & Recreation', 'Society & Culture', 'Comedy'], 'bellator,ufcfightnight,mixed martial arts,ufc fight night,fight night,ufc event,funny,Comedy,Brendan Schaub,Bryan Callen,Ultimate Fighting Championship,ufc,MMA']

podcast_info.loc[5] = ["Ari Shaffir's Skeptic Tank", ['Ari Shaffir'], 'http://shaffir1.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/b/4/2/5/b4254b9d8fe44416/SkepticTank_cover4.jpg',
                      ['Comedy', 'Education'], 'allthingscomedy,ari,arithegreat,burr,comedy,death,deathsquad,diaz,duncan,freak,joe,joey,kreischer,party,punchdrunk,rogan,sceptic,segura,septic,shaffir,shafir,skeptic,squad,store,tank,thisisnothappening,trussell']

podcast_info.loc[6] = ['Under The Skin with Russell Brand', ['Russell Brand'], 'https://rss.art19.com/under-the-skin',
                       'https://dfkfj8j276wwv.cloudfront.net/images/96/ea/83/97/96ea8397-cf58-431e-8dd9-52076598956f/116d59ed2835d58004391beaa0d2642c26f3739452e996f20b13384f54eee5db752a71c1a70e0922941daf8b746395f6bf4758a6d593654fd595aaa04c4234af.jpeg',
                      ['Comedy', 'Society & Culture', 'Philosophy'], '']

podcast_info.loc[7] = ['Pointless: with Kevin Pereira', ['Kevin Pereira'], 'http://pointlesspod.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/b/c/b/c/bcbccaff844fdfb6/Pointless_Logo.png',
                      ['Comedy'], 'attack,attackoftheshow,g4,hackmylife,kevinpereira,pointless']

podcast_info.loc[8] = ['ID10T with Chris Hardwick', ['Chris Hardwick'], 'https://rss.art19.com/id10t',
                      'https://dfkfj8j276wwv.cloudfront.net/images/58/a1/cf/f4/58a1cff4-2127-476f-a386-eb043b863a7a/577d912b5d1f36c085da75e9b1590c392669d508757552874e76c4d4d1fe8d0143ed8b003d90b5a6e8eb5ef72763a9f889c5ca7818e8d5dc4740ffab7e19d414.jpeg',
                      ['Comedy'], 'ID10T,hardwick']

podcast_info.loc[9] = ['Waking Up with Sam Harris', ['Sam Harris'], 'http://wakingup.libsyn.com/rss',
                      'http://static.libsyn.com/p/assets/0/b/e/4/0be4dc9e0fc61265/podcast_art_alt_1.5.18.jpg',
                      ['Science & Medicine', 'Society & Culture', 'Religion & Spirituality'], 'currentevents,ethics,neuroscience,philosophy,politics,religion,samharris,science']

podcast_info.loc[10] = ['Kill Tony', ['Tony Hinchcliffe', 'Brian Redban'], 'http://www.deathsquad.tv/feed/',
                       'http://is1.mzstatic.com/image/thumb/Music62/v4/a2/28/46/a22846be-aa37-a34f-b0b1-82f2eda98fff/source/1200x630bb.jpg',
                       ['Comedy', 'Technology', 'TV & Film'], '']

podcast_info.loc[11] = ['The Rubin Report', ['Dave Rubin'], 'https://rss.art19.com/the-rubin-report',
                       'https://dfkfj8j276wwv.cloudfront.net/images/26/c5/8b/5a/26c58b5a-3265-47af-baa3-8fcb03552e8b/1667b2b70b03d6be83ea88721bba31e5a3b1163b34be18d15dc871ab51ec406353f7fa688c37e521bd87211ad78acc268c0cc7b860c196b611674f2dd0b3786e.jpeg',
                       ['News & Politics', 'Comedy', 'Society & Culture'], 'world news,real time,political news,bill maher,the daily show,the rubin report,political comedy,Rubin Report ,Interview Politics,Dave Rubin,news channel,Talk Show,political correctness,joe rogan,celebrity,breaking news,free speech,current events,technology,entertainment,news']

podcast_info.loc[12] = ['Comedy Bang Bang', ['Scott Aukerman'], 'http://rss.earwolf.com/comedy-bang-bang',
                       'https://dfkfj8j276wwv.cloudfront.net/images/9f/09/33/49/9f093349-89d6-436b-ad97-1e6de2bc95e4/f5549c7f8f4b94c14765e5d186cbd701a8e30673abe6afc4cd8d3e3280a60b403371cc6c53dd99c5a96c091f5d8f052a7034d3f1c3532078a7b494b62094ce0f.jpeg',
                       ['Comedy'], '']

podcast_info.loc[13] = ['H3 Podcast', ['Ethan Klein'], 'http://h3h3roost.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/4/4/3/c/443cb5e4b2df7938/NEW_Podcast_Logo_SQUARE.png',
                       ['Comedy'], 'comedy,entertainment,ethan,ethanklein,h3,h3h3,h3h3productions,h3podcast,hila,hilaklein,interview,klein']

podcast_info.loc[14] = ['WTF with Marc Maron Podcast', ['Marc Maron'], 'http://wtfpod.libsyn.com/rss', 
                       'http://static.libsyn.com/p/assets/6/c/a/3/6ca38c2fefa1e989/WTF_-_new_larger_cover.jpg',
                       ['Comedy', 'Arts', 'Performing Arts', 'TV & Film'], '']

podcast_info.loc[15] = ["The Church of What's Happening Now: With Joey Coco Diaz", ['Joey Diaz'], 'http://thechurchofwhatshappeningnow.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/0/9/2/b/092b6071107e1f7d/itunes.jpg',
                       ['Comedy'], 'comedy,diaz,joey,music']

podcast_info.loc[16] = ["Your Mom's House with Christina P. and Tom Segura", ['Tom Segura', 'Christina Pazsitzky'], 'http://feeds.feedburner.com/YourMomsHouseWithChristinaPazsitzkyAndTomSegura',
                       'http://static.libsyn.com/p/assets/f/a/9/9/fa99383b96617676/YMH_ATCcover_1.jpg',
                       ['Comedy'], 'tom,segura,christina,pazsitzky,dry,sarcastic,philosophy,wipe,dumps,coffee,teeth,dental,dudes,balls,gay,fart']

podcast_info.loc[17] = ['Harmontown', ['Dan Harmon'], 'http://feeds.feedburner.com/HarmontownPodcast',
                       'https://dfkfj8j276wwv.cloudfront.net/images/89/a3/a0/38/89a3a038-05d1-494d-b1e1-0c4767fccdd8/675f78e08433fc7acfa1d068f9455065988e39d6676f6570e99b295f832fe96c8a6df5bb8d06873a33266c5f66b47cce870543d99e9bf3e7d88d780d6475a373.jpeg',
                       ['Comedy'], '']

podcast_info.loc[18] = ['Freedomain Radio with Stefan Molyneux', ['Stefan Molyneux'], 'http://feeds.feedburner.com/FreedomainRadioVolume6',
                       'http://www.freedomainradio.com/images/xmlfeed/iTunes_Podcast_Avatar_Latest.png',
                       ['News & Politics', 'Education/Higher Education', 'Religion & Spirituality', 'Society & Culture/Philosophy', 'Society & Culture/History', 'News & Politics', 'Education', 'Higher Education', 'Religion & Spirituality', 'Society & Culture', 'Philosophy', 'Society & Culture', 'History'], 'state,god,family,atheism,atheist,anarchy,anarchism,government,freedomain,libertarian,podcast,podcasts,radio,stefan,stephen,stephan,molyneux,violence,philosophy,history,economics,classical,liberalism,capitalism,freedom,free,market,joe,rogan,ron,paul']

podcast_info.loc[19] = ['Econtalk', ['Russ Roberts'], 'http://files.libertyfund.org/econtalk/EconTalk.xml',
                       'http://files.libertyfund.org/econtalk/EconTalkCDcover1400.jpg',
                       ['Education', 'Higher Education', 'Science & Medicine', 'Social Sciences', 'Business'], '']

podcast_info.loc[20] = ['Real Time with Bill Maher', ['Bill Maher'], 'http://billmaher.hbo.libsynpro.com/rss',
                       'http://static.libsyn.com/p/assets/a/0/6/1/a061ceb8595319af/billmaher_logo1400.jpg',
                       ['News & Politics'], 'time,news,real,politics,bill,jokes,with,maher,overtime']

podcast_info.loc[21] = ['You Made It Weird with Pete Holmes', ['Pete Holmes'], 'http://feeds.feedburner.com/YouMadeItWeird',
                       'http://static.libsyn.com/p/assets/c/9/6/4/c96469ee482d87aa/YMIW_logo.jpg',
                       ['Comedy', 'Society & Culture', 'Health', 'Self-Help'], 'peteholmes']

podcast_info.loc[22] = ['Anna Faris Is Unqualified', ['Anna Faris'], 'http://annafarisisunqualified.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/c/1/6/e/c16e77f29f309dce/Podcast_Cover_Artwork.jpg',
                       ['Comedy', 'Society & Culture', 'Personal Journals', 'TV & Film'], 'annafaris,annafarispodcast,unqualifed']

podcast_info.loc[23] = ['Armchair Expert with Dax Shepard', ['Dax Shepard'], 'https://rss.simplecast.com/podcasts/4123/rss',
                       'https://media.simplecast.com/podcast/image/4123/1517966385-artwork.jpg',
                       ['Comedy', 'TV & Film', 'Music'], 'armchair expert, dax shepard, armchair expert with dax shepard']

podcast_info.loc[24] = ['Fitzdog Radio', ['Greg Fitzsimmons'], 'http://feeds.feedburner.com/FitzdogRadio',
                       'http://static.libsyn.com/p/assets/c/a/2/0/ca20a50bab0ab60a/FitzDog-Podcast-Art300.jpg',
                       ['Comedy'], 'comedy,comics,fitzsimmons,greg,howard,radio,siriusxm,standup,stern']

podcast_info.loc[25] = ['Tin Foil Hat With Sam Tripoli', ['Sam Tripoli'], 'http://feeds.soundcloud.com/users/soundcloud:users:26726895/sounds.rss',
                       'http://i1.sndcdn.com/avatars-000318107190-ct1zbx-original.jpg',
                       ['Comedy'], '']

podcast_info.loc[26] = ['Alison Rosen Is Your New Best Friend', ['Alison Rosen'], 'http://ariynbf.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/9/6/e/0/96e0d3a1dc828eca/Alison_Cover_Art_V04_-01bf_violet_sm.jpg',
                       ['Comedy'], '']

podcast_info.loc[27] = ['Tangentially Speaking with Christopher Ryan', ['Christopher Ryan'], 'http://tangent.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/b/0/8/e/b08ee47c18c371a7/drchrisryanpodcast1389127900.jpg',
                       ['Arts', 'Society & Culture'], 'christopherryan,sexatdawn,tangentiallyspeaking']

podcast_info.loc[28] = ['How Did This Get Made?', ['Paul Scheer, June Diane Raphael, Jason Mantzoukas'], 'http://rss.earwolf.com/how-did-this-get-made',
                       'https://dfkfj8j276wwv.cloudfront.net/images/1c/74/3b/e9/1c743be9-1820-49ad-b13c-f8554a37698f/ec7e4935400484879bef5009764cce98bf015f3f314369b3962409886a36b6065cc46d7d434c07c1966864e267505f8911d8f00331ace1b9368bc9f770578554.jpeg',
                       ['Comedy'], '']

podcast_info.loc[29] = ['The Todd Glass Show', ['Todd Glass'], 'http://toddglassshow.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/5/6/1/0/5610162170129e01/toddlogo.jpg',
                       ['Comedy'], 'toddglass']

podcast_info.loc[30] = ['Dumb People Town', ['Jason Sklar', 'Randy Sklar'], 'http://feeds.feedburner.com/DumbPeopleTown',
                       'https://dfkfj8j276wwv.cloudfront.net/images/d1/f0/9e/47/d1f09e47-98ee-4a81-a842-0a5b02e09873/c09de8c8847d3461cd5665c0556ae2c5e076db7996f9e17c492391b905c6569e0a870b2763313797cd6a7690d6a57e78275313185242280ba0dd0fe36950fac9.jpeg',
                       ['Comedy', 'Society & Culture', 'News & Politics'], 'feral audio,Adam Carolla,Earwolf,Sklarbro Country,sklarbro,Sklarbro County,Dan Van Kirk,Jason Sklar,Dumb People Town,news,Randy Sklar,sklar brothers']

podcast_info.loc[31] = ['Doug Loves Movies', ['Doug Benson'], 'http://feeds.feedburner.com/DougLovesMovies',
                       'https://dfkfj8j276wwv.cloudfront.net/images/82/2f/79/e8/822f79e8-722d-4a6b-8647-8cc9741e87a9/f933e361a2ab293aa85d74f63a4ea343522012cae57c6efa04c518b09d5ad28201c3312b452e93b09b6e349f33b211553dedcf0b7ab4da2702d3680700b416ec.jpeg',
                       ['Comedy', 'TV & Film'], 'DLM']

podcast_info.loc[32] = ['Getting Doug with High', ['Doug Benson'], 'https://feeds.megaphone.fm/JSH3263641959',
                       'http://static.megaphone.fm/podcasts/40d5b304-bb47-11e7-9b72-cb2def99ce30/image/ItunesCover2.jpeg',
                       ['Comedy'], '']

podcast_info.loc[33] = ['Who Charted?', ['Howard Kremer', 'Kulap Vilaysack'], 'http://rss.earwolf.com/who-charted',
                       'https://dfkfj8j276wwv.cloudfront.net/images/4b/cb/49/e0/4bcb49e0-21f1-4c91-a32d-1fcc9aaf7cea/2d71321d1eb0408a42003caf2addf797c7a613b8f59399cd3941e0c5d597d559b3bbc6ebe80da127b9f77e51c5e26dc0501c2e204960efbde7516de7b8379ccf.jpeg',
                       ['Comedy'], '']

podcast_info.loc[34] = ['The Indoor Kids with Kumail Nanjiani and Emily V. Gordon', ['Kumail Nanjiani', 'Emily V. Gordon'], 'http://theindoorkids.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/0/5/c/8/05c8dcb6a18e64c7/IK_logo.jpg',
                       ['Comedy', 'Games & Hobbies', 'Video Games'], 'comedy,emilyvgordon,games,kumail,kumailnanjiani,nanjiani,nerdist,video']

podcast_info.loc[35] = ['Comedy Film Nerds', ['Graham Elwood', 'Chris Mancini'], 'http://comedyfilmnerds.libsyn.com/rss',
                       'http://static.libsyn.com/p/assets/c/f/6/7/cf67b16af95c5dd6/ComedyFilmNerds_ATC.jpg',
                       ['Comedy', 'TV & Film', 'Arts', 'Visual Arts'], 'chris,comedians,comedy,elwood,film,graham,mancini,movie,nerds,reviews']



podcast_info.to_csv('meta_podcast_info.csv', sep='\t')


