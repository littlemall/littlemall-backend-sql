from rest_framework import serializers
from .models import Feuser

class FeuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feuser
        fields = ("id","name","email","password","avator","gender","birthdate","created_at","updated_at")