from django.db import models
from feuser.models import Feuser, FeAddress

# Create your models here.
class Fecart(models.Model):
  user = models.ForeignKey(Feuser, on_delete=models.PROTECT)
  goods = models.TextField(blank=True),
  price = models.IntegerField(blank=True),
  address = models.ForeignKey(FeAddress, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
