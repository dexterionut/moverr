from typing import List

from models.file import File
from models.torrent import Torrent


class AbstractPathBuilder:
    @staticmethod
    def getSubfolder(torrentFiles: List[File]):
        firstFileNameSplit = torrentFiles[0].name.split('/')
        if len(firstFileNameSplit) == 1:
            return False

        for torrentFile in torrentFiles[1:]:
            splitName = torrentFile.name.split('/')

            if len(splitName) == 1:
                return False

            if splitName[0] != firstFileNameSplit[0]:
                return False

        return firstFileNameSplit[0]

    @staticmethod
    def buildOldPath(torrent: Torrent):
        subfolder = AbstractPathBuilder.getSubfolder(torrent.files)

        if subfolder:
            return '/'.join([torrent.currentPath, subfolder])

        return '/'.join([torrent.currentPath, torrent.files[0].name])

    @staticmethod
    def _buildNewPathDict(torrent, torrentClientPath):
        torrentSubfolder = AbstractPathBuilder.getSubfolder(torrent.files)
        if not torrentSubfolder:
            newTorrentSubfolder = '.'.join(torrent.name.split('.')[0:-1])
            torrentClientPath = '/'.join([torrentClientPath, newTorrentSubfolder])
            shutilPath = torrentClientPath + '/' + torrent.files[0].name
        else:
            shutilPath = torrentClientPath
        return {
            'shutilPath': shutilPath.replace(' ', '.'),
            'torrentClientPath': torrentClientPath.replace(' ', '.')
        }

    @staticmethod
    def buildNewPath(torrent: Torrent, basePath='/') -> dict:
        raise NotImplementedError()
