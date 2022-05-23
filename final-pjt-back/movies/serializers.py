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
    # genre_ids를 바탕으로 랜덤으로 영화 하나 추천
    class Meta:
        model = Movie
        fields = ('pk', 'user', 'original_title', 'overview', 'genre_ids', 'poster_path', 'like_users')


class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)       # user
    # comment_count = serializers.IntegerField()  # 댓글 수
    # article_count = serializers.IntegerField()  # 게시글 수 

    class Meta:
        model = Movie
        fields = ('pk', 'user', 'original_title', 'poster_path', 'overview')