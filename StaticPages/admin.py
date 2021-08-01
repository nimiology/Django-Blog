from django.contrib import admin
from .models import SocialMedias
# Register your models here.

class ScoialMediaAdmin(admin.ModelAdmin):
    list_display = ("Title","Link",)

admin.site.register(SocialMedias,ScoialMediaAdmin)