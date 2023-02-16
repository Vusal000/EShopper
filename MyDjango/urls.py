"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# media add

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from baseuser.urls import urlpatterns as baseuser_urls
from core.urls import urlpatterns as core_urls
from shop.urls import urlpatterns as shop_urls
from shop.api.urls import urlpatterns as shop_api_urls
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

# translation
urlpatterns += i18n_patterns(
    path('shop/api/', include(shop_api_urls)),
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('', include(shop_urls)),
    path('baseuser/', include(baseuser_urls)),
)

 















































