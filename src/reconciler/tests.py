from unittest import TestCase
import uuid
from mockito import when, mock, verify, ANY

from reconciler.models import MusicEntry

from musicworks.settings.base import BASE_DIR
from .reconliator import Reconciliator
from aggregator.repository import MusicRepository


class ReconciliatorTests(TestCase):
    csv_test_data_file = f'{BASE_DIR}/../reconciler/test_metadata.csv'

    def setUp(self):
        self.music_repository = mock(MusicRepository)
        self.reconciliator = Reconciliator(self.music_repository)
        self.get_music_entry_response = MusicEntry(
            id=uuid.uuid4(),
            title='The title',
            contributors=['John Doe', 'Sarah Jane'],
            iswc='T9204649558',
        )

    def test_music_entry__insert(self):
        when(self.music_repository).get_music(...).thenReturn(None)
        when(self.music_repository).insert_music(...).thenReturn(None)

        self.reconciliator.read_csv(self.csv_test_data_file)

        verify(self.music_repository, times=6).get_music(...)
        verify(self.music_repository, times=6).insert_music(...)

    def test_music_entry__update(self):
        when(self.music_repository).get_music(...).thenReturn(self.get_music_entry_response)
        when(self.music_repository).update_music(...).thenReturn(None)

        self.reconciliator.read_csv(self.csv_test_data_file)

        verify(self.music_repository, times=6).get_music(...)
        verify(self.music_repository, times=6).update_music(...)
