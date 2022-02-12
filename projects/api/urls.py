from django.urls import path

from projects.api.views import ProjectsAPI, ProjectAPI

app_name = 'api'

urlpatterns = [
    path('', ProjectsAPI.as_view(), name='projects'),

    path('create/', ProjectAPI.as_view(), name='create_project'),
    path('<int:pk>/', ProjectAPI.as_view(), name='project'),
]