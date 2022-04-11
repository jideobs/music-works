import csv

from aggregator.repository import MusicRepository
from .models import MusicEntry


class Reconciliator:
    def __init__(self, music_repository: MusicRepository):
        self._music_repository = music_repository

    def read_csv(self, csv_file):
        with open(csv_file, 'r') as csvfile:
            metadata_reader= csv.DictReader(csvfile)
            # Todo: find a way to reconcile duplicates before going to DB
            # as to reduce the amount of transactions hitting the DB.
            for metadata in metadata_reader:
                music_entry = MusicEntry(
                    title=metadata['title'],
                    contributors=metadata['contributors'].split('|'),
                    iswc=metadata['iswc'])
                existing_music_entry = self._music_repository.get_music(music_entry)
                if existing_music_entry:
                    new_contributors = set(existing_music_entry.contributors).difference(music_entry.contributors)
                    self._music_repository.update_music(
                        existing_music_entry.id, 
                        music_entry.iswc, 
                        new_contributors)
                else:
                    self._music_repository.insert_music(music_entry)
