from baseuser.models import MyUser
from rest_framework import serializers
from shop.models import  Category,Products
from blog.models import News
from core.models import  subscribe


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

class  AuthorSerializer():
    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
            'bio',
        )




class GETNewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'image',
            'author',
        )


class POSTNewsSerializer(serializers.ModelSerializer):
    
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


















































