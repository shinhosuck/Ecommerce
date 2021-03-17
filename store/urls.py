from django.urls import path
from store.views import home

app_name = "store"


urlpatterns = [
    path("", home, name="home"),
]
