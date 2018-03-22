# pymetal

python api for [Encyclopaedia Metallum](https://www.metal-archives.com/)

# install

    pip install git+https://www.github.com/jarbasal/pymetal

# related projects


[Metal Dataset](https://github.com/JarbasAI/metal_dataset)


# usage

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
    # 'active': 'Active',
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
    # 'active': 'Active',
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