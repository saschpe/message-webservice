from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import Message, Version


class VersionInline(admin.TabularInline):
    model = Version
    extra = 2


class MessageAdmin(TabbedTranslationAdmin):
    inlines = [VersionInline]
    list_display = ['title', 'body', 'type']
    list_filter = ['type']


admin.site.register(Message, MessageAdmin)
admin.site.register(Version)
