from builders.abstract_path_builder import AbstractPathBuilder
from models.torrent import Torrent


class MoviePathBuilder(AbstractPathBuilder):
    @staticmethod
    def isFullSeason(guessedDict):
        if 'season' in guessedDict and 'episode' in guessedDict:
            return False

        return True

    @staticmethod
    def buildNewPath(torrent: Torrent, basePath='/') -> dict:
        torrentClientPath = basePath

        return MoviePathBuilder._buildNewPathDict(torrent, torrentClientPath)
