from django.db import models

# Create your models here.
class Feuser(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  password =  models.CharField(max_length=100)
  avator =  models.CharField(max_length=2048)
  gender =  models.IntegerField(default=0)
  birthdate = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)