# pymetal

python api for [Encyclopaedia Metallum](https://www.metal-archives.com/)

# install

    pip install git+https://www.github.com/jarbasal/pymetal

# usage

    from pymetal import MetalArchives

    m = MetalArchives()
    print m.random_band()
    print m.get_band_data("https://www.metal-archives.com/bands/Burzum/88")
    for band in m.search_band("metallica"):
        print band
    for band in m.search_band(genre="black metal"):
        print band
    for song in m.search_song(band_name="metallica"):
        print song
    print m.get_lyrics("67900")