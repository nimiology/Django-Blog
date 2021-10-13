from django.urls import path
from .views import Projects, Projectgetter

app_name = 'Projects'
urlpatterns = [
    path('', Projects, name='projects'),
    path("page/<int:page>", Projects, name='projects'),
    path("<slug>", Projectgetter, name='project'),
]
