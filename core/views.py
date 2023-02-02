from django.shortcuts import render
from .models import  settings, homepage, blog, advertisement, subscribe

# Create your views here.


def contact(request):

    return render(request, 'contact.html')

# def my_index(request):
#     return render(request, 'index.html')


def home(request):
    my_homepage = homepage.objects.first()
    my_settings = settings.objects.first()
    my_advertisement =advertisement.objects.all()    
    my_blog = blog.objects.all()
    subscribes = subscribe.objects.all()
    context = {
        'settings': my_settings,
        'subscibers': subscribes,
        'advertisement': my_advertisement,
        'blog': my_blog,
        'homepage': my_homepage
    }
    return render(request , 'index.html', context)
