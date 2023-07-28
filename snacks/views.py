from django.shortcuts import render
from .models import Meal
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer
# Create your views here.

# class SnackListView(ListAPIView):
class SnackListView(ListCreateAPIView):

    queryset = Meal.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = SnackSerializer

