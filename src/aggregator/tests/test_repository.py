from django.test import TestCase
import pytest

from aggregator.repository import MusicRepository
from reconciler.models import MusicEntry


class MusicRepositoryTestCases(TestCase):
    def setUp(self):
        self.music_repository = MusicRepository()
        self.music_entry = MusicEntry(
            title='The title',
            contributors=['John Doe', 'Sarah Jane'],
            iswc='T9204649558',
        )
        self.sample_music_entry = MusicEntry(
            title='The title 2',
            contributors=['John Doe', 'Sarah Jane'],
        )
        self.music_entry_without_incomplete_details = MusicEntry(
            title='The title 3',
            contributors=['John Doe'],
        )

    def test_insert_music(self):
        self.music_repository.insert_music(self.music_entry)
        music_entry_from_db = self.music_repository.get_music(self.music_entry)
        
        self.assertIsNotNone(music_entry_from_db)
        self.assertIsNotNone(music_entry_from_db.id)
        self.assertEqual(self.music_entry.title, music_entry_from_db.title)
        self.assertEqual(sorted(self.music_entry.contributors), sorted(music_entry_from_db.contributors))
        self.assertEqual(self.music_entry.iswc, music_entry_from_db.iswc)

    def test_get_music__music_not_existing_in_db(self):
        self.assertIsNone(self.music_repository.get_music(self.music_entry))

    def test_get_music__music_available_with_iswc(self):
        self.music_repository.insert_music(self.music_entry)

        music_entry = self.music_repository.get_music(self.music_entry)

        self.assertIsNotNone(music_entry)
        self.assertIsNotNone(music_entry.id)

    def test_get_music__music_available_with_title(self):
        self.music_repository.insert_music(self.sample_music_entry)

        request_music_entry = MusicEntry(
            title='The title 2',
            contributors=['John Doe'],
            iswc='',
        )
        music_entry_from_db = self.music_repository.get_music(request_music_entry)

        self.assertIsNotNone(music_entry_from_db)
        self.assertIsNotNone(music_entry_from_db.id)
        self.assertEqual(self.sample_music_entry.title, music_entry_from_db.title)
        self.assertEqual(sorted(self.sample_music_entry.contributors), sorted(music_entry_from_db.contributors))

    def test_update_music(self):
        music_id = self.music_repository.insert_music(self.music_entry_without_incomplete_details)

        self.music_repository.update_music(music_id, 'NEWISWC', ['Sarah Jane'])

        music_entry = self.music_repository.get_music(self.music_entry_without_incomplete_details)
        
        self.assertIsNotNone(music_entry)
        self.assertEqual(sorted(music_entry.contributors), sorted(['Sarah Jane', 'John Doe']))
        self.assertEqual(music_entry.iswc, 'NEWISWC')
