from onLineStore.models import ShippingAddress
from django import forms


class ShippingAddressForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

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
