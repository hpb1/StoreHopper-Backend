from rest_framework import serializers
from .models import ItemRequest

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRequest
        fields = '__all__'