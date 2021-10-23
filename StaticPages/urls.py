from django.urls import path
from .views import Home, About, Error404

app_name = 'StaticPages'
urlpatterns = [
    path("", Home, name="home"),
    path("about/", About, name="about"),
    path('404/', Error404, name="notFound")
]
