from django.urls import path
from .views import Home, SocialMedia, Error404

app_name = 'StaticPages'
urlpatterns = [
    path("", Home, name="home"),
    path("about", SocialMedia, name="about"),
    path('404', Error404, name="notFound")
]
