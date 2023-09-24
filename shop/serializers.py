from rest_framework import serializers
from shop.models import Category, Product, Article



class SerializersProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name','date_created', 'date_updated', 'description', 'category']

    

class SerializerCategory(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = [ 'id', 'name', 'description', 'active', 'date_created', 'date_updated','products']
        
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializers = SerializersProduct(queryset, many= True)
        return serializers.data