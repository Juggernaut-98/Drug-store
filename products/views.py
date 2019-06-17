from django.shortcuts import render
from .models import product


# Create your views here.
def products(request, _id=None):
    products = product.objects.all()
    if id!=None:
        products = product.objects.filter(category_id=_id)
        return render(request, 'products/products.html', {'data': products})
    return render(request, 'products/products.html', {'data': products})


def product_details(request, _id=None):
    return render(request, 'products/product_details.html', {'data': product.objects.filter(id=_id)})


def checkout(request):
    return render(request, 'products/checkout.html')
