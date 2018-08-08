from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from connects import viewsets

router = DefaultRouter()
router.register(r'connects', viewsets.ConnectViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
