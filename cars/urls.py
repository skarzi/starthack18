from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views

urlpatterns = [
    url(r'^$', views.CarsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CarDetail.as_view()),
    url(r'^unlock/(?P<pk>[0-9]+)/$', views.CarUnlock.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)