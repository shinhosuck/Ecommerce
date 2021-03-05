from onLineStore.models import ShippingAddress
from django import forms


class ShippingAddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = [
            "first_name",
            "last_name",
            "address",
            "city",
            "state",
            "zipcode"
        ]
