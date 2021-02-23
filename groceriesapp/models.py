from django.db import models

# Create your models here.


class GroceryItem(models.Model):
    
    ## "id" is autogenrated in django if we don't use of primary key.
   
    title = models.CharField(max_length=30)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)  ##Timestamp
    price = models.IntegerField()
    
    class Meta:  
        db_table = "Grocery_item"

