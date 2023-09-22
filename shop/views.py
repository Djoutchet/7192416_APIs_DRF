from shop.serializers import SerializerCategory, SerializersProduct
from rest_framework.views import APIView 
from shop.models import Category, Product
from rest_framework.response import Response

class GetAllCategory(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializers = SerializerCategory(category, many= True)
        return Response(serializers.data)

class GetAllProduct(APIView):
    def get(self, *args , **kwargs):
        products = Product.objects.all()
        serializers = SerializersProduct(products, many = True)
        return Response(serializers.data)