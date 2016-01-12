from django.contrib.auth.models import User
from rest_framework import generics, serializers, viewsets
from .models import Message, ProductPlatform, ProductFlavor, Version


class TranslateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(TranslateSerializer, self).__init__(*args, **kwargs)
        self.translate_fields = getattr(self.Meta, 'translate_fields', ())
        if kwargs.get('context', None):
            self.lang = utils.get_request_language(kwargs['context'].get('request', None))

    def to_native(self, obj):
        # Exclude ALWAYS language specific fields
        for language in settings.LANGUAGES:
            if language[0] != 'en':
                for field in self.translate_fields:
                    key = field + '_' + language[0]
                    if self.fields.get(key):
                        self.fields.pop(key)

        ret = super(serializers.ModelSerializer, self).to_native(obj)

        # Get current language and give the fields
        if self.lang != 'en':
            for field in self.translate_fields:
                trans = getattr(obj, field + "_" + self.lang)
                if trans:
                    ret[field] = trans
        return ret

    def from_native(self, data, files):
        instance = getattr(self, 'object', None)
        if self.lang != 'en':
            for field in self.translate_fields:
                value = data.get(field) or None
                if value:
                    data[field + "_" + self.lang] = value
                    # If is instance (existent object), set the original attr
                    data[field] = getattr(instance, field, data[field])

        ret = super(serializers.ModelSerializer, self).from_native(data, files)
        return ret


class MessageSerializer(TranslateSerializer):
    class Meta:
        model = Message
        fields = ('title', 'body', 'type', 'created_at', 'updated_at')


class ProductPlatformSerializer(serializers.ModelSerializer):
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


class VersionMessageSerializer(serializers.ModelSerializer):
    title    = serializers.ReadOnlyField(source='message.title')
    body     = serializers.ReadOnlyField(source='message.body')
    type     = serializers.ReadOnlyField(source='message.type')
    platform = serializers.ReadOnlyField(source='flavor.platform.title')
    flavor   = serializers.ReadOnlyField(source='flavor.title')

    class Meta:
        model = Version
        nested = False
        exclude = ('id', 'message', 'author', 'comment', 'flavor', 'created_at', 'updated_at')

    
class AllMessages(generics.ListAPIView):
    serializer_class = VersionMessageSerializer
    queryset = Version.objects.all()


class PlatformMessages(generics.ListAPIView):
    serializer_class = VersionMessageSerializer
    lookup_platform = "platform"

    def get_queryset(self):
        p = self.kwargs.get(self.lookup_platform)
        message = Version.objects.filter(flavor__platform__title__iexact=p)
        return message


class FlavorMessages(generics.ListAPIView):
    serializer_class = VersionMessageSerializer
    lookup_platform  = "platform"
    lookup_flavor = "flavor"

    def get_queryset(self):
        p = self.kwargs.get(self.lookup_platform)
        f = self.kwargs.get(self.lookup_flavor)
        message = Version.objects.filter(flavor__platform__title__iexact=p, flavor__title__iexact=f)
        return message


class VersionMessages(generics.ListAPIView):
    serializer_class = VersionMessageSerializer
    lookup_platform  = "platform"
    lookup_flavor    = "flavor"
    lookup_version   = "version"

    def get_queryset(self):
        p = self.kwargs.get(self.lookup_platform)
        f = self.kwargs.get(self.lookup_flavor)
        v = self.kwargs.get(self.lookup_version)
        message = Version.objects.filter(flavor__platform__title__iexact=p, flavor__title__iexact=f, version=v)
        return message
