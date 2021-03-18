from django.contrib import admin
from store.models import Customer, Category, Product, SubCategory


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)

