from django.shortcuts import render,Http404
from products.models import Product
# Create your views here.
def home(request):
    template = 'products/home.html'
    context = {'products':Product.objects.all()}
    return render(request,template,context)

def single(request,slug):
        product = Product.objects.get(slug = slug)
        images = product.productimage_set.all()
        products = Product.objects.all()
        template = 'products/single.html'
        context = {'product':product,"images":images}
        return render(request,template,context)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains = q)
        context = {'query':q,'products':products}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {'products':Product.objects.all()}
    return render(request,template,context)
