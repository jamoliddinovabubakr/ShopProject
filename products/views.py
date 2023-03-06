from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductListDetailDestroyAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView,
#                                       GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class ProductListDetail(generics.ListAPIView, generics.RetrieveAPIView, GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
