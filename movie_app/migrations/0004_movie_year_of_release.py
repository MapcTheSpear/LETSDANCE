# Generated by Django 4.2.9 on 2024-01-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year_of_release',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
