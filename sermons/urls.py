from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sermons import views

urlpatterns = [
    url(r'^series/$', views.SerieList.as_view()),
    url(r'^series/(?P<pk>[0-9]+)/$', views.SerieDetail.as_view()),
    url(r'^sermons/$', views.SermonList.as_view()),
    url(r'^sermons/(?P<pk>[0-9]+)/$', views.SermonDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)