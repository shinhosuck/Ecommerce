from django.shortcuts import render, redirect, get_object_or_404
from onLineStore.models import Product, Order, Customer, ShippingAddress
from django.contrib.auth.models import User
from onLineStore.forms import ShippingAddressForm




def store(request):
    user = request.user
    if not user.is_authenticated:
        products = Product.objects.all()
        return render(request, "onLineStore/store.html", {"products": products})
    try:
        customer = Customer.objects.get(name=user)
    except:
        customer = Customer.objects.create(name=user, email=user.email)

    current_user = Customer.objects.get(name=user)
    orders = current_user.order_set.all()
    total_items = 0

    for order in orders:
        total_items += order.quantity

    current_user.quantity_ordered = total_items
    current_user.save()

    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "onLineStore/store.html", context)


def add_to_cart(request, id):
    user = request.user
    if user.is_authenticated:
        name = Customer.objects.get(name=user)
        product = get_object_or_404(Product, id=id)
        new_order = Order.objects.create(customer=name, product=product, quantity=1)

        return redirect("onLineStore:home")
    else:
        return redirect("onLineStore:home")


def cart(request):
    user = request.user
    if user.is_authenticated:
        current_user = Customer.objects.get(name=user)
        orders = current_user.order_set.all()

        total_items = 0
        amount_due = 0
        total = {}

        for order in orders:
            total_items += order.quantity
            amount_due += order.quantity * order.product.price
            total[order] = order.product.price * order.quantity

        context = {
            "total": total,
            "total_items": total_items,
            "amount_due": amount_due,
        }
        return render(request, "onLineStore/cart.html", context)
    else:
        context = {
            "total_items": 0,
            "amount_due": 0
        }
    return render(request, "onLineStore/cart.html", context)


def delete_item(request, pk):
    user = request.user.customer
    item = user.order_set.get(pk=pk)
    item.quantity = item.quantity - 1

    if item.quantity <= 0:
        item.delete()
    else:
        item.save()
    return redirect("onLineStore:cart")


def add_item(request, pk):
    user = request.user.customer
    item = user.order_set.get(pk=pk)
    item.quantity = item.quantity + 1
    item.save()
    return redirect("onLineStore:cart")


def check_out(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = ShippingAddressForm(request.POST)
            if form.is_valid():
                customer_name = get_object_or_404(Customer, name=user)
                form.instance.customer = customer_name
                form.save()
                print(customer_name.order_set.all())
            return redirect("onLineStore:check_out")

        else:
            customer = get_object_or_404(Customer, name=user)
            orders = customer.order_set.all()
            total_items = 0
            amount_due = 0

            for order in orders:
                total_items += order.quantity
                amount_due += order.quantity * order.product.price

            form = ShippingAddressForm()
            context = {
                "orders": orders,
                "total_items": total_items,
                "amount_due": amount_due,
                "form": form
            }
            return render(request, "onLineStore/check_out.html", context)
    else:
        total_items = 0
        amount_due = 0
        orders = []
        context = {
            "orders": orders,
            "total_items": total_items,
            "amount_due": amount_due,
        }
        return render(request, "onLineStore/check_out.html", context)


