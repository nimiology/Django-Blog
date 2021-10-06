from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publish", "status")
    list_filter = ("title", "status")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "publish"]


admin.site.register(Project, ProjectAdmin)
