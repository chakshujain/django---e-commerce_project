from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from carts.models import Cart,CartItem
from products.models import Product,Variation
# Create your views here.
def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if(the_id):
        cart = Cart.objects.get(id = the_id)
        context = {'cart':cart}
    else:
        empty_message = "YOUR CART IS EMPTY"
        context = {'empty':True,'empty_message':empty_message}
    template = 'carts/view.html'
    return render(request,template,context)

def remove_from_cart(request,id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id =id)
    cartitem.cart = None
    cartitem.save()
    return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request,slug):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug = slug)
    except:
        pass


    product_var = []
    if request.method=="POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(product = product,category__iexact=key,title__iexact=val)
                product_var.append(v)
            except:
                pass
        cart_item = CartItem.objects.create(cart = cart, product = product)
        if(len(product_var)>0):
            for item in product_var:
                cart_item.variations.add(item)

        cart_item.quantity = qty
        cart_item.save()


        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price)*item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cartitem_set.count()

        cart.total = new_total
        cart.save()

        return HttpResponseRedirect(reverse('cart'))
    else:
        return HttpResponseRedirect(reverse('cart'))
