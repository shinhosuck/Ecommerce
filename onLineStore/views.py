from django.shortcuts import render




def store(request):
    return render(request, "onLineStore/store.html", {})


def cart(request):
    return render(request, "onLineStore/cart.html", {})


def check_out(request):
    return render(request, "onLineStore/check_out.html", {})