from django.shortcuts import render, redirect

from .models import homepage, blog
from core.forms import ContactForm
from shop.models import Products
# from core.forms import SubscriberForm
from django.http import HttpRequest, HttpResponse

# Create your views here.


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

# def my_index(request):
#     return render(request, 'index.html')
  

def home(request):
    my_homepage = homepage.objects.first()
    # setting = settings.objects.all()
    my_blog = blog.objects.all()
    products = Products.objects.all()

    # subscribe_form = SubscriberForm()
    # if request.method == 'POST':
        # subscribe_form = SubscriberForm(request.POST)
        # if subscribe_form.is_valid():
        #     subscribe_form.save()
        #     # subscribe_form = SubscriberForm()
    context = {
        # 'settings': setting,
        'blog': my_blog,
        'homepage': my_homepage,
        'products':products[0:3]
        # 'subscribe_form' : subscribe_form,
    }
    return render(request , 'index.html', context)




# def new(request, id):
#     news = News.objects.get(id=id)

#     context = {
#         'news': news
#     }

#     return render(request, "blog_detail.html", context)

# def news(request):
#     news = News.objects.all()
#     context = {
#         'news':news,
#     }
#     return render(request , 'news.html', context)



# def new(request, id):
#     news = News.objects.get(id=id)

#     context = {
#         'news': news
#     }

#     return render(request, "new.html", context)



# def news(request):
#     news = News.objects.all()
    

#     context = {
#         'news':news,
#         'news': news
#     }
#     return render(request , 'news.html', context)

