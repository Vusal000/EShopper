from django.urls import path
from core import views

urlpatterns =[
    path('', views.home, name='home'),
    path('contact/', views.contact_form, name='contact'),
    path ('search', views.shop_search, name= 'search'),
    # path('news/', views.news, name='news'),
    # path("products/<int:id>", views.products, name='products'),
]

