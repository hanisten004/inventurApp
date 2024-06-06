from django import forms
from .models import Location
from .models import KastenProduct
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'target_quantity', 'quantity']  # Hinzufügen von 'quantity' zu den Feldern

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Überprüfen, ob das Produkt bereits existiert
            self.fields['target_quantity'].widget.attrs['readonly'] = True  # Markieren von target_quantity als nicht bearbeitbar


class KastenProductForm(forms.ModelForm):
    class Meta:
        model = KastenProduct
        fields = ['product', 'quantity']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['place', 'floor', 'room', 'adresse', 'country', 'fk_kasten']