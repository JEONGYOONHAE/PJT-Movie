from django.shortcuts import render
from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models import Count
# 영화 home
@api_view(['GET'])
def movie_list(request):
  # 최신영화, 평점 좋은 순으로 나열하는 것은 vue에서 하는지..? 
  movies = Movie.objects.all()
  serializer = MovieListSerializer(movies, many=True)

  return Response(serializer.data)

# 영화 추천
@api_view(['GET'])
def movie_recommend(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  serializer = MovieSerializer(movie)
  # genre_ids를 기준으로 moive를 골라야 하는지..?
  return Response(serializer.data)

# 영화 좋아요
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)