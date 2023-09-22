
from django.urls import path
from shop import views

urlpatterns = [
    path('get_all_category', views.GetAllCategory.as_view()),
    path('get_all_product', views.GetAllProduct.as_view() )
]
