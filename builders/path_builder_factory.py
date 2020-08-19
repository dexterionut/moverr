import logging

from builders.movie_path_builder import MoviePathBuilder
from builders.tv_show_path_builder import TvShowPathBuilder
from constants import Constants
from models.torrent import Torrent


class PathBuilderFactory:

    @staticmethod
    def create(constants: Constants, torrent: Torrent):
        if torrent.category == constants.TV_SHOWS_CATEGORY:
            return TvShowPathBuilder.build(torrent, constants.TV_SHOWS_BASE_FOLDER)
        elif torrent.category == constants.MOVIES_CATEGORY:
            return MoviePathBuilder.build(torrent, constants.MOVIES_BASE_FOLDER)
        else:
            logging.info('Unknown category of torrent {} with name {}. Continuing...'.format(torrent.id, torrent.name))
            return False
