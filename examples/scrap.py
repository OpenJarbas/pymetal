from pymetal.lyrics import DarkLyrics, AZLyrics


def get_dark_lyrics(artist):
    d = DarkLyrics()
    general_search = d.search_artist(artist)
    data = d.parse_artist_url(general_search[artist]["url"])
    for album in data:
        for song in data[album]:
            song_data = d.parse_song_url(song["url"])
            if song_data["lyrics"]:
                yield song_data["lyrics"]


def get_az_lyrics(artist):
    az = AZLyrics()
    for song in az.search_songs(artist):
        yield az.parse_song_url(song["url"])["lyrics"]


for murder_lyrics in get_dark_lyrics("six feet under"):
    print(murder_lyrics)
for evil_lyrics in get_dark_lyrics("inquisition"):
    print(evil_lyrics)
for bitchy_lyrics in get_az_lyrics("halestorm"):
    print(bitchy_lyrics)
for dark_lyrics in get_dark_lyrics("in this moment"):
    print(dark_lyrics)
