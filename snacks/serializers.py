
from rest_framework import serializers
from .models import Meal

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields =['id','owner', 'title', 'desc']
        # fields = '__all__'