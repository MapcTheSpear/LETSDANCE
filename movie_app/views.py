from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (Director, Movie, Review)
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer)
from rest_framework import status


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'ERROR: NOTFOUND!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def directors_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'ERROR': 'MOVIENOTFOUND!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def movie_api_view(request):
    movies = Movie.objects\
        .prefetch_related('reviews').all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'ERROR': 'NO SUCH REVIEW!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view
def reviews_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews).data
    return Response(data=data)

# Create your views here.
