from django.urls import path

from projects.api.views import ProjectsAPI, ProjectAPI

app_name = 'project_api'

urlpatterns = [
    path('', ProjectsAPI.as_view(), name='projects'),

    path('project/', ProjectAPI.as_view(), name='create_project'),
    path('project/<int:pk>/', ProjectAPI.as_view(), name='project'),
]