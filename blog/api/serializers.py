from rest_framework.serializers import ModelSerializer

from blog.models import Tag, Category, Article, Section


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
