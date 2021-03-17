from django.shortcuts import render, redirect
from store.models import Customer
from users.models import Profile

def home(request):
    user = request.user
    if user.is_authenticated:
        new_info = Profile.objects.get(user=user)
        new_info.first_name = user.first_name
        new_info.last_name = user.last_name
        new_info.email = user.email
        new_info.save()
        return render(request, "store/home.html", {})
    else:
        return render(request, "store/home.html", {})



