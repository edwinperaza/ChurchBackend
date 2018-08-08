from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from contact import viewsets

router = DefaultRouter()
router.register(r'contacts', viewsets.ContactViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
