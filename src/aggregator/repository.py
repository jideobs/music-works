import uuid
from typing import List

from reconciler.models import MusicEntry
from .models import Music, Contributor


class MusicRepository:
    def get_music(self, music_entry: MusicEntry) -> MusicEntry:
        if music_entry.iswc:
            try:
                music = Music.objects.get(iswc_slug=music_entry.iswc.lower())
                return MusicEntry(
                    id=music.id, 
                    title=music.title, 
                    contributors=[contributor.name for contributor in music.contributors.all()], 
                    iswc=music.iswc)
            except Music.DoesNotExist:
                return None
        else:
            music = Music.objects.filter(
                title_slug=music_entry.title.lower(),
                contributors__name__in=music_entry.contributors).first()
            if music:
                return MusicEntry(
                    id=music.id, 
                    title=music.title, 
                    contributors=[contributor.name for contributor in music.contributors.all()], 
                    iswc=music.iswc)

    def _insert_contributors(self, contributors: List[str]) -> List[Contributor]:
        contributors_list = []
        for name in contributors:
            contributor, _ = Contributor.objects.get_or_create(name=name)
            contributors_list.append(contributor)
        return contributors_list

    def insert_music(self, music_entry: MusicEntry) -> uuid.uuid4:
        music = Music(
            title=music_entry.title,
            title_slug=music_entry.title.lower(),
            iswc=music_entry.iswc,
            iswc_slug=(music_entry.iswc.lower() if music_entry.iswc else None))
        music.save()

        contributors = self._insert_contributors(music_entry.contributors)
        music.contributors.add(*contributors)
        music.refresh_from_db()

        return music.id

    def update_music(self, id: uuid.uuid4, iswc: str, contributors: List[str]) -> None:
        music = Music.objects.get(id=id)
        if not music.iswc_slug:
            music.iswc = iswc
            music.iswc_slug = iswc.lower()
            music.save()
        
        contributors = self._insert_contributors(contributors)
        music.contributors.add(*contributors)
