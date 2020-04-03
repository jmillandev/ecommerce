from django.forms import ModelForm

from .models import ShippingAddresses

class ShippingAddressesForm(ModelForm):
    class Meta:
        model = ShippingAddresses
        fields = [
            'line1','line2','city','state','country','zip_code', 'reference',
        ]
        labels = {
            'line1': 'Calle 1',
            'line2' : 'Calle 2',
            'city' : 'Ciudad',
            'state': 'Estado',
            'country' : 'Ciudad',
            'zip_code' : 'Codigo Postal',
            'reference' : ' Referencia'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['line1'].widget.attrs.update({
            'class' : 'form-control'
        })
    
        self.fields['line2'].widget.attrs.update({
            'class' : 'form-control'
        })
        self.fields['city'].widget.attrs.update({
            'class' : 'form-control'
        })
        self.fields['state'].widget.attrs.update({
            'class' : 'form-control'
        })
        self.fields['country'].widget.attrs.update({
            'class' : 'form-control'
        })
        self.fields['zip_code'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : '0000'
        })
        self.fields['reference'].widget.attrs.update({
            'class' : 'form-control'
        })