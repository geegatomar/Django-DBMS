from django import forms
from .models import Items, ItemsCart

class ItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = [
            "item_name",
            "item_type",
            "item_details",
            "item_price",
        ]

class ItemsCartForm(forms.ModelForm):

    class Meta:
        model = ItemsCart
        fields = [
        ]