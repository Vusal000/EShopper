from django.shortcuts import render
from .models import  Category, Products
# Create your views here.



def shop(request, slug):
    products = Products.objects.get(slug=slug)

    context = {
        'products': products
    }

    return render(request, "detail.html", context)






def shops(request):
    products = Products.objects.all()
    category = Category.objects.all()

    context = {
        'products':products,
        'category': category
    }
    return render(request , 'shop.html', context)









