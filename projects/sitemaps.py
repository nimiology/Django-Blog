from django.contrib.sitemaps import Sitemap

from projects.models import Project


class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 1

    def items(self):
        return Project.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated