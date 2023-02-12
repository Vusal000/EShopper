from core.models import Settings


def header_and_footer(request):
    settings = Settings.objects.first()
    context = {
        "settings": settings
    }
    return context
    
