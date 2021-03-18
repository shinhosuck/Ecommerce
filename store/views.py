from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from store.models import Product, Basket, Customer
from users.models import Profile



def home(request):
    products = Product.objects.all()
    user = request.user
    if user.is_authenticated:
        new_info = Profile.objects.get(user=user)
        new_info.first_name = user.first_name
        new_info.last_name = user.last_name
        new_info.email = user.email
        new_info.save()

        # customer = get_object_or_404(Customer, name=user)
        # products = customer.basket_set.all()
        # totalItems = 0
        # for product in products:
        #     totalItems += product.quantity
        # customer.total_items = totalItems
        # customer.save()
        return render(request, "store/home.html", {"products": products})
    else:
        return render(request, "store/home.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})


@login_required
def add_to_basket(request, pk):
    user = request.user
    if user.is_authenticated:
        try:
            customer = Customer.objects.get(name=user)
            products = customer.basket_set.all()
            product = get_object_or_404(Product, pk=pk)
            count = 0
            for item in products:
                if item.product.product_name == product.product_name:
                    count += 1
                    item.quantity += 1
                    item.save()
            if count == 0:
                Basket.objects.create(customer=customer, product=product, quantity=1)

        except Customer.DoesNotExist:
            Customer.objects.create(name=user, first_name=user.first_name, 
                        last_name=user.last_name, email=user.email)
        return redirect("store:home")
    else:
        return redirect("store:home")
