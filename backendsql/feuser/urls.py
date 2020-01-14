
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^get_user/$', views.FeuserView.as_view(), name='feuser'),
   url(r'^login/$', views.LoginView.as_view(), name='login'),
   url(r'^register/$', views.RegisterView.as_view(), name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
