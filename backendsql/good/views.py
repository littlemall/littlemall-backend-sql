from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view

from feuser.models import Feuser,FeAddress
from feuser.utils import AuTokenPermission, get_au_token
from backendsql.res import Result
from backendsql.utils import encrypt_md5
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from session.models import Session, SessionGoodsRelate
from good.models import Goods

# Create your views here.

class SessionListView(APIView):
  def get(self, request, format=None):
    try:
      page = request.GET.get("page", 1)
      size = request.GET.get("size", 10)
      sessionRes = Session.objects.filter(
        keyword="【推荐专场】"
      )
      if(len(sessionRes) > 0):
        session = sessionRes.get()
        sgrRes = SessionGoodsRelate.objects.filter(
          session=session
        )
        goods = []
        for sgr in sgrRes:
          goods.append(sgr.goods.id)
        # goodstr = ','.join(str(i) for i in goods)
        total = Goods.objects.order_by("-created_at").filter(
          id__in=goods
        )
        count = len(total)
        paginator = Paginator(total, size)
        try:
          good_list = paginator.page(page)
        except PageNotAnInteger:
          good_list = paginator.page(1)
        except EmptyPage:
          return Result(200,'success',{
            "count":   count,
            "list": [],
          })
        res = []
        for o in good_list:
          res.append({
           "name":o.name,
           "promotion":o.promotion,
           "keyword":o.keyword,
           "unit":o.unit,
           "tags":o.tags,
           "base_sale":o.base_sale,
           "base_click":o.base_click,
           "base_share":o.base_share,
           "product_code":o.product_code,
           "picture":o.picture,
           "starttime":o.starttime,
           "validity_period":o.validity_period,
           "inventory":o.inventory,
           "sku_ids":o.sku_ids,
           "photo":o.photo,
           "created_at":o.created_at
        })
        return Result(200,'success',{
          "count":   count,
          "list": res,
        })
      else:
        return Result(200,'success',{
          "count": count,
          "list": [],
        })
    except Exception as e:
      return Result(500,'error',str(e))

