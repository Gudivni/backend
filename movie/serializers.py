from rest_framework import serializers
from movie.models import Movie, Director, Genre, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name age'.split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genres = GenreSerializer(many=True)
    director_name = serializers.SerializerMethodField()
    filtered_review_list = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'filtered_review_list director director_name genres genres_list id name rating duration'.split()

    def get_director_name(self, movie):
        try:
            return movie.director.name
        except:
            return None
