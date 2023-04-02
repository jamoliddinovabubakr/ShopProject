from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'inStock']


"""
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    category_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    inStock = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.inStock = validated_data.get('inStock', instance.price)
        instance.save()
        return instance

"""
