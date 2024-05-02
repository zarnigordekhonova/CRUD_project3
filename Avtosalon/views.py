from django.shortcuts import render
from .models import Transport, Categories

# Create your views here.


def get_info(request):
    categories = Categories.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'index.html', context=context)


def get_product(request, pk):
    products = Transport.objects.filter(category=pk)
    context = {
        'products' : products}

    return render(request, 'products.html', context=context)

def detail(request, pk):
    product = Transport.objects.get(pk=pk)
    context = {
        'product' : product
    }
    return render(request, 'detail.html', context=context)