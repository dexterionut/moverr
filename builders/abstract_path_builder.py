from typing import List

from models.file import File
from models.torrent import Torrent


class AbstractPathBuilder:
    @staticmethod
    def hasSubfolder(torrentFiles: List[File]) -> bool:
        firstFileNameSplit = torrentFiles[0].name.split('/')
        if len(firstFileNameSplit) == 1:
            return False

        for torrentFile in torrentFiles[1:]:
            splitName = torrentFile.name.split('/')

            if len(splitName) == 1:
                return False

            if splitName[0] != firstFileNameSplit[0]:
                return False

        return True

    @staticmethod
    def build(torrent: Torrent, basePath='/') -> str:
        raise NotImplementedError()
