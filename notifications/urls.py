from django.conf.urls import include, url
from .api import *


urlpatterns = [
    url(r'messages/$', AllMessages.as_view()),
    url(r'messages/(?P<platform>\w+)/$', PlatformMessages.as_view()),
    url(r'messages/(?P<platform>\w+)/(?P<flavor>\w+)/$', FlavorMessages.as_view()),
    url(r'messages/(?P<platform>\w+)/(?P<flavor>\w+)/(?P<version>\w+)/$', VersionMessages.as_view()),
]
