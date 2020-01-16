from django.db import models
from feuser.models import Feuser, FeAddress

# Create your models here.
class Fecart(models.Model):
  user = models.OneToOneField(Feuser, on_delete=models.PROTECT,null=True)
  goods = models.TextField(default="[]")
  price = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at = models.DateTimeField(auto_now=True,null=True)
