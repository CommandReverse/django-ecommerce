from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories(request):
    return {'categories': Category.objects.all()}

def home(request):
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'categories': categories})

def about(request):
    return render(request, 'store/about.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def product_detail(request, slug):
   product = get_object_or_404(Product, slug=slug, in_stock=True) 
   return render(request, 'store/products/detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
