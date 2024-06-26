from rest_framework import serializers
from .models import Product, Establishment, Location, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'
