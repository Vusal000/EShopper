from django.urls import path

from .views import(
    ProductAPIView,NewsAPIView,ProductDetailAPIView, SubscribeAPIViev
)

urlpatterns =[
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<int:id>', ProductDetailAPIView.as_view(), name='products'),
    path('news/', NewsAPIView.as_view(), name='news'),
    path('subscribe/', SubscribeAPIViev.as_view(), name='subscribe'),
]