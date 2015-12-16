from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Message, ProductPlatform, ProductFlavor, Version


@admin.register(Message)
class MessageAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'body', 'type', 'author', 'created_at', 'updated_at']
    list_filter = ['type', 'author']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


@admin.register(ProductPlatform)
class ProductPlatformAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProductFlavor)
class ProductFlavorAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform']
    list_filter = ['platform']


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['version', 'flavor', 'message', 'message_type', 'comment', 'author', 'created_at', 'updated_at']
    list_filter = ['flavor', 'message', 'author']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def message_type(self, obj):
        for k, v in Message.MESSAGE_CHOICES:
            if k == obj.message.type:
            	return v
        return ''
