from django.contrib import admin
from store.models import Address, Category, Product, SubCategory, Basket, Customer


admin.site.register(Address)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Customer)

