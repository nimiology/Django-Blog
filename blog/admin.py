from django.contrib import admin
from .models import Article, Category, Tag, Section


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publishDate", "published")
    list_filter = ("publishDate", "published")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["published", "publishDate"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published")
    list_filter = (["published"])
    search_fields = ("title", 'slug')
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published")
    list_filter = (["published"])
    search_fields = ("title", 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Section)