from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

# creating a table in the database


class Items(models.Model):

    class ItemType(models.TextChoices):
        DRAFTERS = 'DRAFTERS',_('Drafters')
        BOOKS = 'BOOKS',_('Books')
        CYCLES = 'CYCLES',_('Cycles')
        OTHER = 'OTHER',_('Other (Mattress,Mirror,Laundry Baskets/Hangers,etc')
    
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=10,
                                 choices=ItemType.choices,
                                 default=ItemType.OTHER,
                                )
    item_details = models.TextField()
    item_price = models.FloatField(default=0.00)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.item_name 
