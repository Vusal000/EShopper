from django.urls import path
from shop import views



urlpatterns =[
    path('shops', views.shops, name='shops'),
    path("shops/<slug:slug>", views.shop, name='shop'),
    
]




















