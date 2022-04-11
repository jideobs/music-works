from django.urls import path

from aggregator.views import MusicView


urlpatterns = [
    path('/', MusicView.as_view(), name='music')
]
