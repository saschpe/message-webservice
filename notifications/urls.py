from django.conf.urls import include, url
from rest_framework import routers

from .api import MessageViewSet, ProductPlatformViewSet, ProductFlavorViewSet, VersionViewSet


router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'platforms', ProductPlatformViewSet)
router.register(r'flavors', ProductFlavorViewSet)
router.register(r'versions', VersionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
