from django.urls import path

from blog.api.views import TagAPI, TagsAPI, CategoryAPI, CategoriesAPI, ArticlesAPI, ArticleAPI, SectionAPI, SectionsAPI

app_name = 'api'
urlpatterns = [
    path('tag/', TagAPI.as_view(), name='create_tag'),
    path('tag/<int:pk>', TagAPI.as_view(), name='tag'),
    path('tag/all/', TagsAPI.as_view(), name='tags'),

    path('category/', CategoryAPI.as_view(), name='create_category'),
    path('category/<int:pk>/', CategoryAPI.as_view(), name='category'),
    path('category/all/', CategoriesAPI.as_view(), name='categories'),

    path('article/', ArticleAPI.as_view(), name='create_article'),
    path('article/<slug>', ArticleAPI.as_view(), name='article'),
    path('article/all/', ArticlesAPI.as_view(), name='articles'),

    path('section/', SectionAPI.as_view(), name='create_section'),
    path('section/<int:pk>', SectionAPI.as_view(), name='section'),
    path('section/all/', SectionsAPI.as_view(), name='sections'),
]
