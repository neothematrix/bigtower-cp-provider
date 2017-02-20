import traceback

from bs4 import BeautifulSoup, SoupStrainer
from couchpotato.core.helpers.variable import tryInt, getIdentifier
from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import re
import time
from urllib import unquote

log = CPLog(__name__)


class BigTower(TorrentProvider, MovieProvider):

    urls = {
        'test': 'http://bigtower.info/',
        'login': 'http://bigtower.info/index.php?page=login',
        'login_check': 'http://bigtower.info/index.php?page=usercp',
        'search': 'http://bigtower.info/index.php?page=torrents&%s',
        'baseurl': 'http://bigtower.info/%s',
        'details': 'http://bigtower.info/index.php?page=torrent-details&id=%s'
    }

    # BigTower movie search categories
    cat_ids = [
        ([92, 19], ['3d']),
        ([91, 18], ['1080p']),
        ([17], ['720p']),
        ([16], ['brrip']),
        ([83], ['2160p']),
        ([15], ['dvdrip']),
        ([89, 90], ['dvdr']),
        ([14], ['scr','r5','tc','ts','cam'])
    ]
    cat_backup_id = 0

    http_time_between_calls = 1  # Seconds
    login_fail_msg = 'Benvenuto Guest'
    only_tables_tags = SoupStrainer('table')


    def buildUrl(self, title, media, cat):
        query = tryUrlencode({
            'search': title,
            'category': cat,
            'options': 0
         })
        return query

    def _searchOnTitle(self, title, movie, quality, results):
        cat = ';'.join(str(x) for x in self.getCatId(quality))

        url = self.urls['search'] % self.buildUrl(title, movie, cat)
        log.debug("Searching for quality: %s (id: %s)" % (quality['label'], cat))

        data = self.getHTMLData(url)

        if data:
            html = BeautifulSoup(data, 'html.parser', parse_only = self.only_tables_tags)

            try:
                result_table = html.findAll('table', {'class': 'lista', 'width': '100%'})[1]
                result_td = result_table.find_all('td', {'class':'lista'})
                if not result_table or len(result_td) == 0:
                    log.info("No torrents found for %s (quality %s) on BigTower" % (title, quality['label']))

                entries = result_table.find_all('tr')
                for result_row in entries:

                    all_cells = result_row.find_all('td', {'class':'lista'})

                    if len(all_cells) == 0: continue

                    torrent_score = 0

                    torrent = all_cells[1].find_all('a')[0]

                    # prefer gold torrents (free leech)
                    if all_cells[1].find('img', {'alt':'Gold 100% Free'}): torrent_score += 1000

                    torrent_name = torrent.getText()
                    torrent_id = re.match('.*id=(.*)$',torrent['href']).group(1)
                    # check the number of columns before assuming the cell position, some user have a different visualization
                    torrent_seeders = tryInt(all_cells[5].getText()) if all_cells[9].getText() != "" else tryInt(all_cells[4].getText())
                    torrent_leechers = tryInt(all_cells[6].getText()) if all_cells[9].getText() != "" else tryInt(all_cells[5].getText())
                    torrent_size = self.parseSize(all_cells[9].getText()) if all_cells[9].getText() != "" else self.parseSize(all_cells[8].getText())
                    torrent_url = self.urls['baseurl'] % 'download.php?id=%s' % torrent_id
                    torrent_detail_url = self.urls['details'] % torrent_id

                    result = {
                        'id': torrent_id,
                        'name': torrent_name,
                        'size': torrent_size,
                        'seeders': torrent_seeders,
                        'leechers': torrent_leechers,
                        'url': torrent_url,
                        'detail_url': torrent_detail_url,
                        'score': torrent_score
                    }

                    log.debug("New result %s", result)
                    results.append(result)

            except:
                    log.error('Failed getting results from %s: %s', (self.getName(), traceback.format_exc()))

    def getLoginParams(self):
        return {
            'uid': self.conf('username'),
            'pwd': self.conf('password')
        }

    def loginSuccess(self, output):
        return 'logout.php' in output.lower()

    loginCheckSuccess = loginSuccess
