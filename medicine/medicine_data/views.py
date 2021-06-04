from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .models import KoreanData, ForeignData
from medicine.serializer import KoreanSerializer, ForeignSerializer
from django.db import connection
# Create your views here.

class Koreanviewset(viewsets.ModelViewSet):
   queryset = KoreanData.objects.all()
   serializer_class = KoreanSerializer

class Foreignviewset(viewsets.ModelViewSet):
   queryset = ForeignData.objects.all()
   serializer_class = ForeignSerializer
