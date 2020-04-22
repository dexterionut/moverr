import logging
import os
import sys
from time import sleep

from dotenv import load_dotenv

from builders.movie_path_builder import MoviePathBuilder
from builders.tv_show_path_builder import TvShowPathBuilder
from clients.qbittorrent_client import QBitTorrentClient

load_dotenv()


def configLogging():
    import time
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.basicConfig(format='{}: GMT: %(asctime)s %(levelname)s %(message)s'.format(os.path.split(sys.argv[0])[1]))
    logging.Formatter.converter = time.gmtime


def main():
    configLogging()

    TORRENT_CLIENT_HOST = os.getenv('TORRENT_CLIENT_HOST')
    TORRENT_CLIENT_USERNAME = os.getenv('TORRENT_CLIENT_USERNAME')
    TORRENT_CLIENT_PASSWORD = os.getenv('TORRENT_CLIENT_PASSWORD')

    TV_SHOWS_BASE_FOLDER = os.getenv('TV_SHOWS_BASE_FOLDER')
    TV_SHOWS_CATEGORY = os.getenv('TV_SHOWS_CATEGORY')

    MOVIES_BASE_FOLDER = os.getenv('MOVIES_BASE_FOLDER')
    MOVIES_CATEGORY = os.getenv('MOVIES_CATEGORY')

    logging.info('Started moving files...')

    client = QBitTorrentClient(
        host=TORRENT_CLIENT_HOST,
        username=TORRENT_CLIENT_USERNAME,
        password=TORRENT_CLIENT_PASSWORD
    )

    torrents = client.getTorrentsByCategory(TV_SHOWS_CATEGORY) + \
               client.getTorrentsByCategory(MOVIES_CATEGORY)

    if len(torrents) == 0:
        logging.info('Nothing to move.')
        return

    # move torrents
    for torrent in torrents:
        if torrent.category == TV_SHOWS_CATEGORY:
            newPath = TvShowPathBuilder.build(torrent, TV_SHOWS_BASE_FOLDER)
        elif torrent.category == MOVIES_CATEGORY:
            newPath = MoviePathBuilder.build(torrent, MOVIES_BASE_FOLDER)
        else:
            logging.info('Unknown category of torrent {} with name {}. Continuing...'.format(torrent.id, torrent.name))
            continue

        if torrent.currentPath != newPath:
            logging.info(
                'Changing location of torrent {} from {} to {}'.format(torrent.id, torrent.currentPath, newPath)
            )
            client.changeLocation(torrent.id, newPath)


if __name__ == '__main__':
    main()
