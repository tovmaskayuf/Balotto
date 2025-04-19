from .cart import Cart

def cart_total_quantity(request):
    cart = Cart(request)
    return{
        'cart_total_quantity':sum(item['quantity'] for item in cart)
    }
