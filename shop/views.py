from django.shortcuts import render
from .models import  Products,category
# Create your views here.


def shop(request):
    products = Products.objects.all()
    my_category = category.objects.all()

    context = {
        'products':products,
        'category': my_category
    }
    return render(request , 'shop.html', context)









