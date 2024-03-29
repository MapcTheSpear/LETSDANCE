# Generated by Django 4.2.9 on 2024-01-23 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie', verbose_name='Movie'),
        ),
    ]
