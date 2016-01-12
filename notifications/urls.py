from django.conf.urls import include, url
from .api import *


urlpatterns = [
    url(r'messages/$', AllMessages.as_view()),
    url(r'messages/(?P<platform>[a-zA-Z_-]+)/$', PlatformMessages.as_view()),
    url(r'messages/(?P<platform>[a-zA-Z_-]+)/(?P<flavor>[a-zA-Z_-]+)/$', FlavorMessages.as_view()),
    url(r'messages/(?P<platform>[a-zA-Z_-]+)/(?P<flavor>[a-zA-Z_-]+)/(?P<version>[0-9.]+)/$', VersionMessages.as_view()),
]
