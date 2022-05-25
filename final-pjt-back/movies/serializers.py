from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie, Genre, Review


User = get_user_model()
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['pk','user','movie_id','score',]
        read_only_fields = ('movie_id', )

# 영화 추천 받을 경우 detail 
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    class GenreCustomSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name')
    # class MovieReviewSerializer(serializers.ModelSerializer):
    #     class UserSerializer(serializers.ModelSerializer):
    #         class Meta:
    #             model = User
    #             fields = ('pk', 'username')

    #     user = UserSerializer(read_only=True)

    #     class Meta:
    #         model = Review
    #         fields = '__all__'
    #         read_only_fields = ('movie_id', )
            
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    genre_ids = GenreCustomSerializer(read_only=True, many=True)
    review_id = ReviewSerializer(read_only=True,many=True)
    # review_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    class GenreCustomSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name')

    user = UserSerializer(read_only=True)       # user
    like_users = UserSerializer(read_only=True, many=True)
    genre_ids = GenreCustomSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'user', 'backdrop_path', 'genre_ids',  'overview', 'poster_path', 'title', 'release_date', 'vote_average', 'vote_count', 'like_users')

