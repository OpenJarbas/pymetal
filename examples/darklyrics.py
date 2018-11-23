from pymetal.lyrics import DarkLyrics


d = DarkLyrics()
max_pages = 2

general_search = d.search("arch enemy", max_pages)
# {'albums': {},
#  'artists': {'arch enemy': {'artist': 'arch enemy',
#                             'name': 'ARCH ENEMY',
#                             'url': 'http://www.darklyrics.com/a/archenemy.html'}},
#  'songs': {' Arch (Enemy) Misanthrope': {'artist': 'dååth ',
#                                          'name': ' Arch (Enemy) Misanthrope',
#                                          'url': 'http://www.darklyrics.com/lyrics/dth/dth.html#9'},
#            ' Arch Enemy Spain': {'artist': 'god dethroned ',
#                                  'name': ' Arch Enemy Spain',
#                                  'url': 'http://www.darklyrics.com/lyrics/goddethroned/thelairofthewhiteworm.html#2'}}}
#

url = 'http://www.darklyrics.com/lyrics/gloryhammer/space1992riseofthechaoswizards.html'
lyrics = d.parse_album_url(url)
# {'Apocalypse 1992': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                      'album_date': '2015',
#                      'album_type': 'album',
#                      'artist': 'gloryhammer',
#                      'lyrics': '[Spoken:]\n'
#                                'And lo, led by the valiant hero Angus McFife '
#                                'XIII\n'
#                                'The forces of justice assembled their armies '
#                                'in the skies above Mars\n'
#                                'In preparation for the epic battle against the '
#                                'demon horde\n'
#                                'But on planet Earth, a far more sinister '
#                                'machination was afoot\n'
#                                'In the dwarven caverns beneath the mighty '
#                                'citadel of Dundee\n'
#                                'The evil wizard Zargothrax began to recite the '
#                                'dread incantation\n'
#                                'Which would unlock the Chaos Portal to the '
#                                'galactic nexus\n'
#                                'As foretold in the dark prophecy of Anstruther '
#                                'countless centuries ago\n'
#                                "As he placed the goblin king's crystal key "
#                                'into the altar before him\n'
#                                'Ancient runes began to glow on the surface of '
#                                'the portal\n'
#                                'Soon the gateway would open and the elder god '
#                                'Korviliath\n'
#                                'Of the eighteenth hell dimension would be '
#                                'unleashed onto the galaxy\n'
#                                'The countdown to universal annihilation had '
#                                'begun\n'
#                                '\n'
#                                'Warriors of planet Earth, hear my raging cry\n'
#                                'For mighty Dundee, the demons will die\n'
#                                '\n'
#                                '[Spoken:]\n'
#                                'Yes, battle cruisers\n'
#                                "To space we'll go\n"
#                                'Discover new worlds\n'
#                                'And conquer galaxies\n'
#                                '\n'
#                                'Across the skies of Mars, the demon wars '
#                                'begin\n'
#                                "Trust in your sword, this battle we'll win\n"
#                                'The space knights of Crail are first to the '
#                                'fight\n'
#                                'Clashing with lasers and power of might\n'
#                                '\n'
#                                'Fly high through apocalypse skies\n'
#                                'Fight for the world we must save\n'
#                                'Like tears of a unicorn lost in the rain\n'
#                                'Chaos will triumph this day\n'
#                                'Apocalypse 1992\n'
#                                '\n'
#                                'At the speed of light the dwarven king '
#                                'arrives\n'
#                                'With crystal laser battleaxe into the fight he '
#                                'rides\n'
#                                '\n'
#                                '[Spoken:]\n'
#                                'Pathetic dwarves\n'
#                                'You are no match for my demon hordes\n'
#                                'Let battle commence\n'
#                                '\n'
#                                "It's the rage, the cosmic rage\n"
#                                'The cosmic rage of astral dwarves from '
#                                'Aberdeen\n'
#                                'From their mines they will arise and fight\n'
#                                'The rage of the dwarves is tonight\n'
#                                '\n'
#                                "It's the rage, the cosmic rage\n"
#                                'The cosmic rage of astral dwarves from '
#                                'Aberdeen\n'
#                                'From their mines they will arise and fight\n'
#                                'The rage of the dwarves is tonight\n'
#                                '\n'
#                                'My ancestral demon army\n'
#                                'Will ride a cosmic sphere\n'
#                                'And liberate the multiverse\n'
#                                'From slavery and fear\n'
#                                'With the power of the crystal\n'
#                                'From an ancient galaxy\n'
#                                'The force of evil will prevail\n'
#                                'It is my destiny\n'
#                                '\n'
#                                'Fly high through apocalypse skies\n'
#                                'Fight for the world we must save\n'
#                                'Like tears of a unicorn lost in the rain\n'
#                                'Chaos will triumph this day\n'
#                                '\n'
#                                'Fly high through apocalypse skies\n'
#                                'Fight for the world we must save\n'
#                                'Like tears of a unicorn lost in the rain\n'
#                                'Chaos will triumph this day\n'
#                                'Apocalypse 1992\n'
#                                '\n'
#                                'From the caves beneath Dundee\n'
#                                'Ancient hermit arrives\n'
#                                'A messenger to the war in the stars\n'
#                                'Korviliath is nigh\n'
#                                '\n'
#                                'Deep inside the Hootsman there lies a secret '
#                                'heart\n'
#                                'Barbarian is a cyborg powered by a neutron '
#                                'star\n'
#                                'For centuries immortal he will quest in time '
#                                'and space\n'
#                                'But now he must make sacrifice to save the '
#                                'human race\n'
#                                '\n'
#                                'The only way to save the galaxy\n'
#                                'Is to destroy planet Earth and Aberdeen\n'
#                                '\n'
#                                'Faster than a laser bullet\n'
#                                'Hootsman flies to Fife\n'
#                                'He detonates his neutron\n'
#                                'Destroys all human life\n'
#                                '\n'
#                                'Fly high through apocalypse skies\n'
#                                'Fight for the world we must save\n'
#                                'Like tears of a unicorn lost in the rain\n'
#                                'Chaos will triumph this day\n'
#                                '\n'
#                                'Fly high through apocalypse skies\n'
#                                'Fight for the world we must save\n'
#                                'Like tears of a unicorn lost in the rain\n'
#                                'Chaos will triumph this day\n'
#                                'Apocalypse\n'
#                                '\n'
#                                '[Spoken:]\n'
#                                'With a thunderous implosion the Earth was '
#                                'vaporised\n'
#                                'Tearing a dimensional rift in the heavens\n'
#                                'Using his last chance of power\n'
#                                'Zargothrax plunged through the space portal\n'
#                                'Vanishing into another reality\n'
#                                'And so Angus McFife XIII followed him into the '
#                                'wormhole\n'
#                                'For the eternal glory of Dundee\n'
#                                '\n'
#                                'Sanctus!\n'
#                                'Dominus!',
#                      'song_number': '10'},
#  'Dundax Aeterna': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                     'album_date': '2015',
#                     'album_type': 'album',
#                     'artist': 'gloryhammer',
#                     'lyrics': '[Instrumental]\n'
#                               'Ben Turk â\x80\x94 Drums\n'
#                               'Christopher Bowes â\x80\x94 Keyboards\n'
#                               'James Cartwright â\x80\x94 Bass\n'
#                               'Paul Templing â\x80\x94 Guitars\n'
#                               'Thomas Winkler â\x80\x94 Vocals\n'
#                               'Submits, comments, corrections are welcomed at '
#                               'webmaster@darklyrics.com\n'
#                               'GLORYHAMMER LYRICS',
#                     'song_number': '11'},
#  'Goblin King Of The Darkstorm Galaxy': {'album': 'Space 1992: Rise Of The '
#                                                   'Chaos Wizards',
#                                          'album_date': '2015',
#                                          'album_type': 'album',
#                                          'artist': 'gloryhammer',
#                                          'lyrics': 'I have returned from '
#                                                    'centuries of slumber, now '
#                                                    'the universe must burn\n'
#                                                    'I feel the power, yet '
#                                                    'still I thirst for more, '
#                                                    'ancient secrets I must '
#                                                    'learn\n'
#                                                    'I ride the twilight, in '
#                                                    'search of cosmic fire\n'
#                                                    'The Goblin King knows my '
#                                                    'desire\n'
#                                                    '\n'
#                                                    'Regis! Kobalos! Cast '
#                                                    'unholy fire!\n'
#                                                    '\n'
#                                                    'Goblin King of the '
#                                                    'Darkstorm Galaxy\n'
#                                                    'Ride on the wings of doom\n'
#                                                    'Grant me the power to '
#                                                    'fight my foes\n'
#                                                    'And defeat the lords of '
#                                                    'the moon\n'
#                                                    '\n'
#                                                    'This magic crystal is the '
#                                                    'artifact you seek to '
#                                                    'unleash evil from the sky\n'
#                                                    'You must find the portal, '
#                                                    'the crystal is the '
#                                                    'key...all universal life '
#                                                    'will die!\n'
#                                                    'Deep beneath Dundee, the '
#                                                    'mighty citadel\n'
#                                                    'There lies a passageway to '
#                                                    'Hell',
#                                          'song_number': '4'},
#  'Heroes (Of Dundee)': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                         'album_date': '2015',
#                         'album_type': 'album',
#                         'artist': 'gloryhammer',
#                         'lyrics': 'As word spread of the demon army invasion '
#                                   'that was threatening Mars, mighty warriors '
#                                   'of the entire galaxy began to assemble in '
#                                   'preparation to fight for the power of the '
#                                   'cosmic justice. Crystalline darkness was '
#                                   'falling upon the hearts of the assembled '
#                                   'host. After a thousand years of peace, the '
#                                   'Intergalactic Space Empire of Fife was '
#                                   'about to once again plunge into a bloody '
#                                   'war, standing behind the banner of Angus '
#                                   'McFife XIII. Riding his ancestral '
#                                   'laserdragon, the brave prince of Dundee '
#                                   'stood before his proud legions and raised '
#                                   'the Hammer of Glory to the heavens.\n'
#                                   '\n'
#                                   'Fly! On gigantic dragons made out of '
#                                   'steel.\n'
#                                   'Strike! With the Hammer of Glory, we will '
#                                   'prevail\n'
#                                   'Kill! Our cosmical enemies with full force, '
#                                   'blasting forth without remorse\n'
#                                   '\n'
#                                   'Rage! With bold supersonic velocity\n'
#                                   "Trust! In our lasers to storm 'cross the "
#                                   'galaxy\n'
#                                   'Die! For the universe that we are fighting '
#                                   'for, to win the war, forevermore\n'
#                                   '\n'
#                                   'For Dunkeld and Cowdenbeath, an epic war is '
#                                   'fight\n'
#                                   '\n'
#                                   'We are heroes, heroes of Dundee,\n'
#                                   'We are riding forth to free our galaxy\n'
#                                   'We are heroes, heroes of Dundee,\n'
#                                   'We are heroes, legends we will be!\n'
#                                   '\n'
#                                   'Fear! Our troll mass destruction '
#                                   'artillery.\n'
#                                   'Hear! Our battlecry echoing through the '
#                                   'sphere\n'
#                                   "Ride! On the back of the dragons, we're "
#                                   'standing proud, wrath unbound, we hold our '
#                                   'ground\n'
#                                   '\n'
#                                   'For Crail and for Aberdeen, an epic war is '
#                                   'fight\n'
#                                   '\n'
#                                   'We passed primordial black holes\n'
#                                   'Fought goblins and trolls on faraway stars\n'
#                                   'Together we dashed through infinity for '
#                                   'honour and glory\n'
#                                   'From Neptune to Mars to Mercury\n'
#                                   'To bring it all to an end, to make our '
#                                   'final stand\n'
#                                   'In unity we rise, we will ascend to realms '
#                                   'we must protect\n'
#                                   'Mighty hammer connects\n'
#                                   'The force to annihilate Zargothrax\n'
#                                   '\n'
#                                   'Yes, mighty warriors! In the name of cosmic '
#                                   'justice we ride.\n'
#                                   'Glory will prevail this day...hail to the '
#                                   'King of Dundee!\n'
#                                   '\n'
#                                   'We are heroes, heroes of Dundee,\n'
#                                   "Now the time has come that we'll make "
#                                   'history\n'
#                                   'We are heroes, heroes of Dundee,\n'
#                                   'We are heroes, legends we will be!',
#                         'song_number': '9'},
#  'Infernus Ad Astra': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                        'album_date': '2015',
#                        'album_type': 'album',
#                        'artist': 'gloryhammer',
#                        'lyrics': 'In the distant future of the year 1992,\r\n'
#                                  'War has returned to the galaxy!',
#                        'song_number': '1'},
#  'Legend Of The Astral Hammer': {'album': 'Space 1992: Rise Of The Chaos '
#                                           'Wizards',
#                                  'album_date': '2015',
#                                  'album_type': 'album',
#                                  'artist': 'gloryhammer',
#                                  'lyrics': 'Slashing my way through an army of '
#                                            'goblins on the dark side of the '
#                                            'moon\n'
#                                            'Far overhead lunar dragons are '
#                                            'swarming, my hammer will be their '
#                                            'doom\n'
#                                            'Angus McFife the 13th my name, the '
#                                            'scion of mighty Dundee\n'
#                                            'Intergalactic great hero of steel, '
#                                            'ruler of the whole galaxy\n'
#                                            'Wielding this ancestral weapon, '
#                                            'the Hammer of Glory its name\n'
#                                            'The kingdom of Fife will forever '
#                                            'proclaim\n'
#                                            '\n'
#                                            'Legend of the Astral Hammer\n'
#                                            'Forged in the heart of the '
#                                            'celestial fire\n'
#                                            'Legend of the Astral Hammer\n'
#                                            'Minuscule goblin, impractical '
#                                            'sword\n'
#                                            'Legend of the Astral Hammer\n'
#                                            'Powered by lasers entwined in a '
#                                            'star\n'
#                                            'Legend of the Astral Hammer\n'
#                                            'Crystal enchantment of steel\n'
#                                            '\n'
#                                            'Aeons ago the starlords descended '
#                                            'Powerful unknown to man\n'
#                                            'With three epic weapons to '
#                                            'safeguard from doom, concealing '
#                                            "them far 'cross the land\n"
#                                            'Relics of legend, relics of might, '
#                                            'forged in a time before time\n'
#                                            'For thousands of years unfathomed '
#                                            'unknown, deep in a mystical '
#                                            'shrine\n'
#                                            '\n'
#                                            'Descendant of ultimate fighter\n'
#                                            'Now battle a war in the stars\n'
#                                            'Defending the kingdom from Demons '
#                                            'of Mars\n'
#                                            '\n'
#                                            'Now Zargothrax rises once more\n'
#                                            'To threaten the force of the '
#                                            'light\n'
#                                            'Assemble the heroes of steel\n'
#                                            'Prepare for the ultimate fight',
#                                  'song_number': '3'},
#  'Questlords Of Inverness, Ride To The Galactic Fortress!': {'album': 'Space '
#                                                                       '1992: '
#                                                                       'Rise Of '
#                                                                       'The '
#                                                                       'Chaos '
#                                                                       'Wizards',
#                                                              'album_date': '2015',
#                                                              'album_type': 'album',
#                                                              'artist': 'gloryhammer',
#                                                              'lyrics': 'The '
#                                                                        'Questlords '
#                                                                        'of '
#                                                                        'Inverness '
#                                                                        'ride\n'
#                                                                        'Far '
#                                                                        'far '
#                                                                        'away, '
#                                                                        'to the '
#                                                                        'ultimate '
#                                                                        'light\n'
#                                                                        'Travelling '
#                                                                        'throughout '
#                                                                        'the '
#                                                                        'time\n'
#                                                                        'The '
#                                                                        'Questlords '
#                                                                        'of '
#                                                                        'Inverness '
#                                                                        'ride\n'
#                                                                        'To '
#                                                                        'Galactic '
#                                                                        'Fortress!\n'
#                                                                        '\n'
#                                                                        'They '
#                                                                        'storm '
#                                                                        'the '
#                                                                        'universe '
#                                                                        'in '
#                                                                        'interstellar '
#                                                                        'time\n'
#                                                                        'From '
#                                                                        'the '
#                                                                        'town '
#                                                                        'of '
#                                                                        'Inverness '
#                                                                        'beneath '
#                                                                        'the '
#                                                                        'ancient '
#                                                                        'sign\n'
#                                                                        'Warriors '
#                                                                        'of '
#                                                                        'power '
#                                                                        'steel '
#                                                                        'who '
#                                                                        'hear '
#                                                                        'galactic '
#                                                                        'cry\n'
#                                                                        'Unicorn '
#                                                                        'defenders, '
#                                                                        'unafraid '
#                                                                        'to '
#                                                                        'die\n'
#                                                                        '\n'
#                                                                        'Zargothrax '
#                                                                        'is '
#                                                                        'riding '
#                                                                        'on, '
#                                                                        'with '
#                                                                        'crystal '
#                                                                        'key in '
#                                                                        'hand\n'
#                                                                        'Nobody '
#                                                                        'can '
#                                                                        'stop '
#                                                                        'him, '
#                                                                        'bring '
#                                                                        'death '
#                                                                        'across '
#                                                                        'the '
#                                                                        'land\n'
#                                                                        'Questlords '
#                                                                        'of '
#                                                                        'Inverness, '
#                                                                        'the '
#                                                                        'time '
#                                                                        'has '
#                                                                        'come '
#                                                                        'to '
#                                                                        'fight\n'
#                                                                        'Ride '
#                                                                        'to '
#                                                                        'space '
#                                                                        'battle '
#                                                                        'with '
#                                                                        'brave '
#                                                                        "highland's "
#                                                                        'might\n'
#                                                                        '\n'
#                                                                        'Questlords '
#                                                                        'arise, '
#                                                                        'fight '
#                                                                        'til we '
#                                                                        'die\n'
#                                                                        'For '
#                                                                        'the '
#                                                                        'honour, '
#                                                                        'the '
#                                                                        'glory, '
#                                                                        'the '
#                                                                        'pride\n'
#                                                                        'Ride '
#                                                                        'on the '
#                                                                        'wind '
#                                                                        'and '
#                                                                        'hail '
#                                                                        'to the '
#                                                                        'king\n'
#                                                                        'When '
#                                                                        'the '
#                                                                        'Questlords '
#                                                                        'of '
#                                                                        'Inverness '
#                                                                        'ride\n'
#                                                                        '\n'
#                                                                        'Mighty '
#                                                                        'heroes '
#                                                                        'quest '
#                                                                        'to '
#                                                                        'Mars '
#                                                                        'to '
#                                                                        'fight '
#                                                                        'the '
#                                                                        'demon '
#                                                                        'horde\n'
#                                                                        'Undead '
#                                                                        'force '
#                                                                        'of '
#                                                                        'terror, '
#                                                                        'will '
#                                                                        'fall '
#                                                                        'beneath '
#                                                                        'the '
#                                                                        'sword\n'
#                                                                        'Raise '
#                                                                        'the '
#                                                                        'flag '
#                                                                        'of '
#                                                                        'Inverness, '
#                                                                        'rally '
#                                                                        'all '
#                                                                        'the '
#                                                                        'troops\n'
#                                                                        'Fight '
#                                                                        'for '
#                                                                        'Dundee '
#                                                                        'and '
#                                                                        'the '
#                                                                        'power '
#                                                                        'of '
#                                                                        'Hoots\n'
#                                                                        '\n'
#                                                                        'Unicorn! '
#                                                                        'Show '
#                                                                        'me the '
#                                                                        'way\n'
#                                                                        'Lead '
#                                                                        'me to '
#                                                                        'the '
#                                                                        'ultimate '
#                                                                        'fortress\n'
#                                                                        'Unicorn! '
#                                                                        'Reveal '
#                                                                        'the '
#                                                                        'truth\n'
#                                                                        'Of the '
#                                                                        'ancient '
#                                                                        'crystal '
#                                                                        'galaxy',
#                                                              'song_number': '7'},
#  'Rise Of The Chaos Wizards': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                                'album_date': '2015',
#                                'album_type': 'album',
#                                'artist': 'gloryhammer',
#                                'lyrics': 'Sanctus dominus\n'
#                                          'Infernus ad astra\n'
#                                          'Sanctus dominus\n'
#                                          'Infernus ad astra\n'
#                                          'Sanctus dominus\n'
#                                          'Infernus ad astra\n'
#                                          'Sanctus dominus\n'
#                                          'Infernus ad astra\n'
#                                          '\n'
#                                          'Across the galaxy a new force of '
#                                          'evil is rising\n'
#                                          'Wizards of Chaos fighting the throne '
#                                          'of brave king of Dundee\n'
#                                          'Entwined by mystic spells, they know '
#                                          'where the sorcerer hidden\n'
#                                          'Imprisoned in ice on the planet of '
#                                          'knights, the powerful heroes of '
#                                          'Crail\n'
#                                          '\n'
#                                          'Eons of warfare returning\n'
#                                          'No longer peace will survive\n'
#                                          'The intergalactic great empire of '
#                                          'Fife will die\n'
#                                          '\n'
#                                          'For the king we will ride\n'
#                                          'To the dark galactic skies\n'
#                                          'To defeat the foes\n'
#                                          'When the Chaos Wizards rise\n'
#                                          'Now the universe will burn\n'
#                                          'Evil sorcerer returns\n'
#                                          'Tragic fate rages tonight\n'
#                                          'Chaos Wizards rise\n'
#                                          '\n'
#                                          'Sanctus dominus\n'
#                                          'Infernus ad astra\n'
#                                          'Sanctus dominus\n'
#                                          'Infernus ad astra\n'
#                                          '\n'
#                                          'Ten centuries ago brave heroes '
#                                          'defeated the wizard\n'
#                                          'Now Chaos reigns and evil returns to '
#                                          'the kingdom of Fife\n'
#                                          'Wizard cultists rage - on dark wings '
#                                          'of steel they are flying\n'
#                                          'To space they must go, great terror '
#                                          'they sow, nothing can stand in their '
#                                          'way\n'
#                                          '\n'
#                                          'The space knights of Crail are '
#                                          'defeated\n'
#                                          'The fortress of Triton is lost\n'
#                                          'Zargothrax rises once more from his '
#                                          'prison of frost\n'
#                                          '\n'
#                                          'For the king we will ride\n'
#                                          'Through the dark galactic skies\n'
#                                          'To defeat the foes\n'
#                                          'When the Chaos Wizards rise\n'
#                                          'Now the universe will burn\n'
#                                          'Evil sorcerer returns\n'
#                                          'Tragic fate rages tonight\n'
#                                          'Chaos Wizards rise\n'
#                                          '\n'
#                                          '[Spoken:]\n'
#                                          'And lo, after centuries of frozen '
#                                          'slumber I am free once more\n'
#                                          'Cosmic infinity courses through my '
#                                          'veins\n'
#                                          'My body is ablaze with astral '
#                                          'charge\n'
#                                          'The galaxy shall once again tremble '
#                                          'before the might of Zargothrax\n'
#                                          '\n'
#                                          'For the king we will ride\n'
#                                          'Through the dark galactic skies\n'
#                                          'To defeat the foes\n'
#                                          'When the Chaos Wizards rise\n'
#                                          'Now the universe will burn\n'
#                                          'Evil sorcerer returns\n'
#                                          'Tragic fate rages tonight\n'
#                                          'Chaos Wizards rise',
#                                'song_number': '2'},
#  'The Hollywood Hootsman': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                             'album_date': '2015',
#                             'album_type': 'album',
#                             'artist': 'gloryhammer',
#                             'lyrics': '1,000 years ago a hero crossed the '
#                                       'sea\r\n'
#                                       'In search of distant realms to claim '
#                                       'his destiny,\r\n'
#                                       'The land of Unst was not enough he had '
#                                       'to conquer more\r\n'
#                                       'Into the west a hero quests, to far '
#                                       'American shores!\r\n'
#                                       'With his mighty battle axe he '
#                                       'slaughtered everything,\r\n'
#                                       'Till all of California did call the '
#                                       'hero king!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       'HAIL TO HOOTS!\r\n'
#                                       'Mighty proud and standing tall,\r\n'
#                                       'A legend to us all!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       "HE'S THE KING!\r\n"
#                                       'Riding from the silver screen,\r\n'
#                                       'into the battlefield!\n'
#                                       '\r\n'
#                                       "He's the king of California....\r\n"
#                                       'HOOTS!\n'
#                                       '\r\n'
#                                       'Immortal warrior with armor made from '
#                                       'wolf,\r\n'
#                                       'His legend proves the centuries with '
#                                       'the power of the hoots!\r\n'
#                                       'His prowess on the battlefield does '
#                                       'show on the stage,\r\n'
#                                       'In Hollywood he found his fame, the '
#                                       'finest of his age!\r\n'
#                                       'The greatest movie star to ever walk '
#                                       'the land,\r\n'
#                                       "If you ever meet this man I'm sure "
#                                       "you'll understand!\n"
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       'HAIL TO HOOTS!\r\n'
#                                       'Mighty proud and standing tall,\r\n'
#                                       'A legend to us all!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       "HE'S THE KING!\r\n"
#                                       'Riding from the silver screen,\r\n'
#                                       'into the battlefield!\n'
#                                       '\r\n'
#                                       "He's the king of California....\r\n"
#                                       'HOOTS!\n'
#                                       '\r\n'
#                                       'Now Angus calls for him to join the '
#                                       'epic fight,\r\n'
#                                       'Once more these mighty warriors will '
#                                       'battle side by side!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       'HAIL TO HOOTS!\r\n'
#                                       'Mighty proud and standing tall,\r\n'
#                                       'A legend to us all!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       "HE'S THE KING!\r\n"
#                                       'Riding from the silver screen,\r\n'
#                                       'into the battlefield!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       'HOOTS, HOOTS!\r\n'
#                                       'Mighty proud and standing tall,\r\n'
#                                       'A legend to us all!\n'
#                                       '\r\n'
#                                       "He's The Hollywood Hootsman!\r\n"
#                                       'HOOTS, HOOTS!\r\n'
#                                       'Riding from the silver screen,\r\n'
#                                       'into the battlefield!\n'
#                                       '\r\n'
#                                       "He's the king of California....\r\n"
#                                       'HOOTS!',
#                             'song_number': '5'},
#  'Universe On Fire': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                       'album_date': '2015',
#                       'album_type': 'album',
#                       'artist': 'gloryhammer',
#                       'lyrics': 'I wanna set the universe on fire\r\n'
#                                 'Feel it burn tonight\r\n'
#                                 'Set the universe on fire\r\n'
#                                 "There's no end in sight\n"
#                                 '\r\n'
#                                 'Bring me to the holy raging power\r\n'
#                                 'Where I find my destiny\r\n'
#                                 'The universe on fire\r\n'
#                                 "You're my guiding light\n"
#                                 '\r\n'
#                                 'Carrying the breath on fire within the lungs '
#                                 'of steel\r\n'
#                                 'Soaring to light the flame forged by cosmic '
#                                 'ordeal\r\n'
#                                 'Ascending in mighty dragons with metal wings '
#                                 'and claw\r\n'
#                                 'In a great battle foregone one thousand years '
#                                 'ago\n'
#                                 '\r\n'
#                                 'Now lead me to the stars\r\n'
#                                 'Atomic flame ignite my heart\n'
#                                 '\r\n'
#                                 'I wanna set the universe on fire\r\n'
#                                 'Feel it burn tonight\r\n'
#                                 'Set the universe on fire\r\n'
#                                 "There's no end in sight\n"
#                                 '\r\n'
#                                 'Bring me to the holy raging power\r\n'
#                                 'Where I find my destiny\r\n'
#                                 'The universe on fire\r\n'
#                                 "You're my guiding light\n"
#                                 '\r\n'
#                                 'Gliding across the sun to soak up all its '
#                                 'might\r\n'
#                                 'Charging my solar gun and prepare for epic '
#                                 'fight\r\n'
#                                 'Questing through nebulas in search for '
#                                 'crystal stone\r\n'
#                                 'That gives me the overdose of force to claim '
#                                 'space throne\n'
#                                 '\r\n'
#                                 'It is time, take up your arms\r\n'
#                                 'Nova bombs and plasma guns\n'
#                                 '\r\n'
#                                 'I wanna set the universe on fire\r\n'
#                                 'Feel it burn tonight\r\n'
#                                 'Set the universe on fire\r\n'
#                                 "There's no end in sight\n"
#                                 '\r\n'
#                                 'Bring me to the holy raging power\r\n'
#                                 'Where I find my destiny\r\n'
#                                 'The universe on fire\r\n'
#                                 "You're my guiding light\n"
#                                 '\r\n'
#                                 'Set me on fire\n'
#                                 '\r\n'
#                                 'I wanna set the universe on fire\r\n'
#                                 'Feel it burn tonight\r\n'
#                                 'Set the universe on fire\r\n'
#                                 "There's no end in sight\n"
#                                 '\r\n'
#                                 'Bring me to the holy raging power\r\n'
#                                 'Where I find my destiny\r\n'
#                                 'The universe on fire\r\n'
#                                 "You're my guiding light\r\n"
#                                 "You're my guiding light\r\n"
#                                 "You're my guiding light",
#                       'song_number': '8'},
#  'Victorious Eagle Warfare': {'album': 'Space 1992: Rise Of The Chaos Wizards',
#                               'album_date': '2015',
#                               'album_type': 'album',
#                               'artist': 'gloryhammer',
#                               'lyrics': 'There was a time when legends of '
#                                         'Crail ran true\n'
#                                         'All over, their majesty everyone '
#                                         'knew\n'
#                                         'But now in the future, defeated by '
#                                         'evil untold\n'
#                                         'We yearn for the knight from story of '
#                                         'old\n'
#                                         '\n'
#                                         'A hero cannot be defeated\n'
#                                         'Simply by making him die\n'
#                                         'Proletius will rise\n'
#                                         'A hologram hero will fight\n'
#                                         '\n'
#                                         'Victorious eagle warfare\n'
#                                         'So glorious, riding high up in the '
#                                         'sky\n'
#                                         'Victorious eagle warfare\n'
#                                         'Brave warriors questing hard until '
#                                         'they die\n'
#                                         'With nothing above but the heavens '
#                                         'above\n'
#                                         'Guiding us on through the war\n'
#                                         'Eagle force\n'
#                                         '\n'
#                                         'Inside the chamber of cryogenetical '
#                                         'fire\n'
#                                         'A magical wizard is doing a spell\n'
#                                         'Powered by robots, a hologram coming '
#                                         'to life\n'
#                                         'To stand at the side of the king of '
#                                         'Fife\n'
#                                         '\n'
#                                         'The galaxy knights are rising\n'
#                                         'Reborn from the ashes of Crail\n'
#                                         'A force for the light\n'
#                                         'To whom we eternally hail\n'
#                                         '\n'
#                                         'Victorious eagle warfare\n'
#                                         'So glorious, riding high up in the '
#                                         'sky\n'
#                                         'Victorious eagle warfare\n'
#                                         'Brave warriors questing hard until '
#                                         'they die\n'
#                                         'With nothing above but the heavens '
#                                         'above\n'
#                                         'Guiding us on through the war\n'
#                                         'Eagle force\n'
#                                         '\n'
#                                         '[Spoken:]\n'
#                                         'Mighty warriors of the galaxy\n'
#                                         'You have proven yourselves to be '
#                                         'mighty indeed\n'
#                                         'Now, who of you will join me in my '
#                                         'Space Knights of Crail?\n'
#                                         '\n'
#                                         'Victorious eagle warfare\n'
#                                         'So glorious, riding high up in the '
#                                         'sky\n'
#                                         'Victorious eagle warfare\n'
#                                         'Brave warriors questing hard until '
#                                         'they die\n'
#                                         'With nothing above but the heavens '
#                                         'above\n'
#                                         'Fight against power of evil corrupt\n'
#                                         'Guiding us on through the war\n'
#                                         'Eagle force',
#                               'song_number': '6'}}

url = "http://www.darklyrics.com/lyrics/fivefingerdeathpunch/thewrongsideofheavenandtherighteoussideofhellvolume1.html#4"
lyrics = d.parse_song_url(url)
# {'album': 'The Wrong Side Of Heaven And The Righteous Side Of Hell, Volume 1',
#  'album_date': '2013',
#  'album_type': 'album',
#  'artist': 'five finger death punch',
#  'lyrics': "I spoke to god today, and she said that she's ashamed.\n"
#            'What have I become, what have I done?\n'
#            "I spoke to the devil today, and he swears he's not to blame.\n"
#            'And I understood, cuz I feel the same.\n'
#            '\n'
#            'Arms wide open, I stand alone.\n'
#            "I'm no hero, and I'm not made of stone.\n"
#            'Right or wrong, I can hardly tell.\n'
#            "I'm on the wrong side of heaven, and the righteous side of hell.\n"
#            "I'm on the wrong side of heaven, and the righteous side, righteous "
#            'side of hell.\n'
#            '\n'
#            'I heard from god today, and she sounded just like me.\n'
#            'What have I done, and who have I become.\n'
#            'I saw the devil today, and he looked a lot like me.\n'
#            'I looked away, I turned away!\n'
#            '\n'
#            'Arms wide open, I stand alone.\n'
#            "I'm no hero, and I'm not made of stone.\n"
#            'Right or wrong, I can hardly tell.\n'
#            "I'm on the wrong side of heaven, and the righteous side of hell.\n"
#            "I'm on the wrong side of heaven, and the righteous side, the "
#            'righteous side of hell.\n'
#            '\n'
#            "I'm not defending, downward descending,\n"
#            'falling further and further away!\n'
#            "I'm closer EVERYDAY!\n"
#            '\n'
#            "I'm getting closer every day, to the end.\n"
#            'The end, The end, the end,\n'
#            "I'm getting closer EVERYDAY!\n"
#            '\n'
#            'Arms wide open, I stand alone.\n'
#            "I'm no hero, and I'm not made of stone.\n"
#            'Right or wrong, I can hardly tell.\n'
#            "I'm on the wrong side of heaven, and the righteous side of hell.\n"
#            "I'm on the wrong side of heaven, and the righteous side of hell.\n"
#            "I'm on the wrong side of heaven, and the righteous side, the "
#            'righteous side of hell.',
#  'song_number': '4'}

url = "http://www.darklyrics.com/b/burzum.html"
albums = d.parse_artist_url(url)
# {'Aske ': [{'album': 'Aske ',
#             'album_type': 'EP',
#             'artist': 'burzum',
#             'song': 'Stemmen Fra Taarnet',
#             'url': 'http://www.darklyrics.com/lyrics/burzum/aske.html#1',
#             'year': '1992'},
#            {'album': 'Aske ',
#             'album_type': 'EP',
#             'artist': 'burzum',
#             'song': 'Dominus Sathanas',
#             'url': 'http://www.darklyrics.com/lyrics/burzum/aske.html#2',
#             'year': '1992'},
#            {'album': 'Aske ',
#             'album_type': 'EP',
#             'artist': 'burzum',
#             'song': 'A Lost Forgotten Sad Spirit',
#             'url': 'http://www.darklyrics.com/lyrics/burzum/aske.html#3',
#             'year': '1992'}],
#  'Belus ': [{'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': 'Leukes Renkespill (Introduksjon)',
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#1',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': "Belus' DÃ¸d",
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#2',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': 'Glemselens Elv',
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#3',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': "Kaimadalthas' Nedstigning",
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#4',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': 'Sverddans',
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#5',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': 'Keliohesten',
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#6',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': 'MorgenrÃ¸de',
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#7',
#              'year': '2010'},
#             {'album': 'Belus ',
#              'album_type': 'album',
#              'artist': 'burzum',
#              'song': "Belus' Tilbakekomst (Konklusjon)",
#              'url': 'http://www.darklyrics.com/lyrics/burzum/belus.html#8',
#              'year': '2010'}],
#  'Burzum ': [{'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Feeble Screams From Forests Unknown',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#1',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Ea, Lord Of The Depths',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#2',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Black Spell Of Destruction',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#3',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Channelling The Power Of Souls Into A New God',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#4',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'War',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#5',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'The Crying Orc',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#6',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'A Lost Forgotten Sad Spirit',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#7',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'My Journey To The Stars',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#8',
#               'year': '1991'},
#              {'album': 'Burzum ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Dungeons Of Darkness',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/burzum.html#9',
#               'year': '1991'}],
#  'DauÃ°i Baldrs ': [{'album': 'DauÃ°i Baldrs ',
#                      'album_type': 'album',
#                      'artist': 'burzum',
#                      'song': 'DauÃ°i Baldrs',
#                      'url': 'http://www.darklyrics.com/lyrics/burzum/daudibaldrs.html#1',
#                      'year': '1997'},
#                     {'album': 'DauÃ°i Baldrs ',
#                      'album_type': 'album',
#                      'artist': 'burzum',
#                      'song': 'HermoÃ°r Ã\x81 HelferÃ°',
#                      'url': 'http://www.darklyrics.com/lyrics/burzum/daudibaldrs.html#2',
#                      'year': '1997'},
#                     {'album': 'DauÃ°i Baldrs ',
#                      'album_type': 'album',
#                      'artist': 'burzum',
#                      'song': 'BÃ¡lferÃ° Baldrs',
#                      'url': 'http://www.darklyrics.com/lyrics/burzum/daudibaldrs.html#3',
#                      'year': '1997'},
#                     {'album': 'DauÃ°i Baldrs ',
#                      'album_type': 'album',
#                      'artist': 'burzum',
#                      'song': 'Ã\x8d Heimr Heljar',
#                      'url': 'http://www.darklyrics.com/lyrics/burzum/daudibaldrs.html#4',
#                      'year': '1997'},
#                     {'album': 'DauÃ°i Baldrs ',
#                      'album_type': 'album',
#                      'artist': 'burzum',
#                      'song': 'Illa TiÃ°andi',
#                      'url': 'http://www.darklyrics.com/lyrics/burzum/daudibaldrs.html#5',
#                      'year': '1997'},
#                     {'album': 'DauÃ°i Baldrs ',
#                      'album_type': 'album',
#                      'artist': 'burzum',
#                      'song': 'MÃ³ti Ragnarokum',
#                      'url': 'http://www.darklyrics.com/lyrics/burzum/daudibaldrs.html#6',
#                      'year': '1997'}],
#  'Det Som Engang Var ': [{'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Den Onde Kysten',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#1',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Key To The Gate',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#2',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'En Ring Til Aa Herske',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#3',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Lost Wisdom',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#4',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Han Som Reiste',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#5',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Naar Himmelen Klarner',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#6',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Snu Mikrokosmos Tegn',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#7',
#                           'year': '1992'},
#                          {'album': 'Det Som Engang Var ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Svarte Troner',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/detsomengangvar.html#8',
#                           'year': '1992'}],
#  'Fallen ': [{'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Fra Verdenstreet (Introduksjon)',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#1',
#               'year': '2011'},
#              {'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Jeg Faller',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#2',
#               'year': '2011'},
#              {'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Valen',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#3',
#               'year': '2011'},
#              {'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Vanvidd',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#4',
#               'year': '2011'},
#              {'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Enhver Til Sitt',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#5',
#               'year': '2011'},
#              {'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Budstikken',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#6',
#               'year': '2011'},
#              {'album': 'Fallen ',
#               'album_type': 'album',
#               'artist': 'burzum',
#               'song': 'Til Hel Og Tilbake Igjen (Konklusjon)',
#               'url': 'http://www.darklyrics.com/lyrics/burzum/fallen.html#7',
#               'year': '2011'}],
#  'Filosofem ': [{'album': 'Filosofem ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Burzum (Dunkelheit)',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/filosofem.html#1',
#                  'year': '1996'},
#                 {'album': 'Filosofem ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': "Jesu Dod (Jesus' Tod)",
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/filosofem.html#2',
#                  'year': '1996'},
#                 {'album': 'Filosofem ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Beholding The Daughters Of The Firmament (Erblicket '
#                          'die TÃ¶chter des Firmaments)',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/filosofem.html#3',
#                  'year': '1996'},
#                 {'album': 'Filosofem ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Decrepitude .I. (Gebrechlichkeit .I.)',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/filosofem.html#4',
#                  'year': '1996'},
#                 {'album': 'Filosofem ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'RundtgÃ¥ing Av Den Transcendentale Egenhetens '
#                          'StÃ¸tte (Rundgang um die transzendentale SÃ¤ule der '
#                          'SingularitÃ¤t)',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/filosofem.html#5',
#                  'year': '1996'},
#                 {'album': 'Filosofem ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Decrepitude .II. (Gebrechlichkeit .II.)',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/filosofem.html#6',
#                  'year': '1996'}],
#  'Forgotten Realms ': [{'album': 'Forgotten Realms ',
#                         'album_type': 'single',
#                         'artist': 'burzum',
#                         'song': 'Forgotten Realms',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/forgottenrealms.html#1',
#                         'year': '2015'}],
#  'HliÃ°skjÃ¡lf ': [{'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': "Tuistos Herz (Tuisto's Heart)",
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#1',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': 'Der Tod Wuotans (The Death of Wuotan)',
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#2',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': 'Ansuzgardaraiwo',
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#3',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': "Die Liebe Nerpus' (Nerpus' Love)",
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#4',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': 'Das Einsame Trauern Von Frijo (The Lonesome '
#                             'Mourning Of Frijo)',
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#5',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': 'Die Kraft De Mitgefuehls (The Power Of Empathy)',
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#6',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': "Frijos Goldene Tranen (Frijo's Golden Tears)",
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#7',
#                     'year': '1999'},
#                    {'album': 'HliÃ°skjÃ¡lf ',
#                     'album_type': 'album',
#                     'artist': 'burzum',
#                     'song': 'Der Weinende Hadnur (The Crying Hadnur)',
#                     'url': 'http://www.darklyrics.com/lyrics/burzum/hlidskjalf.html#8',
#                     'year': '1999'}],
#  'Hvis Lyset Tar Oss ': [{'album': 'Hvis Lyset Tar Oss ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Det Som En Gang Var (Was Einst War)',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/hvislysettaross.html#1',
#                           'year': '1993'},
#                          {'album': 'Hvis Lyset Tar Oss ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Hvis Lyset Tar Oss (Wenn Das Licht Uns '
#                                   'Nimmt)',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/hvislysettaross.html#2',
#                           'year': '1993'},
#                          {'album': 'Hvis Lyset Tar Oss ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Inn I Slottet Far Droemmen (In Das Schloss '
#                                   'Der Traeume)',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/hvislysettaross.html#3',
#                           'year': '1993'},
#                          {'album': 'Hvis Lyset Tar Oss ',
#                           'album_type': 'album',
#                           'artist': 'burzum',
#                           'song': 'Tomhet (Leere)',
#                           'url': 'http://www.darklyrics.com/lyrics/burzum/hvislysettaross.html#4',
#                           'year': '1993'}],
#  'The Ways Of Yore ': [{'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'God From The Machine',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#1',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'The Portal',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#2',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'Heill Ã\x93Ã°inn',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#3',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'The Lady In The Lake',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#4',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'The Coming Of Ettins',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#5',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'The Reckoning Of Man',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#6',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'Heil Freyja',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#7',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'The Ways Of Yore',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#8',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'Ek Fellr (I Am Falling)',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#9',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'Hall Of The Fallen',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#10',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'Autumn Leaves',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#11',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'Emptiness',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#12',
#                         'year': '2014'},
#                        {'album': 'The Ways Of Yore ',
#                         'album_type': 'album',
#                         'artist': 'burzum',
#                         'song': 'To Hel And Back Again',
#                         'url': 'http://www.darklyrics.com/lyrics/burzum/thewaysofyore.html#13',
#                         'year': '2014'}],
#  'Umskiptar ': [{'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'BlÃ³Ã°stokkinn',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#1',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'JÃ³ln',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#2',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Alfadanz',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#3',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Hit Helga TrÃ©',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#4',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Ã\x86ra',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#5',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'HeiÃ°r',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#6',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Valgaldr',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#7',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'GalgviÃ°r',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#8',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Surtr Sunnan',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#9',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'Gullaldr',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#10',
#                  'year': '2012'},
#                 {'album': 'Umskiptar ',
#                  'album_type': 'album',
#                  'artist': 'burzum',
#                  'song': 'NÃ\xadÃ°hÃ¶ggr',
#                  'url': 'http://www.darklyrics.com/lyrics/burzum/umskiptar.html#11',
#                  'year': '2012'}]}

songs = d.search_song("whore")
# {' Celestial Whore': {'artist': 'whythre ',
#                       'name': ' Celestial Whore',
#                       'url': 'http://www.darklyrics.com/lyrics/whythre/helshollows.html#7'},
#  " Do You Think I'm A Whore?": {'artist': 'kittie ',
#                                 'name': " Do You Think I'm A Whore?",
#                                 'url': 'http://www.darklyrics.com/lyrics/kittie/spit.html#4'},
#  ' Gold-Digging Whore': {'artist': 'steel panther ',
#                          'name': ' Gold-Digging Whore',
#                          'url': 'http://www.darklyrics.com/lyrics/steelpanther/ballsout.html#10'},
#  ' High Whore': {'artist': 'raging speedhorn ',
#                  'name': ' High Whore',
#                  'url': 'http://www.darklyrics.com/lyrics/ragingspeedhorn/ragingspeedhorn.html#7'},
#  ' New Orleans Is A Dying Whore': {'artist': 'down ',
#                                    'name': ' New Orleans Is A Dying Whore',
#                                    'url': 'http://www.darklyrics.com/lyrics/down/downii.html#10'},
#  ' She Must Be Gods Whore': {'artist': 'born of sin ',
#                              'name': ' She Must Be Gods Whore',
#                              'url': 'http://www.darklyrics.com/lyrics/bornofsin/letitbegin.html#3'},
#  ' The Whore Of Babylon': {'artist': 'lefay ',
#                            'name': ' The Whore Of Babylon',
#                            'url': 'http://www.darklyrics.com/lyrics/lefay/symphonyofthedamned.html#1'},
#  ' Two Penny Whore': {'artist': 'inkubus sukkubus ',
#                       'name': ' Two Penny Whore',
#                       'url': 'http://www.darklyrics.com/lyrics/inkubussukkubus/thegoat.html#4'},
#  ' Whip The Whore': {'artist': 'azarath ',
#                      'name': ' Whip The Whore',
#                      'url': 'http://www.darklyrics.com/lyrics/azarath/diabolicimpiousevil.html#1'},
#  ' Whore': {'artist': 'in this moment ',
#             'name': ' Whore',
#             'url': 'http://www.darklyrics.com/lyrics/inthismoment/blood.html#4'},
#  ' Whore (Filthy Whore)': {'artist': 'nattefrost ',
#                            'name': ' Whore (Filthy Whore)',
#                            'url': 'http://www.darklyrics.com/lyrics/nattefrost/bloodandvomit.html#7'},
#  ' Whore Of Babylon': {'artist': 'cloven hoof ',
#                        'name': ' Whore Of Babylon',
#                        'url': 'http://www.darklyrics.com/lyrics/clovenhoof/throneofdamnation.html#2'}}

artists = d.search_artist("bloodbath")
# {'a bloodbath in boston': {'artist': 'a bloodbath in boston',
#                            'name': 'A BLOODBATH IN BOSTON',
#                            'url': 'http://www.darklyrics.com/a/abloodbathinboston.html'},
#  'bloodbath': {'artist': 'bloodbath',
#                'name': 'BLOODBATH',
#                'url': 'http://www.darklyrics.com/b/bloodbath.html'}}

albums = d.search_album("odin")
# {' Odin': {'artist': 'wizard ',
#            'name': ' Odin',
#            'url': 'http://www.darklyrics.com/lyrics/wizard/odin.html'},
#  ' Odin Owns Ye All': {'artist': 'einherjer ',
#                        'name': ' Odin Owns Ye All',
#                        'url': 'http://www.darklyrics.com/lyrics/einherjer/odinownsyeall.html'},
#  ' Sons Of Odin': {'artist': 'manowar ',
#                    'name': ' Sons Of Odin',
#                    'url': 'http://www.darklyrics.com/lyrics/manowar/sonsofodin.html'}}

discography = d.search_discography("nargaroth")
# {'Amarok ': [{'album': 'Amarok ',
#               'album_type': 'compilation',
#               'artist': 'nargaroth',
#               'song': 'Herbstleyd',
#               'url': 'http://www.darklyrics.com/lyrics/nargaroth/amarok.html#1',
#               'year': '2000'},
#              {'album': 'Amarok ',
#               'album_type': 'compilation',
#               'artist': 'nargaroth',
#               'song': 'Black Spell Of Destruction',
#               'url': 'http://www.darklyrics.com/lyrics/nargaroth/amarok.html#2',
#               'year': '2000'},
#              {'album': 'Amarok ',
#               'album_type': 'compilation',
#               'artist': 'nargaroth',
#               'song': 'Shall We Begin?',
#               'url': 'http://www.darklyrics.com/lyrics/nargaroth/amarok.html#3',
#               'year': '2000'},
#              {'album': 'Amarok ',
#               'album_type': 'compilation',
#               'artist': 'nargaroth',
#               'song': 'Into The Void',
#               'url': 'http://www.darklyrics.com/lyrics/nargaroth/amarok.html#4',
#               'year': '2000'},
#              {'album': 'Amarok ',
#               'album_type': 'compilation',
#               'artist': 'nargaroth',
#               'song': 'Amarok - Zorn Des Lammes Part II',
#               'url': 'http://www.darklyrics.com/lyrics/nargaroth/amarok.html#5',
#               'year': '2000'},
#              {'album': 'Amarok ',
#               'album_type': 'compilation',
#               'artist': 'nargaroth',
#               'song': "As The Stars Took Me With 'em",
#               'url': 'http://www.darklyrics.com/lyrics/nargaroth/amarok.html#6',
#               'year': '2000'}],
#  'Black Metal Ist Krieg ': [{'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Introduction',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#1',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Black Metal Ist Krieg',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#2',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Far Beyond The Stars',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#3',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Seven Tears Are Flowing To The River',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#4',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'I Burn For You',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#5',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'The Day Burzum Killed Mayhem',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#6',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'PÃ\xadseÃ² Pro Satana',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#7',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Amarok - Zorn Des Lammes III',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#8',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Erik, May You Rape The Angels',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#9',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'The Gates Of Eternity',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#10',
#                              'year': '2001'},
#                             {'album': 'Black Metal Ist Krieg ',
#                              'album_type': 'album',
#                              'artist': 'nargaroth',
#                              'song': 'Possessed By Black Fucking Metal',
#                              'url': 'http://www.darklyrics.com/lyrics/nargaroth/blackmetalistkrieg.html#11',
#                              'year': '2001'}],
#  'Crushing Some Belgian Scum ': [{'album': 'Crushing Some Belgian Scum ',
#                                   'album_type': 'mlp',
#                                   'artist': 'nargaroth',
#                                   'song': 'Black Metal Ist Krieg',
#                                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/crushingsomebelgianscum.html#1',
#                                   'year': '2004'},
#                                  {'album': 'Crushing Some Belgian Scum ',
#                                   'album_type': 'mlp',
#                                   'artist': 'nargaroth',
#                                   'song': 'Possessed By Black Fucking Metal',
#                                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/crushingsomebelgianscum.html#2',
#                                   'year': '2004'},
#                                  {'album': 'Crushing Some Belgian Scum ',
#                                   'album_type': 'mlp',
#                                   'artist': 'nargaroth',
#                                   'song': 'I Burn For You',
#                                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/crushingsomebelgianscum.html#3',
#                                   'year': '2004'},
#                                  {'album': 'Crushing Some Belgian Scum ',
#                                   'album_type': 'mlp',
#                                   'artist': 'nargaroth',
#                                   'song': 'Vom Traum Die Menschheit Zu TÃ¶ten',
#                                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/crushingsomebelgianscum.html#4',
#                                   'year': '2004'}],
#  'Era Of Threnody ': [{'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'Dawn Of Epiphany',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#1',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'Whither Goest Thou',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#2',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'Conjuction Underneath The Alpha Weel',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#3',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': '...as Orphans Drifting In A Desert Night',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#4',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'The Agony Of A Dying Phoenix',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#5',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'Epicedium To A Broken Dream',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#6',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'Love Is A Dog From Hell',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#7',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'Era Of Threnody',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#8',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'TXFO',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#9',
#                        'year': '2017'},
#                       {'album': 'Era Of Threnody ',
#                        'album_type': 'album',
#                        'artist': 'nargaroth',
#                        'song': 'My Eternal Grief, Anguish Neverending',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/eraofthrenody.html#10',
#                        'year': '2017'}],
#  'Geliebte Des Regens ': [{'album': 'Geliebte Des Regens ',
#                            'album_type': 'album',
#                            'artist': 'nargaroth',
#                            'song': 'Intro - Calling The Rain',
#                            'url': 'http://www.darklyrics.com/lyrics/nargaroth/geliebtedesregens.html#1',
#                            'year': '2003'},
#                           {'album': 'Geliebte Des Regens ',
#                            'album_type': 'album',
#                            'artist': 'nargaroth',
#                            'song': 'Manchmal Wenn Sie SchlÃ¤ft',
#                            'url': 'http://www.darklyrics.com/lyrics/nargaroth/geliebtedesregens.html#2',
#                            'year': '2003'},
#                           {'album': 'Geliebte Des Regens ',
#                            'album_type': 'album',
#                            'artist': 'nargaroth',
#                            'song': 'Wenn Regen Liebt',
#                            'url': 'http://www.darklyrics.com/lyrics/nargaroth/geliebtedesregens.html#3',
#                            'year': '2003'},
#                           {'album': 'Geliebte Des Regens ',
#                            'album_type': 'album',
#                            'artist': 'nargaroth',
#                            'song': 'Von Scherbengestalten und Regenspaziergang',
#                            'url': 'http://www.darklyrics.com/lyrics/nargaroth/geliebtedesregens.html#4',
#                            'year': '2003'},
#                           {'album': 'Geliebte Des Regens ',
#                            'album_type': 'album',
#                            'artist': 'nargaroth',
#                            'song': 'Manchmal Wenn Sie SchlÃ¤ft (Alternative '
#                                    'Version)',
#                            'url': 'http://www.darklyrics.com/lyrics/nargaroth/geliebtedesregens.html#5',
#                            'year': '2003'},
#                           {'album': 'Geliebte Des Regens ',
#                            'album_type': 'album',
#                            'artist': 'nargaroth',
#                            'song': "Outro - Leb'Wohl",
#                            'url': 'http://www.darklyrics.com/lyrics/nargaroth/geliebtedesregens.html#6',
#                            'year': '2003'}],
#  'Herbstleyd ': [{'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Introduction',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#1',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Herbstleyd',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#2',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Karmageddon',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#3',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Nargaroth',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#4',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': "Des Alten Kriegers Seelenruh'",
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#5',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Amarok - Zorn Des Lammes',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#6',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Das Schwarze GemÃ¤lde1',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#7',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Vom Traum, Die Menschheit Zu TÃ·ten',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#8',
#                   'year': '1998'},
#                  {'album': 'Herbstleyd ',
#                   'album_type': 'album',
#                   'artist': 'nargaroth',
#                   'song': 'Outroduction',
#                   'url': 'http://www.darklyrics.com/lyrics/nargaroth/herbstleyd.html#9',
#                   'year': '1998'}],
#  'Jahreszeiten ': [{'album': 'Jahreszeiten ',
#                     'album_type': 'album',
#                     'artist': 'nargaroth',
#                     'song': 'Prolog',
#                     'url': 'http://www.darklyrics.com/lyrics/nargaroth/jahreszeiten.html#1',
#                     'year': '2009'},
#                    {'album': 'Jahreszeiten ',
#                     'album_type': 'album',
#                     'artist': 'nargaroth',
#                     'song': 'FrÃ¼hling',
#                     'url': 'http://www.darklyrics.com/lyrics/nargaroth/jahreszeiten.html#2',
#                     'year': '2009'},
#                    {'album': 'Jahreszeiten ',
#                     'album_type': 'album',
#                     'artist': 'nargaroth',
#                     'song': 'Sommer',
#                     'url': 'http://www.darklyrics.com/lyrics/nargaroth/jahreszeiten.html#3',
#                     'year': '2009'},
#                    {'album': 'Jahreszeiten ',
#                     'album_type': 'album',
#                     'artist': 'nargaroth',
#                     'song': 'Herbst',
#                     'url': 'http://www.darklyrics.com/lyrics/nargaroth/jahreszeiten.html#4',
#                     'year': '2009'},
#                    {'album': 'Jahreszeiten ',
#                     'album_type': 'album',
#                     'artist': 'nargaroth',
#                     'song': 'Winter',
#                     'url': 'http://www.darklyrics.com/lyrics/nargaroth/jahreszeiten.html#5',
#                     'year': '2009'}],
#  'Prosatanica Shooting Angels ': [{'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'Love is Always Over With '
#                                            'Ejaculation',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#1',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'Be Dead or Satanic',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#2',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'Satan Industries',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#3',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'Thinking Below the Ocean',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#4',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'Black and Blasphemic Death Metal',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#5',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'A Tear in the Face of Satan',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#6',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'The Dark Side of the Moon',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#7',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'Hunting Season',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#8',
#                                    'year': '2004'},
#                                   {'album': 'Prosatanica Shooting Angels ',
#                                    'album_type': 'album',
#                                    'artist': 'nargaroth',
#                                    'song': 'I Bring My Harvest Home',
#                                    'url': 'http://www.darklyrics.com/lyrics/nargaroth/prosatanicashootingangels.html#9',
#                                    'year': '2004'}],
#  'Rasluka Part I ': [{'album': 'Rasluka Part I ',
#                       'album_type': 'MCD',
#                       'artist': 'nargaroth',
#                       'song': 'Trauermarsch',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukaparti.html#1',
#                       'year': '2004'},
#                      {'album': 'Rasluka Part I ',
#                       'album_type': 'MCD',
#                       'artist': 'nargaroth',
#                       'song': 'Rasluka',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukaparti.html#2',
#                       'year': '2004'},
#                      {'album': 'Rasluka Part I ',
#                       'album_type': 'MCD',
#                       'artist': 'nargaroth',
#                       'song': 'Wo Die Kraniche Ziehn',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukaparti.html#3',
#                       'year': '2004'},
#                      {'album': 'Rasluka Part I ',
#                       'album_type': 'MCD',
#                       'artist': 'nargaroth',
#                       'song': 'TrÃ¤nen Eines Mannes',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukaparti.html#4',
#                       'year': '2004'}],
#  'Rasluka Part II ': [{'album': 'Rasluka Part II ',
#                        'album_type': 'MCD',
#                        'artist': 'nargaroth',
#                        'song': 'Introduction - In Stillem Gedenken',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukapartii.html#1',
#                        'year': '2002'},
#                       {'album': 'Rasluka Part II ',
#                        'album_type': 'MCD',
#                        'artist': 'nargaroth',
#                        'song': "...Und Ich Sah Sonn' Nimmer Heben",
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukapartii.html#2',
#                        'year': '2002'},
#                       {'album': 'Rasluka Part II ',
#                        'album_type': 'MCD',
#                        'artist': 'nargaroth',
#                        'song': 'Abschiedsbrief Des Prometheus',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukapartii.html#3',
#                        'year': '2002'},
#                       {'album': 'Rasluka Part II ',
#                        'album_type': 'MCD',
#                        'artist': 'nargaroth',
#                        'song': '...Vom Freien Willen Eines Schwarzen Einhorns',
#                        'url': 'http://www.darklyrics.com/lyrics/nargaroth/raslukapartii.html#4',
#                        'year': '2002'}],
#  'Semper Fidelis ': [{'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Introduction',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#1',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Artefucked',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#2',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': "Der Satan Ist's",
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#3',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Vereinsamt',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#4',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Der Leiermann',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#5',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Semper Fi',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#6',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Hate Song',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#7',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Into The Dead Faces Of Aftermath',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#8',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Meine Phantasien Sind Wie Brennendes Laub... '
#                               'Nicht Von Dauer...',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#9',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'I Got My Dead Man Sleep',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#10',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'I Still Know',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#11',
#                       'year': '2007'},
#                      {'album': 'Semper Fidelis ',
#                       'album_type': 'album',
#                       'artist': 'nargaroth',
#                       'song': 'Outroduction',
#                       'url': 'http://www.darklyrics.com/lyrics/nargaroth/semperfidelis.html#12',
#                       'year': '2007'}],
#  'Spectral Visions Of Mental Warfare ': [{'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': "Odin's Weeping For JÃ¶rdh",
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#1',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'An Indifferent Cold In The '
#                                                   'Womb Of Eve',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#2',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Diving Among The Daughters '
#                                                   'Of The Sea',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#3',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': "Odin's Weeping For JÃ¶rdh - "
#                                                   'Part II',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#4',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Journey Through My Cosmic '
#                                                   'Cells (The Negation Of God)',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#5',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'A Whisper Underneath The '
#                                                   'Bark Of Old Trees',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#6',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Spectral Visions Of Mental '
#                                                   'Warfare',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#7',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'March Of The Tyrants',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#8',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Roaming Through The Realm '
#                                                   'Of Hel',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#9',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'The Daemons Of Happiness',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#10',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Through Nebular Dimensions '
#                                                   'Of Fallen Eden',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#11',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Forgotten Memory Of A Dying '
#                                                   'Dream',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#12',
#                                           'year': '2011'},
#                                          {'album': 'Spectral Visions Of Mental '
#                                                    'Warfare ',
#                                           'album_type': 'album',
#                                           'artist': 'nargaroth',
#                                           'song': 'Passed Away',
#                                           'url': 'http://www.darklyrics.com/lyrics/nargaroth/spectralvisionsofmentalwarfare.html#13',
#                                           'year': '2011'}]}

lyrics = d.search_lyrics("in league with satan")
# {'1312': {'album': 'When You Were Shouting At The Devil... We Were In League '
#                    'With Satan',
#           'album_date': '2008',
#           'album_type': 'album',
#           'artist': "zimmer's hole",
#           'lyrics': 'Once proud and fearless, what have we become?\n'
#                     'End the time of weakness, we know what must be done\n'
#                     'Rise above a simple purpose, time you know the score\n'
#                     "Either you're the Master, or just another whore...\n"
#                     '\n'
#                     "What's your Quest?\n"
#                     'What are you fighting for?\n'
#                     'Is that your best?\n'
#                     'Just give a little more...\n'
#                     '\n'
#                     'From the smoking ashes, a tribe of Lordes will rise\n'
#                     'Vengeance will rain down from the Northern skies\n'
#                     'Into the frozen North upon the mountain high\n'
#                     "You cannot run from truth, your blood you can't deny\n"
#                     '\n'
#                     'See the demons fly way up there in the sky\n'
#                     'Lightning bolts they strike and you must wonder why\n'
#                     'Never fear my dear because The Hole is here\n'
#                     'Wipe your tears you puss, you might just worship us!\n'
#                     '\n'
#                     'Feel the power, Northern Thunder\n'
#                     'Feel the power, Northern Thunder!\n'
#                     '\n'
#                     'All paths converge, heed the call\n'
#                     "Purpose and Might, we'll claim it all\n"
#                     "It's yours by right, watch the palace fall\n"
#                     '\n'
#                     '1312',
#           'song_number': '4'},
#  'Alright': {'album': 'When You Were Shouting At The Devil... We Were In '
#                       'League With Satan',
#              'album_date': '2008',
#              'album_type': 'album',
#              'artist': "zimmer's hole",
#              'lyrics': 'The iron horse will roll\n'
#                        'More time in the saddle than on solid ground\n'
#                        'The beast that feeds my soul\n'
#                        "A lust for life you can't understand\n"
#                        '\n'
#                        'Alright!\n'
#                        '\n'
#                        'Onward we will ride\n'
#                        'The glorious sound of the hammer down\n'
#                        'Keep on keeping on\n'
#                        'Ahead of the pack with the wind at my back\n'
#                        'Cut the road like a knife\n'
#                        'What else are you doing with your life?\n'
#                        '\n'
#                        'Alright!\n'
#                        '\n'
#                        'Saddle up and ride\n'
#                        "I'm with you brother by your side\n"
#                        '\n'
#                        'Absolution, live by the wheel\n'
#                        'Chase the horizon, a triumph of will\n'
#                        '\n'
#                        'Alright!\n'
#                        '\n'
#                        'The beast shakes the ground\n'
#                        'Bark of thunder, an unholy sound\n'
#                        'Screaming into the wind\n'
#                        "Not for the weak, we'll deafen the meek\n"
#                        'Take your life in your hands\n'
#                        'If I have to explain you would not understand\n'
#                        '\n'
#                        'Alright!',
#              'song_number': '9'},
#  'Anonymous Esophagus': {'album': 'When You Were Shouting At The Devil... We '
#                                   'Were In League With Satan',
#                          'album_date': '2008',
#                          'album_type': 'album',
#                          'artist': "zimmer's hole",
#                          'lyrics': 'Anonymous Esophagus\n'
#                                    'You love to scream and shout\n'
#                                    'Now suck it in the mouth\n'
#                                    'Could come from anyone\n'
#                                    "You don't know where that cum comes from\n"
#                                    '\n'
#                                    'Anonymous Esophagus\n'
#                                    '\n'
#                                    'Now hush, no time to talk\n'
#                                    'Just get down there and suck on my cock\n'
#                                    "No I don't want to know your name\n"
#                                    'Just as long as I came\n'
#                                    '\n'
#                                    'Well my dick just wrote this song\n'
#                                    'Now swallow-balls and all!\n'
#                                    '\n'
#                                    'Anonymous (Mouth) Esophagus\n'
#                                    '\n'
#                                    'Open mouths across the nation\n'
#                                    'Accepting of my donation\n'
#                                    '\n'
#                                    "It's all about my dong\n"
#                                    'My dick should sing this song!\n'
#                                    '\n'
#                                    'Anonymous Esophagus',
#                          'song_number': '8'},
#  "Devil's Mouth": {'album': 'When You Were Shouting At The Devil... We Were In '
#                             'League With Satan',
#                    'album_date': '2008',
#                    'album_type': 'album',
#                    'artist': "zimmer's hole",
#                    'lyrics': 'The Devil Wins\n'
#                              '\n'
#                              "All I hear is the whisper, it's deafening\n"
#                              "Can't resist, not worth fighting my lower brain\n"
#                              "Once more I'm drawn in blindly, she calls again\n"
#                              '\n'
#                              'The blackest of holes, will swallow your soul\n'
#                              "And blood will flow from the Devil's Mouth\n"
#                              "The Devil's Mouth\n"
#                              '\n'
#                              "You always want what you haven't got\n"
#                              "It's all the same\n"
#                              "And when you get there, it ain't what you "
#                              'thought\n'
#                              "That's the game\n"
#                              '\n'
#                              'The blackest of holes will swallow your soul\n'
#                              "When you're down south, it's the Devil's Mouth, "
#                              "son The Devil's Mouth\n"
#                              '\n'
#                              'Beware the Whisper\n'
#                              '\n'
#                              "In and out it's an endless cycle, she owns your "
#                              'soul\n'
#                              'Kneel before your lord and master and serve the '
#                              'Hole\n'
#                              '\n'
#                              'The blackest of holes will swallow your soul\n'
#                              "And blood will flow from the Devil's Mouth\n"
#                              "The Devil's Mouth\n"
#                              '\n'
#                              'Beware the Mouth for it will swallow you whole',
#                    'song_number': '5'},
#  'Fista Corps': {'album': 'When You Were Shouting At The Devil... We Were In '
#                           'League With Satan',
#                  'album_date': '2008',
#                  'album_type': 'album',
#                  'artist': "zimmer's hole",
#                  'lyrics': 'Who says there is no use for the dearly departed\n'
#                            'Just make a fist and the party has started\n'
#                            'Show appreciation for the dead\n'
#                            'They never complain about giving head\n'
#                            '\n'
#                            'Fista Corps\n'
#                            '\n'
#                            'Fits your hand just like a glove\n'
#                            'Now embrace that necro love\n'
#                            'Nothing finer than rotten vagina\n'
#                            'Oh how sweet, the rancid meat\n'
#                            '\n'
#                            'Fista Corps\n'
#                            '\n'
#                            'And now sweet corpse, one last caress\n'
#                            'As I fondle a putrid breast\n'
#                            'Now you fist bang the open vag-anus\n'
#                            "Just kick the bucket, and we'll make ya famous\n"
#                            '\n'
#                            'Fista Corps',
#                  'song_number': '7'},
#  'Fuck My Aching Tits': {'album': 'When You Were Shouting At The Devil... We '
#                                   'Were In League With Satan',
#                          'album_date': '2008',
#                          'album_type': 'album',
#                          'artist': "zimmer's hole",
#                          'lyrics': '[European Bonus Track]\n'
#                                    '\n'
#                                    'Line-up:\n'
#                                    'Chris Valagao : Vocals\n'
#                                    'Jed Simon : Guitars\n'
#                                    'Byron Stroud : Bass\n'
#                                    'Gene Hoglan : Drums\n'
#                                    '\n'
#                                    '2008 Century Media Records\n'
#                                    '\n'
#                                    'Thanks to sh_wildchild, jackyl, ghost_in90 '
#                                    'for sending these lyrics.\n'
#                                    'Submits, comments, corrections are '
#                                    'welcomed at webmaster@darklyrics.com\n'
#                                    "ZIMMER'S HOLE LYRICS",
#                          'song_number': '13'},
#  "Hair Doesn't Grow On Steel": {'album': 'When You Were Shouting At The '
#                                          'Devil... We Were In League With '
#                                          'Satan',
#                                 'album_date': '2008',
#                                 'album_type': 'album',
#                                 'artist': "zimmer's hole",
#                                 'lyrics': 'Glory, defending with honour\n'
#                                           'Glory, Defenders of Truth\n'
#                                           '\n'
#                                           'On steeds through pouring rain\n'
#                                           'To save the world again\n'
#                                           'And before us you may kneel\n'
#                                           "We know what's good and true\n"
#                                           'The fight for Metal is true\n'
#                                           'Your hair does not grow on my '
#                                           'steel\n'
#                                           '\n'
#                                           'Some they may stand and some they '
#                                           'may tell\n'
#                                           'But few will rise up and claim all '
#                                           'of hell\n'
#                                           'Swift is the steel, swing forth the '
#                                           'blade\n'
#                                           'Our enemies fall, be only the '
#                                           'brave\n'
#                                           '\n'
#                                           'Glory, rise up from your knees!\n'
#                                           'Glory, Defenders of Truth\n'
#                                           '\n'
#                                           'On steeds through pouring rain\n'
#                                           'To save Metal again\n'
#                                           'And before us you may kneel\n'
#                                           "We know what's good and true\n"
#                                           'The fight for music is true\n'
#                                           'Your hair does not grow on my '
#                                           'steel\n'
#                                           '\n'
#                                           "Into the fray, I'll die today\n"
#                                           'Not for the meek or afraid\n'
#                                           'Mighty the blade, in fire be '
#                                           'forged\n'
#                                           'This is how heroes are made\n'
#                                           '\n'
#                                           'On steeds through pouring rain\n'
#                                           'To save the world again\n'
#                                           'We need new heroes, not Vince '
#                                           'Neil!!!\n'
#                                           'The legions and the hordes\n'
#                                           'We all will raise our swords\n'
#                                           'Your hair does not grow on my '
#                                           'steel\n'
#                                           '\n'
#                                           "Chaos is coming, it won't be long\n"
#                                           'All must bear witness, united as '
#                                           'one\n'
#                                           'With courage we stand, only the '
#                                           'strong\n'
#                                           "Fight for what's true\n"
#                                           'It lives within all of you...',
#                                 'song_number': '10'},
#  'In League With Satan': {'album': 'When You Were Shouting At The Devil... We '
#                                    'Were In League With Satan',
#                           'album_date': '2008',
#                           'album_type': 'album',
#                           'artist': "zimmer's hole",
#                           'lyrics': '[European Bonus Track]\n'
#                                     '[Venom cover]\n'
#                                     '\n'
#                                     "I'm in league with Satan\n"
#                                     'I was raised in hell\n'
#                                     'I walk the streets of Salem\n'
#                                     'Amongst the living dead\n'
#                                     'I need no one to tell me\n'
#                                     "What's wrong or right\n"
#                                     'I drink the blood of children\n'
#                                     'Stalk my prey at night\n'
#                                     '\n'
#                                     '[Chorus:]\n'
#                                     'Look out beware\n'
#                                     "When the full moon's high n'bright\n"
#                                     "In every way I'm there\n"
#                                     'In every shadow in the night\n'
#                                     "Cause I'm evil in league with Satan\n"
#                                     'Evil in league with Satan\n'
#                                     '\n'
#                                     "I'm in league with Satan\n"
#                                     'Obey his commands\n'
#                                     'With the goat of Mendes\n'
#                                     'Sitting at his left hand\n'
#                                     "I'm in league with Satan\n"
#                                     'I love the dead\n'
#                                     'No one prayed for Sodom\n'
#                                     'As the people fled\n'
#                                     '\n'
#                                     "I'm in league with Satan\n"
#                                     'I am the masters own\n'
#                                     'I drink the juice of women\n'
#                                     'As they lie alone\n'
#                                     "I'm in league with Satan\n"
#                                     'I bear the devils mark\n'
#                                     'I kill the new born baby\n'
#                                     'Tear the infants flesh',
#                           'song_number': '12'},
#  'Regnum Satani (In League With Satan We Ride)': {'album': 'Katun',
#                                                   'album_date': '2007',
#                                                   'album_type': 'album',
#                                                   'artist': 'hacavitz',
#                                                   'lyrics': 'Every dawn and '
#                                                             'for the dead of '
#                                                             'the nite\r\n'
#                                                             'We call to '
#                                                             'thee\r\n'
#                                                             'In nomine dei '
#                                                             'nostri Luciferi '
#                                                             'excelsi\r\n'
#                                                             'Satanas\r\n'
#                                                             'Ad maiorem ad '
#                                                             'gloriam\r\n'
#                                                             'O satanic '
#                                                             'elite\r\n'
#                                                             'Raise the ordo '
#                                                             'draconai\n'
#                                                             '\r\n'
#                                                             'Ave Satanas\r\n'
#                                                             'In league with '
#                                                             'Satan we ride\r\n'
#                                                             'Regnum Satani\r\n'
#                                                             'O achios pethane\n'
#                                                             '\r\n'
#                                                             'Unrest and '
#                                                             'honoured\r\n'
#                                                             'Forever to walk '
#                                                             'these souls\n'
#                                                             '\r\n'
#                                                             'Feeble perversity '
#                                                             'dances thorugh '
#                                                             'the air\r\n'
#                                                             'Smell the ashes '
#                                                             'of knowledge\r\n'
#                                                             'Rise moten '
#                                                             'disease\r\n'
#                                                             'Upheaval of all\n'
#                                                             '\r\n'
#                                                             'Regnum Satani\r\n'
#                                                             'O achios pethane\n'
#                                                             '\r\n'
#                                                             'No\r\n'
#                                                             'Will to exist\r\n'
#                                                             'Pride that '
#                                                             'surrounds and '
#                                                             'mocks\r\n'
#                                                             'Fever\r\n'
#                                                             'So vicious and '
#                                                             'intrincate\r\n'
#                                                             'For\r\n'
#                                                             'The lord obscure '
#                                                             'we ungrace our '
#                                                             'souls\r\n'
#                                                             'Thee essence\r\n'
#                                                             'For honor '
#                                                             'obscure\n'
#                                                             '\r\n'
#                                                             'Regnum satani\r\n'
#                                                             'Domus nocte '
#                                                             'mundi\r\n'
#                                                             'Regnum satani\r\n'
#                                                             'In league with '
#                                                             'Satan we ride\n'
#                                                             '\r\n'
#                                                             'In whores \r\n'
#                                                             'We rejoice\r\n'
#                                                             'For the eve of '
#                                                             'the goat we '
#                                                             'invoke\r\n'
#                                                             'Salve Satanas\r\n'
#                                                             'Nocte vobiseum',
#                                                   'song_number': '1'},
#  'The Flight Of The Night Bat': {'album': 'When You Were Shouting At The '
#                                           'Devil... We Were In League With '
#                                           'Satan',
#                                  'album_date': '2008',
#                                  'album_type': 'album',
#                                  'artist': "zimmer's hole",
#                                  'lyrics': "You fail, who's the Chosen One?\n"
#                                            'Flight of the Knight Bat\n'
#                                            "Greybeard, old man, carpenter's "
#                                            'son\n'
#                                            'Flight of the Knight Bat\n'
#                                            'A demon descends from the night\n'
#                                            'He comes to take innocence\n'
#                                            'Carrying the Damned, the Bird '
#                                            'takes flight\n'
#                                            'Flight of the Knight Bat\n'
#                                            '\n'
#                                            'Oh Lord of Darkness, have you '
#                                            'conquered the sun?\n'
#                                            'Behold, the world has come undone\n'
#                                            '\n'
#                                            'I feel a breakdown\n'
#                                            'Cheeseburger breakdown\n'
#                                            'We need a breakdown\n'
#                                            'Cheeseburger Breakdown!\n'
#                                            '\n'
#                                            "Impale! Who's the Chosen One?\n"
#                                            'Fallen...now rise forgotten Son\n'
#                                            "You fail, who's the Chosen One?\n"
#                                            'Behold, your world has come '
#                                            'undone.\n'
#                                            '\n'
#                                            'Fly away Little Bat...\n'
#                                            "...This Basket of Death you can't "
#                                            'deny!',
#                                  'song_number': '3'},
#  'The Vowel Song': {'album': 'When You Were Shouting At The Devil... We Were '
#                              'In League With Satan',
#                     'album_date': '2008',
#                     'album_type': 'album',
#                     'artist': "zimmer's hole",
#                     'lyrics': 'A, E, I, O, U, and sometimes\n'
#                               'Y are you wasting my air?\n'
#                               'Why are you still here?\n'
#                               'Why must I tolerate, no debate, eliminate!!!\n'
#                               'A, E, I, O, U...SUCK....SUCK!!!',
#                     'song_number': '6'},
#  'We Rule The Fucking Land': {'album': 'When You Were Shouting At The Devil... '
#                                        'We Were In League With Satan',
#                               'album_date': '2008',
#                               'album_type': 'album',
#                               'artist': "zimmer's hole",
#                               'lyrics': "Alright, let's go!\n"
#                                         '\n'
#                                         'Long time, too bad. Much more than '
#                                         'others had\n'
#                                         'Insane and fire branded...WE RULE THE '
#                                         'FUCKING LAND\n'
#                                         "Smoke weed! Drink booze! We haven't "
#                                         'time to lose\n'
#                                         'Devious and underhanded...WE RULE THE '
#                                         'FUCKING LAND\n'
#                                         '\n'
#                                         'Die by My Hand\n'
#                                         'Rule The Land\n'
#                                         'Die by My Hand\n'
#                                         '\n'
#                                         'Come on!\n'
#                                         '\n'
#                                         "Stand up! Be strong! We haven't very "
#                                         'long...\n'
#                                         'Dominate as commanded...WE RULE THE '
#                                         'FUCKING LAND\n'
#                                         'Lookout! Behold! As the time of old\n'
#                                         'Conquest! Victory! WE RULE THE '
#                                         'FUCKING LAND',
#                               'song_number': '2'},
#  "What's My Name...Evil!": {'album': 'When You Were Shouting At The Devil... '
#                                      'We Were In League With Satan',
#                             'album_date': '2008',
#                             'album_type': 'album',
#                             'artist': "zimmer's hole",
#                             'lyrics': 'Enter into my domain\n'
#                                       'All I offer, lies and pain\n'
#                                       'Turning decent into swine\n'
#                                       'Mothers milk into wine\n'
#                                       'Be the wolf that culls the weak\n'
#                                       'Monster walks among the sheep\n'
#                                       'Turn young girls to Jezebels\n'
#                                       'Seething harlots straight from hell\n'
#                                       '\n'
#                                       "What's my name...Evil!\n"
#                                       '\n'
#                                       "Lust for life you can't relieve\n"
#                                       "The years you've spent upon your knees\n"
#                                       "Now's the time to dry your tears\n"
#                                       'I will confirm all your fears\n'
#                                       'Watch the fires burning bright\n'
#                                       'As my shadow swallows light\n'
#                                       'Flames consuming all the lies\n'
#                                       "You're nothing to me\n"
#                                       '\n'
#                                       'Look to the skies and tell me what do '
#                                       'you see?\n'
#                                       'I am the light that shines infernally\n'
#                                       'Lust for my name, my body, my mind, my '
#                                       'seed\n'
#                                       "You can't deny the power coming from "
#                                       'me\n'
#                                       '\n'
#                                       'Living waste so unseen\n'
#                                       'Your pitiful life is but dream\n'
#                                       'Reach out to me and take my hand\n'
#                                       "I'll lead you to the Promised Land\n"
#                                       'Laughing as the Kingdom burns\n'
#                                       'All is lost, nothing learned\n'
#                                       'Legions rise to claim the earth\n'
#                                       'Witness now the dark rebirth\n'
#                                       '\n'
#                                       "What's my name...Evil!",
#                             'song_number': '11'},
#  'When You Were Shouting At The Devil... We Were In League With Satan': {'album': 'When '
#                                                                                   'You '
#                                                                                   'Were '
#                                                                                   'Shouting '
#                                                                                   'At '
#                                                                                   'The '
#                                                                                   'Devil... '
#                                                                                   'We '
#                                                                                   'Were '
#                                                                                   'In '
#                                                                                   'League '
#                                                                                   'With '
#                                                                                   'Satan',
#                                                                          'album_date': '2008',
#                                                                          'album_type': 'album',
#                                                                          'artist': "zimmer's "
#                                                                                    'hole',
#                                                                          'lyrics': 'In '
#                                                                                    'my '
#                                                                                    'youth, '
#                                                                                    'I '
#                                                                                    'learned '
#                                                                                    'the '
#                                                                                    'Truth, '
#                                                                                    'PURE '
#                                                                                    'METAL '
#                                                                                    'was '
#                                                                                    'the '
#                                                                                    'only '
#                                                                                    'way\n'
#                                                                                    'Glam '
#                                                                                    'rock '
#                                                                                    'can '
#                                                                                    'suck '
#                                                                                    'a '
#                                                                                    'cock, '
#                                                                                    "it's "
#                                                                                    'strictly '
#                                                                                    'for '
#                                                                                    'the '
#                                                                                    'closet '
#                                                                                    'gay\n'
#                                                                                    'Burning '
#                                                                                    'bright, '
#                                                                                    'my '
#                                                                                    'wheels '
#                                                                                    'ignite, '
#                                                                                    'burning '
#                                                                                    'to '
#                                                                                    'the '
#                                                                                    'other '
#                                                                                    'side\n'
#                                                                                    'Exodus '
#                                                                                    'was '
#                                                                                    'fucking '
#                                                                                    'right, '
#                                                                                    'ALL '
#                                                                                    'THE '
#                                                                                    'POSEURS '
#                                                                                    'MUST '
#                                                                                    'DIE!\n'
#                                                                                    '\n'
#                                                                                    'When '
#                                                                                    'you '
#                                                                                    'were '
#                                                                                    'Shouting '
#                                                                                    'at '
#                                                                                    'the '
#                                                                                    'Devil\n'
#                                                                                    'We '
#                                                                                    'were '
#                                                                                    'In '
#                                                                                    'League...\n'
#                                                                                    '\n'
#                                                                                    'Drink '
#                                                                                    'and '
#                                                                                    'fight, '
#                                                                                    'every '
#                                                                                    'night, '
#                                                                                    'take '
#                                                                                    'your '
#                                                                                    'women '
#                                                                                    'away\n'
#                                                                                    'Embrace '
#                                                                                    'the '
#                                                                                    'dark '
#                                                                                    'and '
#                                                                                    'leave '
#                                                                                    'your '
#                                                                                    'mark, '
#                                                                                    'you '
#                                                                                    'know '
#                                                                                    "there's "
#                                                                                    'hell '
#                                                                                    'to '
#                                                                                    'pay\n'
#                                                                                    'We '
#                                                                                    'live '
#                                                                                    'proud '
#                                                                                    'and '
#                                                                                    'love '
#                                                                                    'it '
#                                                                                    'loud, '
#                                                                                    'you '
#                                                                                    'wish '
#                                                                                    'you '
#                                                                                    'were '
#                                                                                    'one '
#                                                                                    'of '
#                                                                                    'the '
#                                                                                    "'Crue'\n"
#                                                                                    'Worship '
#                                                                                    'your '
#                                                                                    'transvestite '
#                                                                                    'gods, '
#                                                                                    'my '
#                                                                                    'sword '
#                                                                                    'will '
#                                                                                    'run '
#                                                                                    'you '
#                                                                                    'through!\n'
#                                                                                    '\n'
#                                                                                    'When '
#                                                                                    'you '
#                                                                                    'were '
#                                                                                    'Shouting '
#                                                                                    'at '
#                                                                                    'the '
#                                                                                    'Devil\n'
#                                                                                    'We '
#                                                                                    'were '
#                                                                                    'In '
#                                                                                    'League...\n'
#                                                                                    'When '
#                                                                                    'you '
#                                                                                    'were '
#                                                                                    'Shouting '
#                                                                                    'at '
#                                                                                    'the '
#                                                                                    'Devil\n'
#                                                                                    'We '
#                                                                                    'were '
#                                                                                    'In '
#                                                                                    'League...\n'
#                                                                                    '\n'
#                                                                                    'With '
#                                                                                    'Satan\n'
#                                                                                    '\n'
#                                                                                    'In '
#                                                                                    'the '
#                                                                                    'pit '
#                                                                                    'of '
#                                                                                    'shadows '
#                                                                                    'blows '
#                                                                                    'the '
#                                                                                    'wind '
#                                                                                    'of '
#                                                                                    'stench\n'
#                                                                                    'Familiar '
#                                                                                    'to '
#                                                                                    'those '
#                                                                                    'who '
#                                                                                    'know...',
#                                                                          'song_number': '1'}}