from django.urls import path

from .views import(
    ProductAPIView,NewsAPIView,ProductDetailAPIView
)

urlpatterns =[
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<int:id>', ProductDetailAPIView.as_view(), name='products'),
    path('news/', NewsAPIView.as_view(), name='products'),
]