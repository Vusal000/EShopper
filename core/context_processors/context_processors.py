from core.models import Settings
from shop.models import Category

def header_and_footer(request):
    settings = Settings.objects.first()
    category = Category.objects.all()
    context = {
        "settings": settings,
        "category": category
    }
    return context
    
