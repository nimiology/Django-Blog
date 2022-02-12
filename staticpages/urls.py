from django.urls import path, include
from .views import Home, About, Error404

app_name = 'staticpages'
urlpatterns = [
    path('api/', include('staticpages.api.urls')),

    path("", Home, name="home"),
    path("about/", About, name="about"),
    path('404/', Error404, name="notFound")
]
