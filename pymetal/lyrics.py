from bs4 import BeautifulSoup
from pymetal.util import merge_dict
from requests_cache import CachedSession
from datetime import timedelta


class DarkLyrics:
    session = CachedSession(backend='memory',
                            expire_after=timedelta(hours=1))
    search_url = "http://www.darklyrics.com/search.php?"

    def search_artist(self, artist, max_pages=1):
        return self.search(artist, max_pages).get("artists", {})

    def search_song(self, song, max_pages=1):
        return self.search(song, max_pages).get("songs", {})

    def search_album(self, album, max_pages=1):
        return self.search(album, max_pages).get("albums", {})

    def search_discography(self, query, max_pages=1):
        data = self.search(query, max_pages)
        disco = {}
        for k in data:
            for entry in data[k]:
                url = data[k][entry]["url"]
                r = self.session.get(url)
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                if "/lyrics/" not in url:
                    merge_dict(disco, self._parse_artist(soup))
        return disco

    def search_lyrics(self, query, max_pages=1):
        data = self.search(query, max_pages)
        lyrics = {}
        for entry in data["songs"]:
            url, num = data["songs"][entry]["url"].split("#")
            r = self.session.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            bucket = self._parse_lyrics(soup)

            for song in bucket:
                if bucket[song]["song_number"] == num:
                    lyrics[song] = bucket[song]
        for entry in data["artists"]:
            url = data["artists"][entry]["url"]
            r = self.session.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            bucket = self._parse_artist(soup)
            for album in bucket:
                songs = bucket[album]
                url = songs[0]["url"].replace("#1", "")
                r = self.session.get(url)
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                merge_dict(lyrics, self._parse_lyrics(soup))
        for entry in data["albums"]:
            url = data["albums"][entry]["url"]
            r = self.session.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            merge_dict(lyrics, self._parse_lyrics(soup))

        return lyrics

    def search(self, query, max_pages=1):
        r = self.session.get(self.search_url,
                             params={"q": query})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        data = self._parse_search(soup)
        if max_pages == -1:
            max_pages = data["num_pages"]
        if max_pages > 1 and data["num_pages"] > 1:
            for p in range(2, data["num_pages"] + 1):
                r = self.session.get(self.search_url,
                                     params={"q": query, "p": p})
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                bucket = self._parse_search(soup)
                bucket.pop("num_pages")
                merge_dict(data, bucket)
                if p > max_pages:
                    break
        data.pop("num_pages")
        return data

    def yield_search(self, query, artists=True, albums=True, songs=True,
                     page=1):
        if page > 1:
            r = self.session.get(self.search_url,
                                 params={"q": query, "p": page})
        else:
            r = self.session.get(self.search_url,
                                 params={"q": query})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        pages = soup.find_all("div", {"class": "search"})
        if len(pages) > 1:
            pages = pages[1].text.split(" ")
        else:
            raise StopIteration
        if pages[-1] == "Next":
            num_pages = int(pages[-2])
        else:
            num_pages = int(pages[-1])
        content = soup.find("div", {"class": "cont"})
        entries = content.find_all("div", {"class": "sen"})
        for e in entries:
            url = e.find("a")["href"]
            name = e.find("h2").text
            if url.startswith("lyrics/"):
                if "#" in url and songs:
                    song_name = name
                    artist = ""
                    if "-" in name:
                        bucket = name.split("-")
                        artist = bucket[0].lower()
                        song_name = "-".join(bucket[1:])
                    yield {"artist": artist, "name": song_name.strip(),
                           "url": "http://www.darklyrics.com/" + url}
                elif albums:
                    album_name = name
                    artist = ""
                    if "-" in name:
                        bucket = name.split("-")
                        artist = bucket[0].lower()
                        album_name = "-".join(bucket[1:])
                    yield {
                        "url": "http://www.darklyrics.com/" + url,
                        "name": album_name.strip(),
                        "artist": artist}
            elif artists:
                yield {"url": url, "name": name, "artist": name.lower()}

        if page + 1 < num_pages:
            for e in self.yield_search(query, artists, albums, songs, page + 1):
                yield e

    def _parse_search(self, soup):

        pages = soup.find_all("div", {"class": "search"})
        if len(pages) > 1:
            pages = pages[1].text.split(" ")
        else:
            return {"artists": {}, "albums": {}, "songs": {}, "num_pages": 0}
        if pages[-1] == "Next":
            num_pages = int(pages[-2])
        else:
            num_pages = int(pages[-1])
        content = soup.find("div", {"class": "cont"})
        entries = content.find_all("div", {"class": "sen"})
        artists = {}
        albums = {}
        songs = {}
        for e in entries:
            url = e.find("a")["href"]
            name = e.find("h2").text
            if url.startswith("lyrics/"):
                if "#" in url:
                    song_name = name
                    artist = ""
                    if "-" in name:
                        bucket = name.split("-")
                        artist = bucket[0].lower()
                        song_name = "-".join(bucket[1:])
                    songs[song_name.strip()] = {"artist": artist,
                                                "name": song_name.strip(),
                                                "url": "http://www.darklyrics.com/"
                                                       + url}
                else:
                    album_name = name
                    artist = ""
                    if "-" in name:
                        bucket = name.split("-")
                        artist = bucket[0].lower()
                        album_name = "-".join(bucket[1:])
                    albums[album_name.strip()] = {
                        "url": "http://www.darklyrics.com/" + url,
                        "name": album_name.strip(),
                        "artist": artist}
            else:
                artists[name.lower()] = {"url": url,
                                         "name": name,
                                         "artist": name.lower()}
        return {"artists": artists, "albums": albums, "songs": songs,
                "num_pages": num_pages}

    def _parse_lyrics(self, soup):
        data = {}
        try:
            artist = soup.find("h1").text.lower().replace(" lyrics", "")
            album = soup.find("div", {"class": "albumlyrics"}).text.split("\n")[1]
            album_type = album.split(":")[0]
            album_name = album.replace('"', "").replace(album_type + ":", "")
            if "(" in album_name:
                album_name, album_date = album_name.replace(")", "").split(" (")
            else:
                album_date = ""
            lyrics = soup.find("div", {"class": "lyrics"})

            if not lyrics:
                return data
            for e in lyrics.find_all("h3"):
                num = e.text[:e.text.find(".")]
                song = e.text[e.text.find(".") + 1:].strip()
                song_lyrics = lyrics.text.split(e.text)[1].split(str(int(num) + 1) + ". ")[0]
                data[song] = {"song_number": num, "lyrics": song_lyrics.strip(),
                              "artist": artist, "album": album_name.strip(),
                              "album_type": album_type, "album_date": album_date}
        except Exception as e:
            print(e)  # TODO debug, this failed here once
        return data

    def _parse_artist(self, soup):
        data = {}
        entries = soup.find_all("div", {"class": "album"})
        artist = soup.find("h1").text.replace(" LYRICS", "").lower()
        for e in entries:
            album_type, name = e.find("h2").text.split(":")
            name, year = name.replace('"', "").replace(")", "").strip().split(
                "(")
            name = name.strip()
            songs = e.find_all("a")
            data[name] = []
            for s in songs:
                url = s["href"].replace("..", "http://www.darklyrics.com")
                song = s.text
                bucket = {"album": name, "year": year, "url": url,
                          "song": song, "album_type": album_type,
                          "artist": artist}
                data[name].append(bucket)
        return data

    def parse_artist_url(self, url):
        assert url.startswith("http://www.darklyrics.com/")
        assert "/lyrics/" not in url
        assert "#" not in url
        r = self.session.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        return self._parse_artist(soup)

    def parse_song_url(self, url):
        assert url.startswith("http://www.darklyrics.com/")
        assert "/lyrics/" in url
        assert "#" in url
        url, num = url.split("#")
        r = self.session.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        lyric = self._parse_lyrics(soup)
        for song in lyric:
            if lyric[song]["song_number"] == num:
                return lyric[song]
        raise NotADirectoryError("invalid song number")

    def parse_album_url(self, url):
        assert url.startswith("http://www.darklyrics.com/")
        assert "/lyrics/" in url
        assert "#" not in url
        r = self.session.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        return self._parse_lyrics(soup)


class AZLyrics:
    session = CachedSession(backend='memory',
                            expire_after=timedelta(hours=1))
    search_url = "https://search.azlyrics.com/search.php?"

    def search_artists(self, artist, max_pages=1, page=1):
        r = self.session.get(self.search_url,
                             params={"q": artist, "w": "artists"})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        panels = soup.find_all("div", {"class": "panel"})
        artists = []
        for p in panels:
            panel_type = p.find("span", {"class": "text-lowercase"}).text
            entries = p.find_all("td", {"class": "text-left"})
            for e in entries:
                name = e.find("b").text
                url = e.find("a")["href"]
                if panel_type == "Artists":
                    artists.append(
                        {"url": url, "name": name})
        if max_pages > 1:
            try:
                artists += self.search_artists(song, max_pages, page + 1)
            except:
                pass
        return artists

    def search_songs(self, song, max_pages=1, page=1):
        r = self.session.get(self.search_url,
                             params={"q": song, "w": "songs"})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        panels = soup.find_all("div", {"class": "panel"})
        songs = []
        for p in panels:
            panel_type = p.find("span", {"class": "text-lowercase"}).text
            entries = p.find_all("td", {"class": "text-left"})
            for e in entries:
                name = e.find("b").text
                artist = e.find_all("b")[1].text
                url = e.find("a")["href"]
                if panel_type == "Songs":
                    songs.append({"song": name, "url": url, "artist": artist})
        if max_pages > 1:
            try:
                songs += self.search_songs(song, max_pages, page + 1)
            except:
                pass
        return songs

    def yield_songs(self, song, page=1):
        r = self.session.get(self.search_url,
                             params={"q": song, "w": "songs"})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        panels = soup.find_all("div", {"class": "panel"})
        for p in panels:
            panel_type = p.find("span", {"class": "text-lowercase"}).text
            entries = p.find_all("td", {"class": "text-left"})
            for e in entries:
                name = e.find("b").text
                artist = e.find_all("b")[1].text
                url = e.find("a")["href"]
                if panel_type == "Songs":
                    yield {"song": name, "url": url, "artist": artist}
        try:
            for song in self.yield_songs(song, page + 1):
                yield song
        except:
            pass

    def yield_artists(self, artist, max_pages=1, page=1):
        r = self.session.get(self.search_url,
                             params={"q": artist, "w": "artists"})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        panels = soup.find_all("div", {"class": "panel"})
        artists = []
        for p in panels:
            panel_type = p.find("span", {"class": "text-lowercase"}).text
            entries = p.find_all("td", {"class": "text-left"})
            for e in entries:
                name = e.find("b").text
                url = e.find("a")["href"]
                if panel_type == "Artists":
                    yield {"url": url, "name": name}
        if max_pages > 1:
            try:
                artists += self.search_artists(song, max_pages, page + 1)
            except:
                pass
        return artists

    def quick_search(self, query):
        r = self.session.get(self.search_url,
                             params={"q": query})
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        panels = soup.find_all("div", {"class": "panel"})
        artists = {}
        songs = {}
        albums = {}
        for p in panels:
            panel_type = p.find("span", {"class": "text-lowercase"}).text
            entries = p.find_all("td", {"class": "text-left"})
            for e in entries:
                name = e.find("b").text
                url = e.find("a")["href"]
                if panel_type == "Artists":
                    artists[name] = url
                elif panel_type == "Songs":
                    songs[name] = url
                elif panel_type == "Albums":
                    albums[name] = url
        return {"artists": artists, "songs": songs, "albums": albums}

    def parse_artist_url(self, url):
        r = self.session.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        artist = soup.find("h1").text.replace(" Lyrics", "")
        lyrics = soup.find(id="listAlbum")
        songs = []
        for url in lyrics.find_all("a"):
            if url.get("href"):
                songs.append({"url": "https://www.azlyrics.com/lyrics" +
                                     url["href"][2:],
                              "name": url.text})
        albums = []
        for album in soup.find_all("div", {"class": "album"}):
            album_type = album.text.split(":")[0]
            album_name = album.text.split(":")[1].split("(")[0].replace('"', "").strip()
            if ")" in album.text:
                album_date = album.text.split(":")[1].split("(")[1].replace(')', "").strip()
            else:
                album_date = ""
            albums.append({"name": album_name, "album_type": album_type,
                           "release_date": album_date})
        return {"artist": artist, "songs": songs, "albums": albums}

    def parse_song_url(self, url):
        r = self.session.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        artist = soup.find("h2").text.replace(" Lyrics", "")
        song = soup.find_all("b")[1].text.replace('"', "")
        album = soup.find_all("b")[2].text.replace('"', "")
        lyrics = soup.find("div", {"class": "col-xs-12 col-lg-8 "
                                            "text-center"}).text
        lyrics = lyrics.split("\r")[1].strip()
        return {"song": song.replace('"', ""), "artist": artist,
                "album": album, "lyrics": lyrics}


if __name__ == "__main__":
    from pprint import pprint

    d = DarkLyrics()

    for artist in d.yield_search("arch enemy", albums=False, songs=False):
        print(artist)
        break

    for album in d.yield_search("space 1992", songs=False, artists=False):
        print(album)
        break

    for song in d.yield_search("in league with satan", albums=False,
                               artists=False):
        print(song)
        break

    az = AZLyrics()

    search = az.quick_search("godsmack")
    # {'artists': {'Godsmack': 'https://www.azlyrics.com/g/godsmack.html'},
    #  'songs': {'Bad Religion': 'https://www.azlyrics.com/lyrics/godsmack/badreligion.html',
    #            'Bulletproof': 'https://www.azlyrics.com/lyrics/godsmack/bulletproof.html',
    #            'I Stand Alone': 'https://www.azlyrics.com/lyrics/godsmack/istandalone.html',
    #            'Straight Out Of Line': 'https://www.azlyrics.com/lyrics/godsmack/straightoutofline.html',
    #            'Under Your Scars': 'https://www.azlyrics.com/lyrics/godsmack/underyourscars.html'}}

    for artist in az.yield_artists("steel panther"):
        print(artist)
        break
    # {'name': 'Steel Panther', 'url': 'https://www.azlyrics.com/s/steelpanther.html'}

    for song in az.yield_songs("i get off"):
        print(song)
        break
    # {'song': 'I Get Off', 'url': 'https://www.azlyrics.com/lyrics/halestorm/igetoff.html', 'artist': 'Halestorm'}

    lyrics = az.parse_song_url("https://www.azlyrics.com/lyrics/steelpanther/deathtoallbutmetal.html")
    pprint(lyrics)
    # All right!
    # Yeah!
    # C-c-come on!
    #
    # Fuck the Goo Goo Dolls, they can suck my balls
    # They look like the dorks that hang out at the mall
    # Eminem can suck it, so can Dr. Dre
    # They can suck each other, just because they're gay
    #
    # They can suck a dick, they can lick a sack
    # Everybody shout, "Heavy metal's back!"
    #
    # Death to all but metal
    # Death to all but metal
    # Death to all but metal
    #
    # Death to Papa Roach, Blink 182
    # All those fucking pussies sounds like doggy doo
    # Wearing baggy pants, spiking up their hair
    # They're not worth the crust on my underwear
    #
    # Where is Def Leppard? Where is MÃ¶tley CrÃ¼e?
    # Why do all my lyrics sound like Dr. Seuss?
    #
    # Death to all but metal
    # Death to all but metal
    # Death to all but metal
    #
    # Kill those fucking fuckheads who program MTV
    # They can suck my ass with all the record companies
    #
    # Death to Britney Spears, kill the little slut
    # Kill Madonna too and then fuck her in the butt
    # Fuck Mariah Carey, death to Sheryl Crow
    # They can kiss each other on their camel toe
    #
    # 50 Cent's a fag, so is Kanye West
    # Shooting hot sperm on each others' chest
    #
    # Death to all but metal
    # Death to all but metal
    # Death to all but metal

    discography = az.parse_artist_url(
        "https://www.azlyrics.com/m/motleycrue.html")
    pprint(discography)
    # {'albums': [{'album_type': 'album',
    #              'name': 'Too Fast For Love',
    #              'release_date': '1981'},
    #             {'album_type': 'album',
    #              'name': 'Shout At The Devil',
    #              'release_date': '1983'},
    #             {'album_type': 'album',
    #              'name': 'Theatre Of Pain',
    #              'release_date': '1985'},
    # ....],
    #  'artist': 'Motley Crue',
    #  'songs': [{'name': 'Live Wire',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/livewire.html'},
    #            {'name': 'Come On And Dance',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/comeonanddance.html'},
    #            {'name': 'Public Enemy #1',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/publicenemy1.html'},
    #            ...
    #            {'name': 'Just Another Psycho',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/justanotherpsycho.html'},
    #            {'name': 'Chicks = Trouble',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/chickstrouble.html'},
    #            {'name': "This Ain't A Love Song",
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/thisaintalovesong.html'},
    #            {'name': 'White Trash Circus',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/whitetrashcircus.html'},
    #            {'name': "Goin' Out Swingin'",
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/goinoutswingin.html'},
    #            {'name': '10.000 Miles Away',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/10000milesaway.html'},
    #            {'name': 'All Bad Things',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/allbadthings.html'},
    #            {'name': 'Bitter Pill',
    #             'url': 'https://www.azlyrics.com/lyrics/lyrics/motleycrue/bitterpill.html'}]}
