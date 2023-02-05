from django.shortcuts import render
from .models import   settings, homepage, blog, advertisement
from core.forms import ContactForm, SubscriberForm
# Create your views here.


def contact_form(request):
    contact_model = ContactForm()
    if request.method == 'POST':
        contact_model = ContactForm(request.POST)
        if contact_model.is_valid():
            contact_model.save()
            contact_model = ContactForm()
            
    context = {
        'contact_model': contact_model
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
