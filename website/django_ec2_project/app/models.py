from django.db import models

PATTERN_CHOICES = [
    ('checkered','checkered'), 
    ('dots','dots'),
    ('floral','floral'),
    ('solid','solid'),
    ('stripes','stripes'),
    ('zigzag','zigzag')
]

ITEM_CHOICES = [
    ('top','top'), 
    ('trouser','trouser'),
    ('pullover','pullover'),
    ('dress','dress'),
    ('coat','coat'),
    ('sandal','sandal'),
    ('shirt','shirt'),
    ('sneaker','sneaker'),
    ('bag','bag'),
    ('ankle boot','ankle boot')
]

# Create your models here.
class Item(models.Model):
    item_image = models.ImageField(upload_to='uploads/')
    
def __str__(self):
     return self.title