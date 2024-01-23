from rest_framework import serializers
from .models import (Director, Movie, Review)
from django.db.models import Avg


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    review = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director_name year_of_release review reviews avg_rating'.split()
        depth = 1

    def get_review(self, movie):
        return [rev.text for rev in movie.reviews.all()]


