from django.contrib import admin
from store.models import (
        ProductReview,
        Address, 
        Product, 
        Basket, 
        Customer, 
        Order
    )


admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductReview)

