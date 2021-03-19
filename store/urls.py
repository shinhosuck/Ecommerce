from django.urls import path
from store.views import home, product_detail, add_to_basket, my_basket

app_name = "store"


urlpatterns = [
    path("", home, name="home"),
    path("product/<int:pk>/detail/", product_detail, name="product_detail"),
    path("product/<int:pk>/add_to_basket/", add_to_basket, name="add_to_basket"),
    path("user/<int:pk>/basket/", my_basket, name="my_basket"),
]
