from django.urls import path
from .views import Blog, Post, CategoryView, TagView

app_name = 'blog'
urlpatterns = [
    path("", Blog, name="blog"),
    path("page/<int:page>/", Blog, name="blog"),
    path("<slug:slug>/", Post, name="article"),
    path("category/<slug:slug>/", CategoryView, name='category'),
    path("category/<slug:slug>/page/<int:page>/", CategoryView, name='category'),
    path("tag/<slug:slug>/", TagView, name='tag'),
    path("tag/<slug:slug>/page/<int:page>/", TagView, name='tag'),
]
