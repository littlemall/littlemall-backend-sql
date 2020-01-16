
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^add_cart/$', views.CartAddView.as_view(), name='add_cart'),
   url(r'^query_cart/$', views.CartQueryView.as_view(), name='query_cart'),
   url(r'^update_cart/$', views.CartUpdateView.as_view(), name='update_cart'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
