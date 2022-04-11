import uuid
from dataclasses import dataclass


@dataclass
class MusicEntry:
    title: str
    contributors: list
    iswc: str = None
    id: uuid.uuid4 = None
