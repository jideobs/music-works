from rest_framework import serializers

from aggregator.models import Contributor, Music


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['name',]


class MusicSerializer(serializers.ModelSerializer):
    contributors = ContributorsSerializer(many=True)

    class Meta:
        model = Music
        fields = ['title', 'iswc', 'contributors']
    
    @property
    def data(self):
        original_data = super().data
        contributors = [contributor['name'] for contributor in original_data['contributors']]
        return {
            'title': original_data['title'],
            'iswc': original_data['iswc'],
            'contributors': contributors,
        }
