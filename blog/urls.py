from django.urls import path
from blog import views


urlpatterns =[
    path('news/', views.news, name='news'),
    path("new/<int:pk>", views.new, name='new'),
    
]