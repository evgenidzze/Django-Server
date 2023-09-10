from rest_framework import serializers

from orders.models import MenuItem, Category


class VariantFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        print(value.id)
        pass

class CategoryFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return {'id': value.id, 'name': value.name}


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategoryFieldSerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
