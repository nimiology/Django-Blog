from django.contrib import admin
from .models import Article, Category


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publishDate", "published")
    list_filter = ("publishDate", "published")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["published", "publishDate"]



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status")
    list_filter = (["status"])
    search_fields = ("title", 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
