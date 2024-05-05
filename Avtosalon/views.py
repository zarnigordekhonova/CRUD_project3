from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories, Transport
from .forms import TransportForm

# Create your views here.

def get_info(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = Transport.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)

def detail(request, pk):
    product = Transport.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)


def add_products(request):
    form = TransportForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Transport:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = Transport.objects.get(pk=pk)
    form = TransportForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('Transport:get_info')
    context = {
        'form': form
    }
    return render(request, 'update.html', context=context)


def delete_products(request, pk):
    product = get_object_or_404(Transport, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Transport:get_info')

    return render(request, 'delete.html', {'product': product})



