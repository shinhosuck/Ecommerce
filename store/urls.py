from django.urls import path
from store.views import home, register


app_name = "store"


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register")
]
