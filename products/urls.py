from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:_id>', views.products, name='products'),
    path('details', views.product_details, name='product_details'),
    path('checkout', views.checkout, name='checkout')
]