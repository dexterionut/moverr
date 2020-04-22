from typing import List

import qbittorrentapi

from clients.abstract_torrent_client import TorrentClient
from models.file import File
from models.torrent import Torrent


class QBitTorrentClient(TorrentClient):

    def __init__(self, host='localhost:8080', username='admin', password='adminadmin'):
        super().__init__()

        self._client = qbittorrentapi.Client(host=host, username=username, password=password)

    def getCompletedTorrentsByCategory(self, category: str) -> List[Torrent]:
        torrents = []
        for torrent in self._client.torrents_info(category=category, sort='added_on', reverse=True):
            # skip already moving files
            if torrent['state'] == 'moving':
                continue

            files = []
            for file in torrent.files:
                files.append(File(file['name']))

            newTorrent = Torrent(torrent['hash'], torrent['name'], torrent['category'], torrent['save_path'], files)
            torrents.append(newTorrent)

        return torrents

    def changeLocation(self, torrentId: str, newLocation: str):
        self._client.torrents.pause(torrentId)
        self._client.torrents_set_location(newLocation, torrentId)
        self._client.torrents.resume(torrentId)

    def isMoving(self) -> bool:
        movingTorrents = [torrent for torrent in self._client.torrents_info() if torrent['state'] == 'moving']
        return len(movingTorrents) > 0
