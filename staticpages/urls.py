from django.urls import path, include
from .views import Home, contact, error404, faq, process, about

app_name = 'staticpages'
urlpatterns = [
    path('api/', include('staticpages.api.urls')),

    path("", Home, name="home"),
    path("contact/", contact, name="contact"),
    path('404/', error404, name="notFound"),
    path('faq/', faq, name="faq"),
    path('process/', process, name="process"),
    path('about/', about, name="about"),
]
