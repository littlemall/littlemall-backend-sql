from django.http import JsonResponse

def Result(code,msg,data):
  return JsonResponse({
    "code": code,
    "msg": msg,
    "data": data
})