from typing import List

from models.torrent import Torrent


class TorrentClient:
    def getCompletedTorrentsByCategory(self, category: str) -> List[Torrent]:
        raise NotImplementedError()

    def changeLocation(self, torrentId: str, newLocation: str):
        raise NotImplementedError()
