import logging

from clients.qbittorrent_client import QBitTorrentClient
from constants import Constants

QBITTORRENT_CLIENT = 'qbittorrent'


class TorrentClientFactory:

    @staticmethod
    def create(constants: Constants, client: str):
        if client == QBITTORRENT_CLIENT:
            return QBitTorrentClient(
                host=constants.TORRENT_CLIENT_HOST,
                username=constants.TORRENT_CLIENT_USERNAME,
                password=constants.TORRENT_CLIENT_PASSWORD
            )
        else:
            logging.info('Unknown torrent client {}'.format(client))
            return False
