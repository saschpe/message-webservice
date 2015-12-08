from tastypie import fields
from tastypie.resources import ModelResource

from .models import Message, Version


class MessageResource(ModelResource):
    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'
        allowed_methods = ['get']


class VersionResource(ModelResource):
    messages = fields.ForeignKey(Message, 'messages')

    class Meta:
        queryset = Version.objects.all()
        resource_name = 'version'
        allowed_methods = ['get']
