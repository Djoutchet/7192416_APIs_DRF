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
        
class ProductVieset(ReadOnlyModelViewSet):
    serializer_class =SerializersProduct
    def get_queryset(self):
        queryset= Product.objects.filter(active= True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id = category_id)
        return queryset
 
