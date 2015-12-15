from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Message, ProductPlatform, ProductFlavor, Version


@admin.register(Message)
class MessageAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'body', 'type']
    list_filter = ['type']


@admin.register(ProductPlatform)
class ProductPlatformAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProductFlavor)
class ProductFlavorAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform']
    list_filter = ['platform']


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['version', 'flavor', 'message', 'message_type', 'comment']
    list_filter = ['flavor', 'message']

    def message_type(self, obj):
        for k, v in Message.MESSAGE_CHOICES:
            if k == obj.message.type:
            	return v
        return ''

    def platform(self, obj):
        return obj.flavor.platform


