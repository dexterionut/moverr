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
    def build(torrent: Torrent, basePath='/') -> str:
        guessedDict = guessit(torrent.name)
        path = '/'.join([basePath, guessedDict['title']])

        if not TvShowPathBuilder.isFullSeason(guessedDict):
            season = 'Season ' + str(guessedDict['season'])
            path = '/'.join([path, season])

        if not TvShowPathBuilder.hasSubfolder(torrent.files):
            torrentSubfolder = '.'.join(torrent.name.split('.')[0:-1])
            path = '/'.join([path, torrentSubfolder])

        return path.replace(' ', '.') + '/'
