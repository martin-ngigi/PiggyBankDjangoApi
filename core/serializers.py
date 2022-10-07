from rest_framework import serializers

from core.models import Category, Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        #feilds = ['id', 'code'.'name'] 
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'