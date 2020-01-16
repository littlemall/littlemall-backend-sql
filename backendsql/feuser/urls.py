
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^get_user/$', views.FeuserView.as_view(), name='feuser'),
   url(r'^login/$', views.LoginView.as_view(), name='login'),
   url(r'^register/$', views.RegisterView.as_view(), name='register'),
   url(r'^password/$', views.PasswordView.as_view(), name='password'),
   url(r'^add_address/$', views.AddressAddView.as_view(), name='add_address'),
   url(r'^list_address/$', views.AddressAddView.as_view(), name='list_address'),
   url(r'^update_address/$', views.AddressUpdateView.as_view(), name='update_address'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
