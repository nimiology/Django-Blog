from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.utils import CreateRetrieveUpdateDestroyAPIView
from projects.api.serializers import ProjectSerializer
from projects.models import Project


class ProjectAPI(CreateRetrieveUpdateDestroyAPIView):
    queryset = Project.objects.filter(publish=True)
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectsAPI(ListAPIView):
    queryset = Project.objects.filter(publish=True)
    serializer_class = ProjectSerializer
    filterset_fields = {
        "title": ['exact', 'contains'],
        "slug": ['exact', 'contains'],
        "github": ['exact', 'contains'],
        "text": ['exact', 'contains'],
        "publishDate": ['exact', 'contains'],
        "created": ['exact', 'contains'],
        "updated": ['exact', 'contains'],
    }
    ordering_fields = '__all__'
