from dataclasses import fields
from unicodedata import category
from rest_framework import serializers
from django.contrib.auth.models import User

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

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = fields

class WriteTransactionSerializer(serializers.ModelSerializer):
    # While inserting currency, intead of using id of currency, use text instead and afterwards display all currencies in text form
    # eg 
    #     {
    #     "currency": "Ksh",
    #     "amount": "20.00",
    #     "date": "2022-08-10T09:22:33Z",
    #     "description": "Testing Kenyan currency",
    #     "category": 3
    # }
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = Transaction
        fields = '__all__'

class ReadTransactionSerializer(serializers.ModelSerializer):
    # return nested object
    # the GET Will return TransactionSerializer and CurrencySerializer inside of TransactionSerializer in the "currency":"" and "category":""
    # eg
    # {
    #     "id": 1,
    #     "currency": {
    #         "id": 2,
    #         "code": "Ksh",
    #         "name": "Kenyan Currency"
    #     },
    #     "category": {
    #         "id": 3,
    #         "name": "Transport"
    #     },
    #     "amount": "30.00",
    #     "date": "2022-08-10T09:22:33Z",
    #     "description": "Testing USA currency"
    # },
    
    # user = ReadUserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = '__all__'

    read_only_fields = fields