from rest_framework import serializers
from shop.models import Category, Product, Article

class serializersArcticles(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields= [ "date_created", "date_updated", "name", "description", "active", "price"]

class SerializersProduct(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [ 'id', 'name','date_created', 'date_updated', 'description', 'category','articles']

# filtrage des article active
    def get_articles(self, instance):
        queryset = instance.articles.filter(active =True)
        serializers = serializersArcticles(queryset, many=True)
        return serializers.data

    
class SerializersListCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']

class SerializerCategory(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = [ 'id', 'name', 'description', 'active', 'date_created', 'date_updated','products']
        
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializers = SerializersProduct(queryset, many= True)
        return serializers.data