from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import GroceryItemSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
import json

from groceriesapp.models import GroceryItem

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


  
### if we dont want to write this much code with the help of function based view or class based view we can simply make use of generic views. That i have 
### used in viewset.py 



@api_view(['GET', 'POST', 'DELETE'])
def Grocery_list(request):
    if request.method == 'GET':
        Grocerys = GroceryItem.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            Grocerys = Grocerys.filter(title__icontains=title)
        
        GroceryItem_serializer = GroceryItemSerializer(Grocerys, many=True)
        return JsonResponse(GroceryItem_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        groceryItem_data = JSONParser().parse(request)
        GroceryItem_serializer = GroceryItemSerializer(data=GroceryItem_data)
        if GroceryItem_serializer.is_valid():
            GroceryItem_serializer.save()
            return JsonResponse(GroceryItem_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(GroceryItem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        grocery = GroceryItem.objects.all().delete()
        return JsonResponse({'message': '{} Groceryitem were deleted successfully!'.format(grocery[0])}, status=status.HTTP_204_NO_CONTENT)
