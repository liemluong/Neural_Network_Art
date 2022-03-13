from django.db import models

# Item model for user uploaded image
class Item(models.Model):
    item_image = models.ImageField(upload_to='uploads/')
    
def __str__(self):
     return self.title