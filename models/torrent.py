from typing import List

from models.file import File


class Torrent:
    id: str
    name: str
    category: str
    currentPath: str
    files: List[File]

    def __init__(self, torrentId: str, name: str, category: str, currentPath: str, files: List[File]):
        self.id = torrentId
        self.name = name
        self.category = category
        self.currentPath = currentPath
        self.files = files
