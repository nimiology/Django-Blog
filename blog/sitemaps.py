from django.contrib.sitemaps import Sitemap

from blog.models import Article, Category, Tag


class ArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.7

    def items(self):
        return Article.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.publishDate


class CategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.3

    def items(self):
        return Category.objects.filter(published=True)


class TagSitemap(CategorySitemap):
    def items(self):
        return Tag.objects.filter(published=True)
