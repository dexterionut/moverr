from builders.abstract_path_builder import AbstractPathBuilder
from models.torrent import Torrent


class MoviePathBuilder(AbstractPathBuilder):
    @staticmethod
    def isFullSeason(guessedDict):
        if 'season' in guessedDict and 'episode' in guessedDict:
            return False

        return True

    @staticmethod
    def build(torrent: Torrent, basePath='/') -> str:
        path = basePath

        if not MoviePathBuilder.hasSubfolder(torrent.files):
            torrentSubfolder = '.'.join(torrent.name.split('.')[0:-1])
            path = '/'.join([path, torrentSubfolder])

        return path.replace(' ', '.') + '/'
