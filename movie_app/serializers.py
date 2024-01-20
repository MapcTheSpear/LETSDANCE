from rest_framework import serializers
from .models import (Director, Movie, Review)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = 'id'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = 'id'.split()
