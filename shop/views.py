from shop.serializers import SerializerCategory, SerializersProduct
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from shop.models import Category, Product
from rest_framework.response import Response

"""class CategoryViewset(ReadOnlyModelViewSet):  # proprieté de lecture seul
    serializer_class = SerializerCategory
    def get_queryset(self):
        return Category.objects.all()"""

#misse en place d'un filtre
class CategoryViewset(ReadOnlyModelViewSet):  
    serializer_class = SerializerCategory
    def get_queryset(self):
        return Category.objects.filter(active =True)
        
class ProductVieset(ModelViewSet):
    serializer_class =SerializersProduct
    def get_queryset(self):
        return Product.objects.all()