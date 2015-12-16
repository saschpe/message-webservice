from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Message, ProductPlatform, ProductFlavor, Version

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('title', 'body', 'type', 'created_at', 'updated_at')


class ProductPlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPlatform


class ProductFlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductFlavor
        depth = 1


class VersionSerializer(serializers.HyperlinkedModelSerializer):
    message = MessageSerializer()
    flavor = ProductFlavorSerializer()

    class Meta:
        model = Version
        exclude = ('author',)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ProductPlatformViewSet(viewsets.ModelViewSet):
    queryset = ProductPlatform.objects.all()
    serializer_class = ProductPlatformSerializer


class ProductFlavorViewSet(viewsets.ModelViewSet):
    queryset = ProductFlavor.objects.all()
    serializer_class = ProductFlavorSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
