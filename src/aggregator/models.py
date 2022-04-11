import uuid
from typing import List

from django.db import models

from reconciler.models import MusicEntry


class Contributor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)


class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    title_slug = models.CharField(max_length=200, blank=False, null=False)
    iswc = models.CharField(max_length=11, null=True, blank=False, unique=True)
    iswc_slug = models.CharField(max_length=11, null=True, blank=False)
    contributors = models.ManyToManyField(Contributor)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
