from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views
from cars.views import ws_car_test

urlpatterns = [
    url(r'^$', views.CarsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CarDetail.as_view()),
    url(r'^unlock/(?P<car_pk>[0-9]+)/(?P<user_pk>[0-9]+)/$', views.CarUnlock.as_view()),
    url(r'^reserve/(?P<car_pk>[0-9]+)/(?P<user_pk>[0-9]+)/$', views.CarReserve.as_view()),
    url(r'^wscartest/(?P<pk>[0-9]+)$', ws_car_test, name='ws_car_test'),
]

urlpatterns = format_suffix_patterns(urlpatterns)