# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import time

import jwt
import pyotp
from rest_framework.permissions import BasePermission
from feuser.models import Feuser
from django.conf import settings

APP_SH_SECRET_KEY = settings.APP_SH_SECRET_KEY

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_au_token(user_id, expiry=86400000, ext=None):  # 1000 days
    key = APP_SH_SECRET_KEY
    return jwt.encode({
        "uid": user_id,
        "ext": ext,
        "exp": int(time.time() + 86400000)
    }, key, algorithm="HS256").decode("u8")

def au_from_token(t):
    key = APP_SH_SECRET_KEY
    data = jwt.decode(t, key, algorithms=["HS256"])
    user = Feuser.objects.get(id=data["uid"])
    return user, data


class AuTokenPermission(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        auth = request.META.get('HTTP_AUTHORIZATION')
        gpt = request.COOKIES.get("app_tok")
        if gpt:
            try:
                user, tok = au_from_token(gpt)
            except Exception as e:
                print(e)
                return False
        elif auth:
            try:
                user, tok = au_from_token(auth)
            except Exception as e:
                print(e)
                return False
        else:
            return False

        request.user = user
        request.tok = tok

        return True
