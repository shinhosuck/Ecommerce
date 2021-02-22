from django.shortcuts import render



def store(request):
    context = {}
    return render(request, "on_line_store/store.html", context)


def cart(request):
    context = {}
    return render(request, "on_line_store/cart.html", context)


def check_out(request):
    context = {}
    return render(request, "on_line_store/check_out.html", context)
