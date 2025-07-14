from rest_framework import serializers
from .models import Needs                                       

class NeedsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = ['id','location', 'title', 'capacity', 'price_min', 'price_max', 'image']

class NeedsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = '__all__'  

class AddNeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = ['title', 'description', 'location', 'capacity', 'price_min', 'price_max', 'category', 'image']
        
class UpdateNeedsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    location = serializers.CharField(max_length=255, required=False)
    capacity = serializers.CharField(required=False)
    price_min = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    price_max = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = serializers.CharField(max_length=100, required=False)
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Needs
        fields = ['title', 'description', 'location', 'capacity', 'price_min', 'price_max', 'category', 'image']
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.price_min = validated_data.get('price_min', instance.price_min)
        instance.price_max = validated_data.get('price_max', instance.price_max)
        instance.category = validated_data.get('category', instance.category)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.save()
        return instance