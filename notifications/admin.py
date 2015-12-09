from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import Message, ProductPlatform, ProductFlavor, Version


class MessageAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'body', 'type']
    list_filter = ['type']


class PlatformAdmin(admin.ModelAdmin):
    list_display = ['title']


class FlavorAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform']
    list_filter = ['platform']


class VersionAdmin(admin.ModelAdmin):
    list_display = ['version', 'flavor', 'message', 'message_type', 'comment']
    list_filter = ['message', 'flavor']

    def message_type(self, obj):
        return obj.message.type


admin.site.register(Message, MessageAdmin)
admin.site.register(ProductPlatform, PlatformAdmin)
admin.site.register(ProductFlavor, FlavorAdmin)
admin.site.register(Version, VersionAdmin)
