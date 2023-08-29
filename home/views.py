from django.shortcuts import render, redirect
from .forms import ProductForm, OrderForm, MatumiziForm
from .models import Product, Orders, Expenses
from django.contrib import messages

# Create your views here.
def home(request):
    orders = Orders.objects.all()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully.')
            return redirect('home')
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, 'home/index.html', context)

def product(request):
    items = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully.')
            return redirect('products')
    context = {
        'form': form,
        'items': items
    }
    return render(request, 'home/products.html', context)

def matumizi(request):
    datas = Expenses.objects.all()
    form = MatumiziForm()
    if request.method == 'POST':
        form = MatumiziForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully.')
            return redirect('matumizi')
    context = {
        'form': form,
        'datas': datas
    }
    return render(request, 'home/matumizi_page.html', context)