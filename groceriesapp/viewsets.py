from rest_framework import viewsets
from . import models
from . import serializers
from .models import  GroceryItem
from .serializers import GroceryItemSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter


### Less no. of code with the help of generic views.


class GroceriesViewPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3      ###pagination on the basis of no. of items

class GroceryItemViewset(viewsets.ModelViewSet):
    queryset = models.GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer
    filter_backends = (DjangoFilterBackend , SearchFilter , OrderingFilter)
    filter_fields = ['price']
    search_fields = ['title', 'description']
    pagination_class = GroceriesViewPagination
    ordering_fields = ['price', 'createdAt']




