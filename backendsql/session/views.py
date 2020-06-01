from django.shortcuts import render
from session.models import Session, SessionGoodsRelate

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

# Create your views here.

class NormalSessionListView(APIView):
  def get(self, request, format=None):
    try:
      sessionRes=Session.objects.filter(
        status=0
      )
      count = len(sessionRes)
      if(len(sessionRes)>0):
        paginator = Paginator(sessionRes, 5)
        try:
          session_list = paginator.page(1)
        except PageNotAnInteger:
          session_list = paginator.page(1)
        except EmptyPage:
            return Result(200,'success',{
              "count": 0,
              "list": [],
            })
        res = []
        for o in session_list:
          res.append({
            "name":o.name,
            "keyword":o.keyword,
            "desc":o.desc,
            "photos":o.photos,
            "banner_pc":o.banner_pc,
            "banner_mobile":o.banner_mobile,
            "bgcolor":o.bgcolor,
            "start_at":o.start_at,
            "end_at":o.end_at,
            "status":o.status,
            "created_at":o.created_at,
            "updated_at":o.updated_at,
            })
        return Result(200,'success',{
                "count": count,
                "list": res,
              })
    except Exception as e:
      return Result(500,'error',str(e))
