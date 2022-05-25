from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .models import Movie, Review
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer

# 영화 home
@api_view(['GET'])
@permission_classes([AllowAny])
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


@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        reviews = movie.review_id.all()
        serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()

