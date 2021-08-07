from django.contrib import admin
from .models import Diaries
# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ["Date"]
    list_filter = ["Date"]
    search_fields = ["Date"]
    ordering = ["Date"]

admin.site.register(Diaries,DiaryAdmin)