from django.urls import path
from on_line_store.views import (
                            store,
                            cart,
                            check_out,
                        )




app_name = "onLineStore"



urlpatterns = [
    path("", store, name="home"),
    path("cart/", cart, name="cart"),
    path("check_out/", check_out, name="check_out")
]
