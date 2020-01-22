from django.db import models
# Create your models here.
from feuser.models import Feuser, FeAddress
from cart.models import Fecart

# Create your models here.
class Feorder(models.Model):
  user = models.ForeignKey(Feuser, on_delete=models.PROTECT)
  address = models.TextField(blank=True,null=True)
  goods = models.TextField(blank=True,null=True)
  oriprice = models.IntegerField(blank=True,null=True)
  price = models.IntegerField(blank=True,null=True)
  pay_type = models.IntegerField(blank=True,default=0)
  status = models.IntegerField(blank=True,default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
