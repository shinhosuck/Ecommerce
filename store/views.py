from django.shortcuts import render, redirect
from store.forms import UserRegisterForm
from store.models import Customer

def home(request):
    return render(request, "store/home.html", {})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("store:home")
    else:
        form = UserRegisterForm(request.POST)
    return render(request, "store/register.html", {"form": form})
