
from django.urls import path, include
from rest_framework import routers
from shop.views import ProductVieset, CategoryViewset, AdminCategoryViewset

router = routers.SimpleRouter() 
router.register('category', CategoryViewset, basename='Category')
router.register('product', ProductVieset, basename= 'Product')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')

urlpatterns = [
    path('api/', include(router.urls)) 
]
