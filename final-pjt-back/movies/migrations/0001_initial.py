# Generated by Django 3.2.12 on 2022-05-24 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField(default=False)),
                ('backdrop_path', models.CharField(max_length=200)),
                ('original_language', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=400)),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('video', models.BooleanField(default=False)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre_ids', models.ManyToManyField(related_name='movie_ids', to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_id', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
