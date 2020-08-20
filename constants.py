import os


class Constants:
    TORRENT_CLIENT_NAME: str
    TORRENT_CLIENT_HOST: str
    TORRENT_CLIENT_USERNAME: str
    TORRENT_CLIENT_PASSWORD: str

    DOWNLOADS_BASE_FOLDER: str

    TV_SHOWS_BASE_FOLDER: str
    TV_SHOWS_CATEGORY: str

    MOVIES_BASE_FOLDER: str
    MOVIES_CATEGORY: str

    def __init__(self) -> None:
        self.TORRENT_CLIENT_NAME = os.getenv('TORRENT_CLIENT_NAME')
        self.TORRENT_CLIENT_HOST = os.getenv('TORRENT_CLIENT_HOST')
        self.TORRENT_CLIENT_USERNAME = os.getenv('TORRENT_CLIENT_USERNAME')
        self.TORRENT_CLIENT_PASSWORD = os.getenv('TORRENT_CLIENT_PASSWORD')

        self.DOWNLOADS_BASE_FOLDER = os.getenv('DOWNLOADS_BASE_FOLDER')

        self.TV_SHOWS_BASE_FOLDER = os.getenv('TV_SHOWS_BASE_FOLDER')
        self.TV_SHOWS_CATEGORY = os.getenv('TV_SHOWS_CATEGORY')

        self.MOVIES_BASE_FOLDER = os.getenv('MOVIES_BASE_FOLDER')
        self.MOVIES_CATEGORY = os.getenv('MOVIES_CATEGORY')
