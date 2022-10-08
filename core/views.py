from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework import status
from rest_framework.filters import SearchFilter

from core.models import Category, Currency, Transaction
from core.serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer, WriteTransactionSerializer

# Create your views here.

# A serializer is used to transform data from pyhthon format to json object


class CurrencyListAPiView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyModelViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.all() # Fetch all
    #queryset = Transaction.objects.select_related("currency") #fetch transactions that are related in currency
    filter_backends = (SearchFilter,)
    search_fields = ("amount",) # i.e. serach amount that is equal to 30 
                                # GET endpoint  http://127.0.0.1:8000/transactions/?search=30


    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        # else
        return WriteTransactionSerializer