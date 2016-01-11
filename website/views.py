from django.shortcuts import redirect

import django_filters
from rest_framework import filters
from rest_framework import generics
from notifications.models import Version
from notifications.api import VersionMessageSerializer


def index(request):
    return redirect('/admin')


class VersionList(generics.ListAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionMessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('version', 'flavor__title', 'flavor__platform__title',)

