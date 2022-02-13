from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publishDate", "published")
    list_filter = ("title", "published")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["published", "publishDate"]


admin.site.register(Project, ProjectAdmin)
