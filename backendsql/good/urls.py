
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^session_list/$', views.SessionListView.as_view(), name='session_list'),
   url(r'^goods_detail/$', views.GoodsDetailView.as_view(), name='goods_detail'),
   url(r'^search_goods/$', views.SearchGoodsView.as_view(), name='search_goods'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
