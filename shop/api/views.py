from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from shop.models import Products,Category
from blog.models import News
from shop.api.serializer import GETNewsSerializer, POSTNewsSerializer, POSTProductsSerializer,  ProductsSerializer, SubscribeSerializer


class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        
        # serializer = ProductsSerializer(products,many = True)
        serializer = ProductsSerializer(products, many = True, context={ 'requset':request })
        return Response(data=serializer.data)
    

    def post(self, request, *args, **kwargs):
        serializer = POSTProductsSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):

    def get(self, request, id, *args, **kwargs):
       
        try:
            product = Products.objects.get(id=id)
            serializer = ProductsSerializer(product)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        product = Products.objects.filter(id=kwargs['id']).first()

        if not product:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductsSerializer(data=request.data, instance=product, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsAPIView(APIView):

    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = GETNewsSerializer(news, many=True, context=({'requset':request}))
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = POSTNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        product = Products.objects.filter(id=kwargs['id']).first()
        if not product:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NewsDetailAPIView(APIView):
    
    def get(self, request, id, *args, **kwargs):
        try:
            post = News.objects.get(id=id)
            serializer = GETNewsSerializer(post)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            blog = News.objects.get(id=kwargs['id'])
            serializer = POSTNewsSerializer(data=request.data, instance=blog, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            blog = News.objects.get(id=id)
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except News.DoesNotExist:
                return Response({'error': 'id is invalid'}, status=status.HTTP_400_BAD_REQUEST)

class SubscribeAPIViev(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SubscribeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

