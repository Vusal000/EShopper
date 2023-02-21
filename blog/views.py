from django.shortcuts import render

from blog.models import News

# Create your views here.

def new(request, pk):
    news = News.objects.get(pk=pk)

    context = {
        'news': news
    }
    return render(request , 'new.html', context)






def news(request):
    news = News.objects.all()

    context = {
        'news': news
    }

    return render(request, "news.html", context)




