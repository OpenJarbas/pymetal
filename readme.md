# pymetal

python api for [Encyclopaedia Metallum](https://www.metal-archives.com/) and
 [DarkLyrics](http://www.darklyrics.com/)

## install

    pip install pymetal

## Searching MetalArchives

    from pymetal import MetalArchives

    m = MetalArchives()
    print m.random_band()

    # output:
    #  {'genre': 'Melodic Power Metal',
    # 'name': 'Divinus',
    # 'url': 'https://www.metal-archives.com/bands/Divinus/12982',
    # 'country': 'Germany',
    # 'label': 'Unsigned/independent',
    # 'date': '1992',
    # 'theme': None,
    # 'location': 'Kaiserslautern, Rhineland-Palatinate',
    # 'status': 'Active',
    # 'years': ['1992-present']}

    print m.get_band_data("https://www.metal-archives.com/bands/Burzum/88")

    # output:
    # {'genre': 'Black Metal, Ambient',
    # 'name': 'Burzum',
    # 'url': 'https://www.metal-archives.com/bands/Burzum/88',
    # 'country': 'Norway',
    # 'label': None,
    # 'date': '1991',
    # 'theme': ['Myths', ' Folklore', ' Odalism', ' Darkness', ' Philosophy'],
    # 'location': u'Bergen (early), B\xf8 (mid), Limousin, France (later)',
    # 'status': 'Active',
    # 'years': ['1991-2000', '2009-present']}

    # generator, not a list
    for band in m.search_band("metallica"):
        print band
        # output:
        # {'url': u'"https://www.metal-archives.com/bands/Metallica/125',
        # 'genre': u'Thrash Metal (early), Hard Rock/Heavy/Thrash Metal (later)',
        # 'name': u'Metallica',
        # 'country': u'United States'}

    # generator, not a list
    for song in m.search_song("black metal ist krieg"):
        print song
        break

        # output:
        # {'song_id': u'1780488',
        # 'band_name': u'Bergen 88 Belsen',
        # 'song_name': u'Black Metal ist Krieg',
        # 'album_type': u'Demo',
        # 'album_url': u'"https://www.metal-archives.com/bands/Bergen_88_Belsen/3540292675',
        # 'album_name': u'Demo'}


    # generator, not a list
    for lyrics in m.get_lyrics(song_title="ace of spades",
                              band_name="Motorhead"):
        print lyrics
        break
            # output:
            # If you like to gamble, I tell you I'm your man,
            # You win some, lose some, all the same to me,
            # The pleasure is to play, makes no difference what you say,
            # I don't share your greed, the only card I need is
            # The Ace Of Spades

            # Playing for the high one, dancing with the devil,
            # Going with the flow, it's all the same to me,
            # Seven or Eleven, snake eyes watching you,
            # Double up or quit, double stake or split,
            # The Ace Of Spades

            # You know I'm born to lose, and gambling's for fools,
            # But that's the way I like it baby,
            # I don't wanna live for ever,
            # And don't forget the joker!

            # Pushing up the ante, I know you wanna see me,
            # Read 'em and weep, the dead man's hand again,
            # I see it in your eyes, take one look and die,
            # The only thing you see, you know it's gonna be,
            # The Ace Of Spades

    # generator, not a list
    for lyrics in m.search_lyrics(genre="death metal"):
            print lyrics
            break
            # output:
            # endless eons
            # fruitless quest
            # destiny now within grasp
            # violent eddy
            # currents
            # dimensional decompression
            # pulling the earth and the moon
            # through
            # the dark caesura
            # vacuum loses orbit
            # binary eclipse
            # molecular
            # circumvention
            # fiery microchasm
            # in the negative void
            # mankind inert; chronic
            # limbo
            # bathed in ultraviolet dead shadows
            # neutrinos pulling down
            # passing
            # through positive
            # matter molecularly decompose
            # lifeless matter breaking down
            # then refusing
            # grisly mutations
            # returning to the plan
            # mankind writhing in
            # pain
            # earth
            # lost orbit; stagnant in space
            # vegetating; revelating
            # sun's
            # zenith deterred
            # partially eclipsed on the horizon
            # unvisioned
            # prophecy
            # cessating planet
            # impending death
            # mankind caught in the grip of leap hour
            # tumultuous... vexating
            # mass
            # atom separation dissolving
            # shrinking the earthen
            # core... implode
            # venting, burning, surface, corrodes
            # lava, fire, air, explodes
            # hydrogen, oxygen
            # supernova
            # gravitation, inertia
            # black.. hole.. tethering.. inward
            # the
            # planets align one last time
            # winding around the anomaly
            # moon fragmenting, then
            # descending
            # into the newborn vortex
            # solar system; centrifuge
            # body collisions
            # at light speeds
            # random explosions, stars erupt
            # dying lights; enter
            # fate
            # timeless, apocalypse, azygous,
            # ending... leaving
            # behind... nothing
            # vacuous, vague spectres still revolve
            # around a dead hole
            

## Seaching DarkLyrics


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

    songs = d.search_song("whore")
    # {' Celestial Whore': {'artist': 'whythre ',
    #                       'name': ' Celestial Whore',
    #                       'url': 'http://www.darklyrics.com/lyrics/whythre/helshollows.html#7'},
    ...
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
    ...
    
    
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
    # ...
  

## related projects


[Metal Dataset](https://github.com/JarbasAI/metal_dataset)

