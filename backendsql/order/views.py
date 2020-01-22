from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from feuser.utils import AuTokenPermission, get_au_token
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.models import Fecart
from feuser.models import Feuser,FeAddress
from backendsql.res import Result
from backendsql.utils import encrypt_md5
from order.models import Feorder
# Create your views here.

class OrderAddView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      address = request.data.get("address", None)
      fecart = Fecart.objects.filter(
        user=request.user
      )
      if(len(fecart) < 1):
        return Result(10010,'购物车不存在',{})
      else:
        fecartObj = fecart.get()
        goods = fecartObj.goods
        price = fecartObj.price
        Feorder.objects.create(
          user = request.user,
          address = address,
          goods = goods,
          oriprice = price
        )
        return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)

class OrderCancelView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      oid = request.data.get("id", None)
      orderRes = Feorder.objects.filter(
        id=oid
      )
      if(len(orderRes)>0):
        orderRes.update(
          status = -20
        )
        return Result(200,'success',{})
      else:
        return Result(10010,'订单不存在',{})
    except Exception as e:
      return Result(500,'error',e)

class queryOrder(APIView):
  permission_classes = (AuTokenPermission,)
  try:
    pass
  except Exception as e:
    return Result(500,'error',e)
