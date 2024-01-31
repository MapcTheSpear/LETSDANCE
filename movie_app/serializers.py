from rest_framework import serializers
from .models import (Director, Movie, Review)
from django.db.models import Avg
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie_name stars_total'.split()


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    review = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director_name year_of_release review reviews avg_rating'.split()
        depth = 1

    def get_review(self, movie):
        return [rev.text for rev in movie.reviews.all()]


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=256)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=150)
    description = serializers.CharField(required=False)
    duration = serializers.FloatField()
    director_id = serializers.IntegerField()
    year_of_release = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('No Such Director!!!')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('No Such Movie!!')
        return movie_id
