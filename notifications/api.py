from rest_framework import serializers, viewsets

from .models import Message, ProductPlatform, ProductFlavor, Version


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message


class ProductPlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPlatform


class ProductFlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductFlavor


class VersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Version
        fields = ('version', 'flavor', 'message')
        depth = 2


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
