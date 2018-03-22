import requests
from lxml import html
import re
import json
import sys
if sys.version_info[0] < 3:
    from urllib import urlencode
    from urllib2 import urlopen
else:
    from urllib.request import urlopen
    from urllib.parse import urlencode


__author__ = "jarbas"


class MetalArchives(object):
    site_url = 'https://www.metal-archives.com/'
    url_search_songs = 'search/ajax-advanced/searching/songs?'
    url_search_bands = 'search/ajax-advanced/searching/bands?'
    url_lyrics = 'release/ajax-view-lyrics/id/'
    lyrics_not_available = '(lyrics not available)'
    lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
    band_name_re = re.compile(r'title="(?P<name>.*)\"')
    tags_re = re.compile(r'<[^>]+>')

    @staticmethod
    def get_band_data(url):
        result = {}
        response = requests.get(url)
        tree = html.fromstring(response.content)
        result["name"] = \
            tree.xpath('//*[@id="band_info"]/h1/a/text()')
        result["url"] = \
            tree.xpath('//*[@id="band_info"]/h1/a/@href')
        result["style"] = \
            tree.xpath(".//*[@id='band_stats']/dl[2]/dd[1]/text()")
        result["theme"] = \
            tree.xpath(".//*[@id='band_stats']/dl[2]/dd[2]/text()")
        result["label"] = \
            tree.xpath(".//*[@id='band_stats']/dl[2]/dd[3]/text()")
        result["country"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[1]/a/text()")
        result["location"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[2]/text()")
        result["active"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[3]/text()")
        result["date"] = \
            tree.xpath(".//*[@id='band_stats']/dl[1]/dd[4]/text()")
        years_active = \
            tree.xpath(".//*[@id='band_stats']/dl[3]/dd/text()")
        result["years"] = years_active

        for r in result.keys():
            if isinstance(result[r], list) and len(result[r]) == 1:
                result[r] = result[r][0]
            elif isinstance(result[r], list) and len(result[r]) == 0:
                result[r] = None
            if isinstance(result[r], basestring) and result[r] == 'N/A':
                result[r] = None
            if r == "years":
                result[r] = result[r][0].rstrip().lstrip()
            if r == "theme" and result[r] is not None:
                result[r] = result[r].split(",")
        return result

    def random_band(self):
        return self.get_band_data('http://www.metal-archives.com/band/random')

    def search_song(self, song_title="", band_name=""):
        params = dict(bandName=band_name, songTitle=song_title)
        url = self.site_url + self.url_search_songs + urlencode(params)
        songs = json.load(urlopen(url))['aaData']
        for song in songs:
            data = {"album_url": song[0][song[0].find('href="') + 5:song[0].find('" title=')],
                    "band_name": song[0][song[0].find('>') + 1:song[0].find('</a')],
                    "album_name": song[1][song[1].find('">') + 2:song[1].find('</a')],
                    "album_type": song[2],
                    "song_name": song[3],
                    "song_id": self.lyric_id_re.search(song[4]).group("id")}
            yield data

    def search_band(self, band_name="", genre="", start=0):
        params = dict(bandName=band_name, genre=genre, iDisplayStart=start)
        url = self.site_url + self.url_search_bands + urlencode(params)
        bands, num = json.load(urlopen(url))['aaData'], json.load(urlopen(url))["iTotalRecords"]
        for band in bands:
            data = {"url": band[0][band[0].find('href="') + 5:band[0].find('">')],
                    "name": band[0][band[0].find('">') + 2:band[0].find('</a>')],
                    "genre": band[1],
                    "country": band[2]}
            yield data

    def get_lyrics(self, song_id):
        url = self.site_url + self.url_lyrics + song_id
        lyrics = self.tags_re.sub('', urlopen(url).read().strip()).decode('utf-8')
        if lyrics == self.lyrics_not_available:
            return None
        return lyrics


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
