from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def products_view(request):
    """ see all products """
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)


@api_view(['GET'])
def product_view(request, pk):
    """ see only one product """
    if not pk:
        return Response({"error": "Method PUT not allowed"})
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    """ Create Product """
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def buy_product(request):
    """ Buy product (name, inStock) """
    try:
        product = Product.objects.get(name=request.data['name'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        product.inStock = product.inStock - request.data['inStock']
        if product.inStock > 0:
            product.save()
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        return Response({"error": "There is not enough quantity in the database, enter less quantity"})


@api_view(['POST'])
def edit_product(request):
    """ edit project, search project by name and change it (except name )"""
    try:
        product = Product.objects.get(name=request.data['name'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_product(request):
    """ delete project """
    try:
        product = Product.objects.get(name=request.data['name'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data['name'])
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""

"""


@csrf_exempt
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


"""

"""


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""

"""


@csrf_exempt
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


"""
