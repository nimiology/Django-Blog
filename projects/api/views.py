from blog.utils import CreateRetrieveUpdateDestroyAPIView, MyListAPIView
from projects.api.permissions import ReadOnly
from projects.api.serializers import ProjectSerializer
from projects.models import Project
from staticpages.api.permissions import IsSuperUser


class ProjectAPI(CreateRetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ReadOnly | IsSuperUser]


class ProjectsAPI(MyListAPIView):
    queryset = Project.objects.all()
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
