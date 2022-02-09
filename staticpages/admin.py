from django.contrib import admin

from staticpages.models import Setting, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "text")


admin.site.register(Setting)
admin.site.register(Message, MessageAdmin)
