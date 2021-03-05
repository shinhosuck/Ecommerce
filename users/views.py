from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserRegisterForm
from django.contrib import messages
from onLineStore.models import Customer
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or none)
        if form.is_valid():
            form.save()
        return redirect("users:login")
    else:
        form = form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "users/profile.html", {"user": user})
    else:
        message = "You must be logged in to view your profile"
    return render(request, "users/profile.html", {"message": message})
