from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('products', views.products, name='all_product'),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>', views.category_list, name='category_list'),
]
