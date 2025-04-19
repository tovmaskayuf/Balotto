from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.cart import Cart

def home(request):
    products = Product.objects.all()
    cart = Cart(request)
    return render(request, 'shop/index.html', {'products': products, 'cart': cart})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})