from django.urls import path
from .views import Home, SocialMedia, NotFound

app_name = 'StaticPages'
urlpatterns = [
    path("", Home, name="home"),
    path("about", SocialMedia, name="about"),
    path('404', NotFound, name="notFound")
]
