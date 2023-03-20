from rest_framework import serializers
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id name rating duration'.split()
        # exclude = 'updated created'.split()
