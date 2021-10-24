from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publishDate", "publish")
    list_filter = ("title", "publish")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["publish", "publishDate"]


admin.site.register(Project, ProjectAdmin)
