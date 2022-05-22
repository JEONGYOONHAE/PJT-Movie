from django.contrib import admin
from .models import User
from articles.models import Article, Comment
from movies.models import Movie
# Register your models here.

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Article)
admin.site.register(Comment)