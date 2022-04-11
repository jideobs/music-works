from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from aggregator.models import Music
from aggregator.serializers import MusicSerializer


class MusicView(APIView):
    def get(self, request):
        iswc = request.query_params.get('iswc')
        try:
            music = Music.objects.get(iswc_slug=iswc.lower())
            serializer = MusicSerializer(music)
            return Response(serializer.data)
        except Music.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)
