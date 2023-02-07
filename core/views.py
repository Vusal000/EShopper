from django.shortcuts import render, redirect
from .models import   settings, homepage, blog, advertisement
from core.forms import ContactForm, SubscriberForm
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
    my_settings = settings.objects.first()
    my_advertisement =advertisement.objects.all()    
    my_blog = blog.objects.all()

    subscribe_form = SubscriberForm()
    if request.method == 'POST':
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_form = SubscriberForm()
    context = {
        'settings': my_settings,
        'advertisement': my_advertisement,
        'blog': my_blog,
        'homepage': my_homepage,
        'subscribe_form' : subscribe_form,
    }
    return render(request , 'index.html', context)


