from django.urls import path
from core import views

urlpatterns =[
    path('', views.homepage, name='home'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.Subscibers, name='subscribe'),
    path('products/', views.product, name='products'),
]