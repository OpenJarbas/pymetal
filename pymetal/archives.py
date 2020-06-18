from requests_cache import CachedSession
from datetime import timedelta
from lxml import html
import re
from pymetal.util import get_random_user_agent


class MetalArchives:
    session = CachedSession(backend='memory',
                            expire_after=timedelta(hours=1))
    site_url = 'https://www.metal-archives.com/'
    url_search_songs = 'search/ajax-advanced/searching/songs?'
    url_search_bands = 'search/ajax-advanced/searching/bands?'
    url_lyrics = 'release/ajax-view-lyrics/id/'
    lyrics_not_available = '(lyrics not available)'
    lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
    band_name_re = re.compile(r'title="(?P<name>.*)\"')
    tags_re = re.compile(r'<[^>]+>')
    genres = ["black", "death", "doom", "stoner", "sludge", "electronic",
              "industrial", "experimental", "avant-garde", "folk", "viking",
              "pagan", "gothic", "grindcore", "groove", "heavy", "metalcore",
              "deathcore", "power", "progressive", "speed", "symphonic",
              "thrash"]

    @staticmethod
    def get_band_data(url):
        result = {}
        response = MetalArchives.session.get(url,
                                             headers={'User-Agent': get_random_user_agent()})
        tree = html.fromstring(response.content)
        result["name"] = \
            tree.xpath('//*[@id="band_info"]/h1/a/text()')
        result["url"] = \
            tree.xpath('//*[@id="band_info"]/h1/a/@href')
        result["genre"] = \
            tree.xpath(".//*[@id='band_stats']/dl[2]/dd[1]/text()")
        result["theme"] = \
            tree.xpath(".//*[@id='band_stats']/dl[2]/dd[2]/text()")
        result["label"] = \
            tree.xpath(".//*[@id='band_stats']/dl[2]/dd[3]/text()")
        result["country"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[1]/a/text()")
        result["location"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[2]/text()")
        result["status"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[3]/text()")
        result["date"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[4]/text()")
        years_active = \
            tree.xpath(".//*[@id='band_stats']/dl[3]/dd/text()")
        # result["years"] = years_active[0]

        for r in result.keys():
            if isinstance(result[r], list) and len(result[r]) == 1:
                result[r] = result[r][0]
            elif isinstance(result[r], list) and len(result[r]) == 0:
                result[r] = None
            if isinstance(result[r], str) and result[r] == 'N/A':
                result[r] = None
            if r == "years":
                if "," in result[r]:
                    years = result[r].split(",")
                    result[r] = [y.rstrip().lstrip() for y in years]
                else:
                    result[r] = [result[r].rstrip().lstrip()]
            if r == "theme" and result[r] is not None:
                result[r] = result[r].split(",")
        return result

    def random_band(self, genre=None):
        band = self.get_band_data('http://www.metal-archives.com/band/random')
        if genre is not None:
            genre = genre.lower() \
                .replace("death core", "deathcore") \
                .replace("metal core", "metalcore") \
                .replace("metal", "") \
                .replace("trash", "thrash") \
                .rstrip().lstrip()
            if genre not in self.genres:
                return {}
            band_genre = band["genre"] \
                .lower() \
                .replace("death core", "deathcore") \
                .replace("metal core", "metalcore") \
                .replace("metal", "") \
                .replace("trash", "thrash") \
                .rstrip().lstrip()
            if "/" in band_genre:
                band_genres = band_genre.split("/")
                for g in band_genres:
                    if genre == g:
                        return band
            while genre != band_genre:
                band = self.get_band_data(
                    'http://www.metal-archives.com/band/random')
                band_genre = band["genre"] \
                    .lower() \
                    .replace("death core", "deathcore") \
                    .replace("metal core", "metalcore") \
                    .replace("metal", "") \
                    .replace("trash", "thrash") \
                    .rstrip().lstrip()
                if "/" in band_genre:
                    band_genres = band_genre.split("/")
                    for g in band_genres:
                        if genre == g:
                            return band
        return band

    def search_song(self, song_title="", band_name="", album_type="any",
                    excluded_album_types=None):
        params = dict(bandName=band_name, songTitle=song_title)
        url = self.site_url + self.url_search_songs
        data = self.session.get(url, params=params,
                                headers={'User-Agent': get_random_user_agent()}).json()
        songs = data['aaData']
        excluded_album_types = excluded_album_types or []
        for song in songs:
            if album_type != "any":
                if song[2] != album_type:
                    continue
            if song[2] in excluded_album_types:
                continue
            data = {"album_url": song[0][
                                 song[0].find('href="') + 6:song[0].find(
                                     '" title=')],
                    "band_name": song[0][
                                 song[0].find('>') + 1:song[0].find('</a')],
                    "album_name": song[1][
                                  song[1].find('">') + 2:song[1].find('</a')],
                    "album_type": song[2],
                    "song_name": song[3],
                    "song_id": self.lyric_id_re.search(song[4]).group("id")}
            yield data

    def search_band(self, band_name="", genre="", index=0):
        params = dict(bandName=band_name, genre=genre, iDisplayStart=index)
        url = self.site_url + self.url_search_bands
        data = self.session.get(url, params=params,
                                headers={'User-Agent': get_random_user_agent()}).json()
        bands, num = data['aaData'], data["iTotalRecords"]
        for band in bands:
            data = {
                "url": band[0][band[0].find('href="') + 6:band[0].find('">')],
                "name": band[0][band[0].find('">') + 2:band[0].find('</a>')],
                "genre": band[1],
                "country": band[2]}
            yield data

    def get_lyrics_by_song_id(self, song_id):
        url = self.site_url + self.url_lyrics + song_id
        data = self.session.get(url,
                            headers={'User-Agent': get_random_user_agent()})
        lyrics = self.tags_re.sub('', data.text.strip())
        return lyrics

    def get_lyrics(self, song_title="", band_name="", album_type="any",
                   excluded_album_types=None):
        for song in self.search_song(song_title=song_title,
                                     band_name=band_name,
                                     album_type=album_type,
                                     excluded_album_types=excluded_album_types):

            song_id = song["song_id"]
            lyrics = self.get_lyrics_by_song_id(song_id)
            if lyrics != self.lyrics_not_available:
                yield lyrics

    def search_lyrics(self, band_name="", genre="", index=0):
        for band in self.search_band(band_name, genre, index):
            band_name = band["name"]
            for lyrics in self.get_lyrics(band_name=band_name):
                yield lyrics


if __name__ == "__main__":
    m = MetalArchives()
    for l in m.search_lyrics("inquisition"):
        print(l)
