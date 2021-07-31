from django.contrib import admin
from .models import Article,Category
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("Title","slug","Publish","Status","Category_to_str")
    list_filter = ("Publish","Status")
    search_fields = ("Title","Text")
    prepopulated_fields = {"slug":("Title",)}
    ordering = ["Status","Publish"]
    def Category_to_str(self, obj):
        return " ".join([category.Title for category in obj.category_Publish()])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Position',"Title", "slug", "Status")
    list_filter = (["Status"])
    search_fields = ("Title",'slug')
    prepopulated_fields = {"slug": ("Title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)