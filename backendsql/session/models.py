from django.db import models
from good.models import *

# Create your models here.
class Session(models.Model):
    name = models.CharField(max_length=256,blank=True, null=True)
    keyword = models.CharField(max_length=128,blank=True, null=True)
    desc = models.CharField(max_length=512,blank=True, null=True)
    photos = models.CharField(max_length=2048,blank=True, null=True)
    banner_pc = models.CharField(max_length=2048,blank=True, null=True)
    banner_mobile = models.CharField(max_length=2048,blank=True, null=True)
    bgcolor = models.CharField(max_length=64,blank=True, null=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True,default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

class SessionGoodsRelate(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.PROTECT, related_name="as_good_session",null=True)
    session = models.ForeignKey(Session, on_delete=models.PROTECT, related_name="as_session_good",null=True)
    status = models.IntegerField(blank=True,default=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        unique_together = ('goods', 'session',)