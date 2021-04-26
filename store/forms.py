from store.models import Address, ProductReview
from django import forms 


class OrderAddressForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    
    class Meta:
        model = Address
        fields = [
            "first_name", 
            "last_name",
            "email",
            "address",
            "city",
            "state",
            "postal_code",
            "country" 
        ]

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            "review_title",
            "content",
        ]