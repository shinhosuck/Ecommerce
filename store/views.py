from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from store.models import Product, Basket, Customer
from users.models import Profile



def home(request):
    all_products = Product.objects.all()
    user = request.user
    if user.is_authenticated:
        try:
            customer = Customer.objects.get(name=user)
        except Customer.DoesNotExist:
            Customer.objects.create(name=user, first_name=user.first_name, last_name=user.last_name, email=user.email, total_items=0)
            return render(request, "store/home.html", {"all_products": all_products})
        else:
            customer = get_object_or_404(Customer, name=user)
            products = customer.basket_set.all()
            totalItems = 0
            for product in products:
                totalItems += product.quantity
            customer.total_items = totalItems
            customer.save()
        return render(request, "store/home.html", {"all_products": all_products})
    else:
        pass
    return render(request, "store/home.html", {"all_products": all_products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})


@login_required
def add_to_basket(request, pk):
    user = request.user
    customer = Customer.objects.get(name=user)
    product = Product.objects.get(pk=pk)
    baskets = customer.basket_set.all()
    counter = 0
    for basket in baskets:
        if basket.product.product_name == product.product_name:
            counter += 1
            basket.quantity += 1
            customer.total_items +=1
            basket.save()
    if counter == 0:
        Basket.objects.create(customer=customer, product=product, quantity=1)
        customer.total_items +=1
    return redirect("store:home")


@login_required
def my_basket(request, pk):
    user = request.user
    customer = get_object_or_404(Customer, name=user)
    baskets = customer.basket_set.all()
    total_amount_due = 0
    for basket in baskets:
        total_amount_due += basket.quantity * basket.product.price
    context = {
        "total_amount_due": total_amount_due,
        "baskets": baskets
    }
    return render(request, "store/my_basket.html", context)