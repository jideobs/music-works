from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from aggregator.models import Contributor, Music


class MusicViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('music_v1:music')

    def test_get_music__not_found(self):
        response = self.client.get(f'{self.url}?iswc=NOTFOUND')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_music__found(self):
        # Given
        music = Music.objects.create(
            title='The title',
            title_slug='The title'.lower(),
            iswc='THEISWC',
            iswc_slug='THEISWC'.lower(),
        )
        contributor = Contributor.objects.create(name='John Doe')
        music.contributors.add(contributor)

        response = self.client.get(f'{self.url}?iswc=THEISWC')

        print(response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected_resposne_data = {
            'title': music.title,
            'iswc': music.iswc,
            'contributors': [contributor.name],
        }
        self.assertEqual(expected_resposne_data, response.data)
