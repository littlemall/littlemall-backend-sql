
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^session_list/$', views.SessionListView.as_view(), name='session_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
