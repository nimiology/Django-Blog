from django.urls import path
from .views import AllDiaries,ADiary
app_name = 'Diary'
urlpatterns = [
    path('<slug:Slug>',ADiary,name='Diary'),
    path('',AllDiaries,name='Diaries')

]