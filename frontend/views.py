from django.shortcuts import render
from .models import *
# Create your views here.


def products(request):
    products = Products.objects.all()
    return render(request, 'product.html', {'products': products})
