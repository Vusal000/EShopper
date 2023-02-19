from django.urls import path
from blog import views


urlpatterns =[
    path('news/', views.news, name='news'),
    path("news/<int:id>", views.news, name='new'),
    
]