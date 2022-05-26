from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductList(ListView):
    model = Product
    ordering = 'date_create'
    template_name = 'market/product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'market/product_detail.html'


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'market/category_list.html'


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'market/category_detail.html'



def index(request):
    return render(request, 'market/index.html')

