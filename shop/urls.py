
from django.urls import path, include
from rest_framework import routers
from shop.views import ProductVieset, CategoryViewset

router = routers.SimpleRouter() 
router.register('category', CategoryViewset, basename='Category')
router.register('product', ProductVieset, basename= 'Product')

urlpatterns = [
    path('api/', include(router.urls))
    
]
