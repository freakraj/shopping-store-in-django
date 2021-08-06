from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

CATEGORY_CHOICES = (
 ('M', 'Mobile'),
 ('L', 'Laptop'),
 ('TW', 'Top Wear'),
 ('BW', 'Bottom Wear'),
)
        
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)



    







    


        
 
