import os
import shutil
import logging
from typing import List

import qbittorrentapi

from clients.abstract_torrent_client import TorrentClient
from models.file import File
from models.torrent import Torrent


class QBitTorrentClient(TorrentClient):

    def __init__(self, host='localhost:8080', username='admin', password='adminadmin'):
        super().__init__()

        self._client = qbittorrentapi.Client(host=host, username=username, password=password)

    def getTorrentsByCategory(self, category: str) -> List[Torrent]:
        torrents = []
        for torrent in self._client.torrents_info(category=category, sort='added_on', reverse=True):
            # only get complete torrents
            if not torrent.state_enum.is_complete:
                continue

            files = []
            for file in torrent.files:
                files.append(File(file['name']))

            newTorrent = Torrent(torrent['hash'], torrent['name'], torrent['category'], torrent['save_path'][:-1],
                                 files)
            torrents.append(newTorrent)

        return torrents

    def changeLocation(self, torrent: Torrent, oldLocation: str, newLocation: dict):
        logging.info(
            'Changing location of torrent {} from {} to {}'.format(
                torrent.name, torrent.currentPath, newLocation['torrentClientPath']
            )
        )

        self._client.torrents.pause(torrent.id)

        os.makedirs(os.path.dirname(newLocation['torrentClientPath']), exist_ok=True)
        shutil.move(oldLocation, newLocation['shutilPath'])

        self._client.torrents_set_location(newLocation['torrentClientPath'], torrent.id)
        self._client.torrents.resume(torrent.id)
