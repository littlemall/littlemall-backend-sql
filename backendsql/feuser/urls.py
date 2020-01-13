
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^api/$', views.FeuserView.as_view(), name='feuser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
