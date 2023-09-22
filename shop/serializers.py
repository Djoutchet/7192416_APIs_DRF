from rest_framework import serializers
from shop.models import Category, Product, Article

class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id', 'name']

class SerializersProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name','date_created', 'date_updated', 'description', 'category']
    
