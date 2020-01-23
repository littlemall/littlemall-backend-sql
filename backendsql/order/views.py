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
        id=oid,
        user=request.user
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

class queryOrderView(APIView):
  permission_classes = (AuTokenPermission,)
  def get(self, request, format=None):
    try:
        orderRes = Feorder.objects.filter(
          user=request.user
        )
        if(len(orderRes) < 1):
          return Result(10010,'订单不存在',{})
        else:
          order = orderRes.get()
          return Result(200,'success',{
            "id":order.id,
            "goods":order.goods,
            "address":order.address,
            "oriprice":order.oriprice,
            "price":order.price,
            "status":order.status,
            "pay_type":order.pay_type,
            "created_at":order.created_at,
          })
    except Exception as e:
      return Result(500,'error',e)

class orderListView(APIView):
  permission_classes = (AuTokenPermission,)
  def get(self, request, format=None):
    try:
      page = request.GET.get("page", 1)
      size = request.GET.get("size", 10)
      total = Feorder.objects.order_by("-created_at").filter(
        user=request.user
      )
      count = len(total)
      paginator = Paginator(total, size)
      try:
        order_list = paginator.page(page)
      except PageNotAnInteger:
        address_list = paginator.page(1)
      except EmptyPage:
        return Result(200,'success',{
          "count":   count,
          "list": [],
        })
      res = []
      for order in order_list:
        res.append({
          "id":order.id,
          "goods":order.goods,
          "address":order.address,
          "oriprice":order.oriprice,
          "price":order.price,
          "status":order.status,
          "pay_type":order.pay_type,
          "created_at":order.created_at,
        })
      return Result(200,'success',{
        "count":   count,
        "list": res,
      })
    except Exception as e:
      return Result(500,'error',e)

class orderPayView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      oid = request.data.get("id", None)
      pay_type = request.data.get("pay_type", 0)
      orderRes = Feorder.objects.filter(
            id=oid,
            user=request.user
          )
      if(len(orderRes) < 1):
        return Result(10010,'订单不存在',{})
      else:
        order = orderRes.get()
        orderRes.update(
          pay_type=pay_type,
          status = 100
        )
      return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)

