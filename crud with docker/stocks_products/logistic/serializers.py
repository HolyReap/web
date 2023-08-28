from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','stocks']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product','quantity','price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id','address','positions','products']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(
                stock = stock, #**positions
                product = position.get('product'),
                quantity = position.get('quantity'),
                price = position.get('price')
            )
            
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(
                stock = stock,
                product = position.get('product'),
                defaults={
                    'quantity':position.get('quantity'),
                    'price':position.get('price')
                }
            )

        return stock
