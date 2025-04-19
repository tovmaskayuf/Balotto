from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart
from .models import Order, OrderItem

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})

def cart_increase(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart_detail')

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.core.mail import send_mail
from .cart import Cart
from .models import Order, OrderItem


def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        order = Order.objects.create(name=name, email=email)

        items_info = ""
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )
            items_info += f"{item['product'].name} × {item['quantity']} = €{item['total_price']}\n"

        send_mail(
            subject='New Order from Balotto Store',
            message=f"""
                New Order Received!

                Name: {name}
                Email: {email}

                Message from client:
                {message}

                Ordered items:
                {items_info}

                Total: €{cart.get_total_price()}
                """,
            from_email='danyyltest@gmail.com',
            recipient_list=['tikitiko.041111@gmail.com'],
            fail_silently=False,
        )

        cart.clear()

        return render(request, 'cart/thanks.html', {'name': name})

    return render(request, 'cart/checkout.html')
def success(request):
    return render(request, "cart/thanks.html")