from django.contrib import admin

from StaticPages.models import About, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "text")


admin.site.register(About)
admin.site.register(Message, MessageAdmin)
