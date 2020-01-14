
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view

from .models import Feuser
from .utils import AuTokenPermission, get_au_token
from backendsql.res import Result
from backendsql.utils import encrypt_md5

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
    