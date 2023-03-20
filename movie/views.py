from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie.serializers import MovieSerializer
from movie.models import Movie
from rest_framework import status


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        'text': 'Hello World',
        'integer': 1000,
        'float': 5.55,
        'bool': False,
        'list': [12, 3, 4243],
        'dict': {'key': 'value'}

    }
    return Response(data=dict_)
