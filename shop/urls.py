from django.urls import path
from shop import views



urlpatterns =[
    path('shops', views.shops, name='shops'),
    path("shops/<int:id>", views.shop),
    
]




















