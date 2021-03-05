from django.urls import path
from onLineStore.views import (
                            store,
                            cart,
                            check_out,
                            add_to_cart,
                            delete_item,
                            add_item,
                        )




app_name = "onLineStore"



urlpatterns = [
    path("", store, name="home"),
    path("cart/", cart, name="cart"),
    path("check_out/", check_out, name="check_out"),
    path("add_to_cart/<int:id>/", add_to_cart, name="add_to_cart"),
    path("delete_item/<int:pk>/", delete_item, name="delete_item"),
    path("add_item/<int:pk>/", add_item, name="add_item"),
]
