from django.shortcuts import render
from .models import product, settings, homepage,blog,advertisement

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

# def product(request):
#     return render(request, 'shop.html')

def index(request):
    my_homepage = homepage.objects.first()
    my_settings = settings.objects.first()
    my_advertisement =advertisement.objects.all()    
    my_product = product.objects.all()
    my_blog = blog.objects.all()
    context = {
        'homepage': my_homepage,
        'settings': my_settings,
        'advertisement': my_advertisement,
        'product': my_product,
        'blog': my_blog
    }
    return render(request , 'index.html', context)

# def products(request):  
#     products = products.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request , 'detail.html', context)
