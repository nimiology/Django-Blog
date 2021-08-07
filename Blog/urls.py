from django.urls import path
from .views import articles,Blog,Categorygetter
app_name = 'Blog'
urlpatterns = [
    path("", articles, name="blog"),
    path("page/<int:page>", articles, name="blog"),
    path("<slug:slug>", Blog, name="article"),
    path("category/<slug:slug>", Categorygetter, name='category'),
    path("category/<slug:slug>/page/<int:page>", Categorygetter, name='category'),
]
