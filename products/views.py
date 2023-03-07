import requests.utils
from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductListDetailDestroyAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView,
                                      GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductListDetail(generics.ListAPIView, generics.RetrieveAPIView, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BuyProduct(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(name=request.data['name'])
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.inStock = product.inStock - request.data['inStock']
        if product.inStock > 0:
            product.save()
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response({"error": "There is not enough quantity in the database, enter less quantity"})


