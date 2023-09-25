from shop.serializers import SerializerCategory, SerializersProduct, SerializersListCategory
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from shop.models import Category, Product
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

"""class CategoryViewset(ReadOnlyModelViewSet):  # proprieté de lecture seul
    serializer_class = SerializerCategory
    def get_queryset(self):
        return Category.objects.all()"""

#misse en place d'un filtre
class CategoryViewset(ReadOnlyModelViewSet):  
    serializer_class = SerializersListCategory
    serializer_detail_class = SerializerCategory 
    def get_queryset(self):
        return Category.objects.filter(active =True)

    def get_serializer_class(self):
        if self.action=='retrieve':  # si l'action est un détail
            return self.serializer_detail_class
        return super().get_serializer_class()

# Pour mettre action en place il faudra écrire une methode avec le meme non que 
# la methode définir dans le model en question ici categorie
    @action(detail=True, methods=['post']) # la methode acesible droit etre uniquement le post
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

class ProductVieset(ReadOnlyModelViewSet):
    serializer_class =SerializersProduct
    def get_queryset(self):
        queryset= Product.objects.filter(active= True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id = category_id)
        return queryset
    
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()

# la mise en place de ces methode permet de redéfinir les methode 
# qui ne sont pas définir dans les opération du CRUD, comme je viens de la faire
# #sont implementation est dans le model et la vue particulièrement  

class AdminCategoryViewset(ModelViewSet):
    serializer_class = SerializersListCategory
    serializer_detail_class = SerializerCategory
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return Category.objects.all()
