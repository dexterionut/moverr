from typing import List

from models.torrent import Torrent


class TorrentClient:
    def getTorrentsByCategory(self, category: str) -> List[Torrent]:
        raise NotImplementedError()

    def changeLocation(self, torrent: Torrent, oldLocation: str, newLocation: dict):
        raise NotImplementedError()
