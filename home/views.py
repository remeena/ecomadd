from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect

from . models import Product
from . models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

   pro=Product.objects.all()
  
   return render(request,'home.html',{'pro':pro})

from django.shortcuts import render, redirect
from django.http import HttpResponse

# View to display the cart
def cart(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart1.html', {'cart': cart})

# View to add an item to the cart by product_id
def add_to_cart(request, product_id):
    # Get cart from session (or initialize an empty list if not exists)
    cart = request.session.get('cart', [])
    
    # Add the product_id to the cart
    cart.append(product_id)
    
    # Save the updated cart back to the session
    request.session['cart'] = cart
    
    return redirect('cart')

# View to remove an item from the cart by product_id
def remove_from_cart(request, product_id):
    # Get cart from session
    cart = request.session.get('cart', [])
    
    # Remove the product_id from the cart if it exists
    if product_id in cart:
        cart.remove(product_id)
    
    # Save the updated cart back to the session
    request.session['cart'] = cart
    
    return redirect('cart')
