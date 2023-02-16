from django.shortcuts import render
from .models import  Products,category
# Create your views here.


def shops(request):
    products = Products.objects.all()
    my_category = category.objects.all()

    context = {
        'products':products,
        'category': my_category
    }
    return render(request , 'shop.html', context)



def shop(request, id):
    products = Products.objects.get(id=id)

    context = {
        'products': products
    }

    return render(request, "detail.html", context)






