import logging
import os
import sys
from time import sleep

import schedule
from dotenv import load_dotenv

from builders.movie_path_builder import MoviePathBuilder
from builders.path_builder_factory import PathBuilderFactory
from builders.tv_show_path_builder import TvShowPathBuilder
from clients.qbittorrent_client import QBitTorrentClient
from clients.torrent_client_factory import TorrentClientFactory
from constants import Constants

load_dotenv()


def configLogging():
    import time
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.basicConfig(format='{}: GMT: %(asctime)s %(levelname)s %(message)s'.format(os.path.split(sys.argv[0])[1]))
    logging.Formatter.converter = time.gmtime


def main():
    configLogging()
    constants = Constants()

    logging.info('Started moving files...')

    client = TorrentClientFactory.create(constants, constants.TORRENT_CLIENT_NAME)
    if not client:
        return

    torrents = client.getTorrentsByCategory(constants.TV_SHOWS_CATEGORY) + \
               client.getTorrentsByCategory(constants.MOVIES_CATEGORY)

    # move torrents
    hasMoved = False
    for torrent in torrents:
        oldPath = PathBuilderFactory.createOldPathString(torrent)
        newPath = PathBuilderFactory.createNewPathDict(constants, torrent)
        if not newPath:
            continue

        if torrent.currentPath != newPath['torrentClientPath']:
            hasMoved = True
            client.changeLocation(torrent, oldPath, newPath)

    if hasMoved:
        logging.info('Moving files done.')
    else:
        logging.info('Nothing to move.')


if __name__ == '__main__':
    schedule.every(1).minutes.do(main)

    while True:
        schedule.run_pending()
        sleep(1)
