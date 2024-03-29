"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.sitemaps import ArticleSitemap, CategorySitemap, TagSitemap
from projects.sitemaps import ProjectSitemap
from staticpages.sitemaps import StaticSitemap

handler404 = 'staticpages.views.error404'
sitemaps = {
    'project': ProjectSitemap,
    'static': StaticSitemap,
    'article': ArticleSitemap,
    'category': CategorySitemap,
    'tag': TagSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),

    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('projects/', include('projects.urls'), ),

    path('blog/', include('blog.urls')),

    path('', include('staticpages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
