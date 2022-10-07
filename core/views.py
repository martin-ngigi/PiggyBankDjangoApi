from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework import status

from core.models import Category, Currency
from core.serializers import CategorySerializer, CurrencySerializer

# Create your views here.

class CurrencyListAPiView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
