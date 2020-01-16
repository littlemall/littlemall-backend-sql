from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view

from cart.models import Fecart
from feuser.models import Feuser,FeAddress
from backendsql.res import Result
from backendsql.utils import encrypt_md5
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from feuser.utils import AuTokenPermission, get_au_token
import json

# Create your views here.

class CartAddView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      goods = request.data.get("goods", None)
      if goods is None:
        return Result(500,'参数错误',e)
      else:
        goods_list = json.loads(goods)
        price = 0;
        print(goods_list[0]["name"])
        for o in goods_list:
          price = price + int(o['price'])
        fecart = Fecart.objects.filter(
          user=request.user,
        )
        if(len(fecart) > 0):
          return Result(10020,'本用户已存在购物车，不能新增购物车',{})
        else:
          Fecart.objects.create(
            user=request.user,
            goods=goods,
            price=price,
          )
          return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)

class CartQueryView(APIView):
  permission_classes = (AuTokenPermission,)
  def get(self, request, format=None):
    try:
      feCart = Fecart.objects.filter(
        user=request.user
      )
      if(len(feCart) > 0):
        feCartObj = feCart.get()
        return Result(200,'success',{
          "goods":feCartObj.goods,
          "price":feCartObj.price,
          "created_at":feCartObj.created_at,
          "updated_at":feCartObj.updated_at
        })
      else:
        return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',{})

class CartUpdateView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      goods = request.data.get("goods", None)
      if(goods is None):
        return Result(500,'参数错误',e)
      else:
        goods_list = json.loads(goods)
        price = 0;
        for o in goods_list:
          price = price + int(o['price'])
        fecart = Fecart.objects.filter(
          user=request.user,
        )
        if(len(fecart) < 1):
          return Result(10020,'本用户没有可修改的购物车数据',{})
        else:
          fecart.update(
            goods=goods,
            price=price,
          )
          return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',str(e))
