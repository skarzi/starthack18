from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^scores/$', views.UserScoresList.as_view()),
    url(r'^leaderboard/(?P<top>[0-9]+)$', views.Leaderboard.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)