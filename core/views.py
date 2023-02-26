from django.shortcuts import render, redirect

from .models import Settings, homepage
from core.forms import ContactForm, SubscriberForm
from shop.models import Category, Products
# from core.forms import SubscriberForm
from django.http import HttpRequest, HttpResponse

# Create your views here.
from django.db.models.query_utils import Q
from django.db.models import QuerySet, Avg, Q, Count





def contact_form(request: HttpRequest) -> HttpResponse:
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print("test")
        if form.is_valid():
            form.save()
            form = ContactForm()
            
    context = {
        'form': form
    }

    return render(request , 'contact.html', context)



def home(request):
    my_homepage = homepage.objects.first()
    # setting = Settings.objects.all()
    products = Products.objects.all()
    categorys = Category.objects.all()

    subscribe_form = SubscriberForm()
    if request.method == 'POST':
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_form = SubscriberForm()
    context = {
        # 'settings': setting,
        'homepage': my_homepage,
        'products':products[0:3],
        'subscribe_form' : subscribe_form,
        'categorys':categorys,
    }
    return render(request , 'index.html', context)




def search_shop(query) -> QuerySet:
    return Products.objects.filter(title__contains = query)



def shop_search(request):
	
	query = request.GET["query"]

	shops = Products.objects.filter(title__icontains=query)
    

	context = {'shops':shops, }

	return render(request, 'search.html', context)
