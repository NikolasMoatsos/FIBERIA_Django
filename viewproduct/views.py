from django.shortcuts import render
from .models import Product
# Create your views here.

def view_product(request,id):
    try:
        product = Product.objects.get(id=int(id))
    except:
        return render(request, 'product.html', {'mess': 'Product Not Found !', 'found': False})
    return render(request, 'product.html', {'pr': product, 'found': True})

def view_collection(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        return render(request, 'collection.html', {'mess': 'There are no Products', 'found': False})
    return render(request, 'collection.html', {'products': products, 'found': True})
