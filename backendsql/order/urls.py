
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
   url(r'^add_order/$', views.OrderAddView.as_view(), name='add_order'),
   url(r'^cancel_order/$', views.OrderCancelView.as_view(), name='cancel_order'),
   url(r'^query_order/$', views.queryOrderView.as_view(), name='query_order'),
   url(r'^order_list/$', views.orderListView.as_view(), name='order_list'),
   url(r'^order_pay/$', views.orderPayView.as_view(), name='order_pay'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
