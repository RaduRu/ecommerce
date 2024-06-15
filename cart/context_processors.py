from .cart import Cart

#i need to make sure the cart works on all pages

def cart(request):
    return {'cart': Cart(request)}