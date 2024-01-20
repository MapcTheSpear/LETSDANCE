from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(
        'movie_app.Director',
        on_delete=models.PROTECT,
        verbose_name='Director',
        related_name='movie'
    )


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(
        'movie_app.Movie',
        on_delete=models.CASCADE,
        verbose_name='Movie',
        related_name='review'
    )
# Create your models here.
