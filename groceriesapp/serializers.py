from rest_framework import serializers
from . import models
from .models import GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = models.GroceryItem
        fields = ['title', 'description', 'createdAt', 'price']
