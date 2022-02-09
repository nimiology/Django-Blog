from django.urls import path, include
from .views import Projects, Projectgetter

app_name = 'projects'
urlpatterns = [
    path('api/', include('projects.api.urls')),
    path('', Projects, name='projects'),
    path("page/<int:page>/", Projects, name='projects'),
    path("<slug>/", Projectgetter, name='project'),
]
