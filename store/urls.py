from django.urls import path
from store.views import (
        home, 
        category,
        sub_category,
        product_detail, 
        add_to_basket, 
        my_basket,
        add_item,
        delete_item,
        shipping_address,
        shop_by_brand,
        brand_name,
        my_orders,
        paypal_payment,
        delete_basket,
        order_complete,
        product_review,
        read_review,
    )

app_name = "store"


urlpatterns = [
    path("", home, name="home"),
    path("product/<int:pk>/category/", category, name="category"),
    path("product/<int:pk>/sub_category/", sub_category, name="sub_category"),
    path("shop_by_brand/", shop_by_brand, name="shop_by_brand"),
    path("brand_name/<int:pk>/", brand_name, name="brand_name"),
    path("product/<int:pk>/detail/", product_detail, name="product_detail"),
    path("product/<int:pk>/add_to_basket/", add_to_basket, name="add_to_basket"),
    path("my_basket/", my_basket, name="my_basket"),
    path("add/item/<int:pk>/", add_item, name="add_item"),
    path("delete/item/<int:pk>/", delete_item, name="delete_item"),
    path("delete/basket/<int:pk>/", delete_basket, name="delete_basket"),
    path("shipping_address/",shipping_address, name="shipping_address"),
    path("my_orders/", my_orders, name="my_orders"),
    path("paypal_payment/", paypal_payment, name="paypal_payment"),
    path("order_complete/", order_complete, name="order_complete"),
    path("product_review/<int:pk>/", product_review, name="product_review"),
    path("read/<int:pk>/review", read_review, name="read_review"),
]
