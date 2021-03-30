from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Items(models.Model):
    class ItemType(models.TextChoices):
        DRAFTERS = 'DRAFTERS',_('Drafters')
        BOOKS = 'BOOKS',_('Books')
        CYCLES = 'CYCLES',_('Cycles')
        OTHER = 'OTHER',_('Other')
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=10,
                                 choices=ItemType.choices,
                                 default=ItemType.OTHER,
                                )
    item_details = models.TextField()
    item_price = models.FloatField(default=0.00)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)
    def __str__(self): 
        return self.item_name 

class ItemsCart(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.item_id.item_name
