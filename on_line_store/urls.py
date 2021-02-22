from django.urls import path
from on_line_store.views import store, cart, check_out



name = "on_line_store"

urlpatterns = [
    path("", store, name="on_line_store-home"),
    path("cart/", cart, name="on_line_store-cart"),
    path("check_out/", check_out, name="on_line_store-check_out")
]