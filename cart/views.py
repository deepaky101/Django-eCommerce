from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from store.models import Product

# Create your views here.
def Cart(request):
    cart_items = Item.objects.all()
    return render(request, 'cart/cart.html', {'cart_items' : cart_items})

def Add_To_Cart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart_item, created = Item.objects.get_or_create(product = product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

def Add_To_Cart_on_cart_page(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart_item, created = Item.objects.get_or_create(product = product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def Remove_To_Cart(request, product_id):
    cart_item = Item.objects.filter(product_id = product_id).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')
        
def Cart_Length(request):
    count = Item.objects.all().count()
    return {'count': count}