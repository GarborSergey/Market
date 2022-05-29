from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<slug:category_slug>', views.products_in_category, name='category_detail'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),

]