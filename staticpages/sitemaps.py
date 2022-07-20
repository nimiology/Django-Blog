from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['staticpages:home', 'staticpages:about', 'staticpages:notFound']

    def location(self, item):
        return reverse(item)