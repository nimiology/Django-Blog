from rest_framework.generics import ListAPIView

from blog.api.serializers import TagSerializer, CategorySerializer, ArticleSerializer, SectionSerializer
from blog.models import Tag, Category, Article, Section
from blog.utils import CreateRetrieveUpdateDestroyAPIView
from projects.api.permissions import ReadOnly
from staticpages.api.permissions import IsSuperUser


class TagAPI(CreateRetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [ReadOnly | IsSuperUser]


class TagsAPI(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filterset_fields = {
        "title": ['exact', 'contains'],
        "slug": ['exact', 'contains'],
        "status": ['exact'],
    }
    ordering_fields = '__all__'


class CategoryAPI(TagAPI):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoriesAPI(TagsAPI):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleAPI(TagAPI):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'


class ArticlesAPI(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filterset_fields = {
        "title": ['exact', 'contains'],
        "slug": ['exact', 'contains'],
        'categories': ['exact', ],
        'tags': ['exact', ],
        'writer': ['exact', 'contains'],
        'publishDate': ['exact', 'contains'],
        'created': ['exact', 'contains'],
        'published': ['exact'],
    }
    ordering_fields = '__all__'


class SectionAPI(TagAPI):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionsAPI(ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    filterset_fields = {
        'article': ['exact'],
        'title': ['exact', 'contains'],
        'youtube': ['exact', 'contains'],
        'text': ['exact', 'contains'],
        'code': ['exact', 'contains'],
        'position': ['exact', 'contains'],

    }
    ordering_fields = '__all__'
