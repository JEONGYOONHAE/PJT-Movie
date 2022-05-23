from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie


User = get_user_model()

# 영화 추천 받을 경우 detail 
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)       # user
    like_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ('pk', 'user', 'genre_ids',  'overview', 'poster_path', 'title', 'release_date', 'vote_average', 'vote_count', 'like_users')