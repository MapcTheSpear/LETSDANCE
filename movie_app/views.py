from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (Director, Movie, Review)
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer)
from rest_framework import status


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'ERROR: NOTFOUND!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def directors_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'directors_id': director.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT',' DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'ERROR': 'MOVIENOTFOUND!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.year_of_release = request.data.get('year_of_release')
        movie.save()
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.prefetch_related('reviews').all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        year_of_release = request.data.get('year_of_release')
        movie = Movie.objects.create(title=title, description=description,
                                     duration=duration, director_id=director_id,
                                     year_of_release=year_of_release)
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'ERROR': 'NO SUCH REVIEW!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def reviews_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)

# Create your views here.
