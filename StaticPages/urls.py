from django.urls import path
from .views import Home,SocialMedia

app_name = 'StaticPages'
urlpatterns = [
    path("",Home, name="main"),
    path("about", SocialMedia, name="About"),
]