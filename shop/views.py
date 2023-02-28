from django.shortcuts import render
from .models import  Category, Color, Products, Size
# Create your views here.



def shop(request, slug):
    products = Products.objects.get(slug=slug)

    context = {
        'products': products
    }

    return render(request, "detail.html", context)

# class ProductListView(ListView):
#     model = Products
#     paginate_by = 1
    


def shops(request):
    products = Products.objects.all()
    category = Category.objects.all()

    colors = Color.objects.all()
    if "color" in request.GET.keys():
        print(request.GET["color"])
        products = Products.objects.filter(
            color_id__title=request.GET["color"])
        

    sizes = Size.objects.all()
    if "size" in request.GET.keys():
        print(request.GET["size"])
        products = Products.objects.filter(
            size_id__title=request.GET["size"])    


    categorys = Category.objects.all()
    if "category" in request.GET.keys():
        print(request.GET["category"])
        products = Products.objects.filter(
            category_id__title=request.GET["category"])    

    context = {
        'products':products,
        'category': category,
        'colors':colors,
        'sizes':sizes,
        'categorys': categorys,

        
    }
    return render(request , 'shop.html', context)







