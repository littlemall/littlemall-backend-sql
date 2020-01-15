from django.db import models

# Create your models here.

class Feuser(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100,unique=True)
  password =  models.CharField(max_length=100)
  avator =  models.CharField(max_length=2048)
  gender =  models.IntegerField(default=0)
  birthdate = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class FeAddress(models.Model):
  user = models.ForeignKey(Feuser, on_delete=models.PROTECT)
  name = models.CharField(max_length=512)
  street = models.CharField(max_length=512)
  street_ext =  models.CharField(max_length=512,null=True)
  city = models.CharField(max_length=64,null=True)
  district = models.CharField(max_length=64,null=True)
  country = models.CharField(max_length=64,null=True)
  code = models.CharField(max_length=10,null=True)
  is_default = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)