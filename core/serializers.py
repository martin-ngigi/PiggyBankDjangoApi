from dataclasses import fields
from rest_framework import serializers

# A serializer is used to transform data from pyhthon format to json object

from core.models import Category, Currency, Transaction

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        #feilds = ['id', 'code'.'name'] 
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'