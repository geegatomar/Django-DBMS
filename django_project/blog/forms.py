from django import forms
from .models import Items

class ItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = [
            "item_name",
            "item_type",
            "item_details",
            "item_price",
            "date_posted",
            "author",
        ]