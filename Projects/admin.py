from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("Title","slug","Publish","Status")
    list_filter = ("Publish","Status")
    search_fields = ("Title","Text")
    prepopulated_fields = {"slug":("Title",)}
    ordering = ["Status","Publish"]

admin.site.register(Project, ProjectAdmin)