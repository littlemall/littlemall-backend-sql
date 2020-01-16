
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view

from .models import Feuser,FeAddress
from .utils import AuTokenPermission, get_au_token
from backendsql.res import Result
from backendsql.utils import encrypt_md5
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 使用APIView
class FeuserView(APIView):
  permission_classes = (AuTokenPermission,)
  def get(self, request, format=None):
    feuser = request.user
    print(feuser.email);
    return Result(200,'success',{
      "email": feuser.email,
      "name": feuser.name,
      "gender": feuser.gender,
      "birthdate": feuser.birthdate,
      "avator": feuser.avator,
    })

class LoginView(APIView):
  def post(self, request, format=None):
    try:
      email = request.data.get("email", None)
      password = request.data.get("password", None)
      if(email is None or password is None):
        return Result(10020,'参数错误',{})
      else:
        feuser = Feuser.objects.filter(
          email=email
        )
        if(len(feuser) == 0):
          return Result(10030,'不存在该用户',{})
        else:
          feuserObj = feuser.get()
          cpassword = feuserObj.password
          upassword = encrypt_md5(password)
          uid = feuserObj.id
          if(cpassword != upassword):
            return Result(10040,'密码错误',{})
          else:
            token = get_au_token(uid)
            return Result(200,'success',{
              "token": token
            })

      return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)


class RegisterView(APIView):
  def post(self, request, format=None):
    try:
      email = request.data.get("email", None)
      password = request.data.get("password", None)
      if(email is None or password is None):
        return Result(10020,'参数错误',{})
      else:
        # 查询是否存在用户
        feuser = Feuser.objects.filter(
          email=email
        )
        if(len(feuser)):
          return Result(10030,'该邮箱已注册',{})
        else:
          password = encrypt_md5(password);
          Feuser.objects.create(
            email=email,
            password=password
          )
      return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)

class PasswordView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      feuser = request.user
      password = request.data.get("password", None)
      npassword = request.data.get("npassword", None)
      upassword = encrypt_md5(password);
      if(upassword !=  feuser.password):
        return Result(10040,'密码错误',{})
      else:
        feuser = Feuser.objects.filter(id=request.user.id);
        feuser.update(
          password = encrypt_md5(npassword)
        )
        return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)
    
class AddressAddView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      feuser = request.user
      name = request.data.get("name", None)
      street = request.data.get("street", None)
      street_ext = request.data.get("street_ext", None)
      city = request.data.get("city", None)
      district = request.data.get("district", None)
      country = request.data.get("country", None)
      code = request.data.get("code", None)
      if(name is None or street is None):
        return Result(10020,'参数错误',{})
      addressObj = FeAddress.objects.filter(
        user=feuser
      )
      if(len(addressObj) > 5):
        return Result(10030,'已超出地址最大限制',{})
      else:
        FeAddress.objects.create(
          user=feuser,
          name=name,
          street= street,
          street_ext= street_ext,
          city = city,
          district = district,
          country = country,
          code = code
        )
        return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)

  def get(self, request, format=None):
    try:
      page = request.GET.get("page", 1)
      size = request.GET.get("size", 10)
      total = FeAddress.objects.order_by("-created_at").filter(
          user=request.user
      )
      count = len(total)
      paginator = Paginator(total, size)
      try:
        address_list = paginator.page(page)
      except PageNotAnInteger:
        address_list = paginator.page(1)
      except EmptyPage:
        return Result(200,'success',{
          "count":   count,
          "list": [],
        })
      res = []
      for o in address_list:
        res.append({
            "name": o.name,
            "street": o.street,
            "street_ext": o.street_ext,
            "city": o.city,
            "district": o.district,
            "country": o.country,
            "code": o.code,
            "is_default": o.is_default,
        })
      return Result(200,'success',{
          "count":   count,
          "list": res,
        })
    except Exception as e:
      return Result(500,'error',e)

class AddressUpdateView(APIView):
  permission_classes = (AuTokenPermission,)
  def post(self, request, format=None):
    try:
      feuser = request.user
      aid = request.data.get("id", None)
      name = request.data.get("name", None)
      street = request.data.get("street", None)
      street_ext = request.data.get("street_ext", None)
      city = request.data.get("city", None)
      district = request.data.get("district", None)
      country = request.data.get("country", None)
      code = request.data.get("code", None)
      if(aid is None or name is None or street is None):
        return Result(10020,'参数错误',{})
      addressObj = FeAddress.objects.filter(
        user=feuser,
        id=aid
      )
      if(len(addressObj) < 1):
        return Result(10040,'没有数据可修改',{})
      else:
        addressObj.update(
          name=name,
          street= street,
          street_ext= street_ext,
          city = city,
          district = district,
          country = country,
          code = code
        )
        return Result(200,'success',{})
    except Exception as e:
      return Result(500,'error',e)
    

      