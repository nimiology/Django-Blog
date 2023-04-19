from django.urls import path, include
from .views import Home, About, error404, faq, process

app_name = 'staticpages'
urlpatterns = [
    path('api/', include('staticpages.api.urls')),

    path("", Home, name="home"),
    path("about/", About, name="about"),
    path('404/', error404, name="notFound"),
    path('faq/', faq, name="faq"),
    path('process/', process, name="process"),
]
