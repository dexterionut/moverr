from guessit import guessit

from builders.abstract_path_builder import AbstractPathBuilder
from models.torrent import Torrent


class TvShowPathBuilder(AbstractPathBuilder):
    @staticmethod
    def isFullSeason(guessedDict):
        if 'season' in guessedDict and 'episode' in guessedDict:
            return False

        return True

    @staticmethod
    def buildNewPath(torrent: Torrent, basePath='/') -> dict:
        guessedDict = guessit(torrent.name)
        torrentClientPath = '/'.join([basePath, guessedDict['title']])

        if not TvShowPathBuilder.isFullSeason(guessedDict):
            season = 'Season ' + str(guessedDict['season'])
            torrentClientPath = '/'.join([torrentClientPath, season])

        return TvShowPathBuilder._buildNewPathDict(torrent, torrentClientPath)
#
