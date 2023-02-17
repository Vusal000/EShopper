from rest_framework import serializers
from shop.models import  category,Products

from core.models import  News, subscribe


class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = (
            'id',
            'title',
            'description',
            'image',
            # 'price',
        )

class POSTProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = (
            'id',
            'title',
            'description',
            'image',
            'price',
        )

 
class GETNewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'image',
        )
 

class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = subscribe
        fields = (
            'email',
        )


















































