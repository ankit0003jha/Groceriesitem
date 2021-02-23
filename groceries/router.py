from groceriesapp.viewsets import GroceryItemViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('GroceryItem', GroceryItemViewset)