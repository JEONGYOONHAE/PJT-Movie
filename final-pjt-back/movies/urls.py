from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_recommend),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete)
]