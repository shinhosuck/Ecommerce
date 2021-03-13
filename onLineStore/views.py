from django.shortcuts import render, redirect, get_object_or_404
from onLineStore.models import Product, Order, Customer, ShippingAddress, Purchase
from django.contrib.auth.models import User
from onLineStore.forms import ShippingAddressForm




def store(request):
    user = request.user

    if user.is_authenticated:
        try:
            customer_name = Customer.objects.get(name=user.customer.name)
        except Customer.DoesNotExist:
            products = Product.objects.all()
            context = {
                "products": products,
                "total_items": 0
            }
            return render(request, "onLineStore/store.html", context)

        else:
            customer = Customer.objects.get(name=user)
            purchases = customer.purchase_set.all()

            totalItems = 0
            for purchase in purchases:
                totalItems += purchase.quantity
            customer.quantity_ordered = totalItems
            customer.save()

        products = Product.objects.all()
        context = {
            "products": products,
        }
        return render(request, "onLineStore/store.html", context)

    else:
        products = Product.objects.all()
        context = {
            "products": products,
        }
    return render(request, "onLineStore/store.html", context)


def add_to_cart(request, pk):
    user = request.user

    if user.is_authenticated:
        try:
            current_user = Customer.objects.get(name=user)
        except Customer.DoesNotExist:
            Customer.objects.create(name=user, email=user.email)

        customer_name = Customer.objects.get(name=user.customer.name)
        product = get_object_or_404(Product, pk=pk)
        purchases = customer_name.purchase_set.all()
        purchase = purchases.first()
        counter = 0

        for purchase in purchases:
            if purchase.product.id == product.id:
                counter += 1
                purchase.quantity += 1
                purchase.save()
        if counter == 0:
            Purchase.objects.create(
                customer=customer_name,
                product=product,
                quantity=1,
                price=product.price,
            )

        user.customer.quantity_ordered += 1
        user.customer.save()
        return redirect("onLineStore:home")

    else:
        return redirect("onLineStore:home")


def cart(request):
    user = request.user

    if user.is_authenticated:

        # when if customer account has not yet been created.
        try:
            current_user = Customer.objects.get(name=user)
        except Customer.DoesNotExist:
            context = {
                "total_items": 0,
                "amount_due": 0
            }
            return render(request, "onLineStore/cart.html", context)
         #end
        else:
            current_user = Customer.objects.get(name=user)
            purchases = current_user.purchase_set.all()

            total_items = 0
            amount_due = 0
            total = {}

            for purchase in purchases:
                total_items += purchase.quantity
                amount_due += purchase.quantity * purchase.product.price
                total[purchase] = purchase.product.price * purchase.quantity

            user.customer.quantity_ordered = total_items

            context = {
                "total": total,
                "amount_due": amount_due,
                "totalItems": total_items
            }
            return render(request, "onLineStore/cart.html", context)
    else:
        context = {
            "total_items": 0,
            "amount_due": 0
        }
    return render(request, "onLineStore/cart.html", context)


def delete_item(request, pk):
    user = request.user
    item = user.customer.purchase_set.get(pk=pk)
    item.quantity = item.quantity - 1
    if item.quantity <= 0:
        item.delete()
    else:
        item.save()

    current_user = Customer.objects.get(name=user)
    purchases = current_user.purchase_set.all()
    total_items = 0

    for purchase in purchases:
        total_items += purchase.quantity

    current_user.quantity_ordered = total_items
    current_user.save()

    return redirect("onLineStore:cart")


def add_item(request, pk):
    user = request.user
    item = user.customer.purchase_set.get(pk=pk)
    item.quantity = item.quantity + 1
    item.save()

    current_user = Customer.objects.get(name=user)
    purchases = current_user.purchase_set.all()
    total_items = 0

    for purchase in purchases:
        total_items += purchase.quantity

    current_user.quantity_ordered = total_items
    current_user.save()

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

                total_amount = 0
                purchases = user.customer.purchase_set.all()
                for item in purchases:
                    total_amount += item.quantity * item.product.price
                shipping_address = user.customer.shippingaddress_set.last()
                order = Order.objects.create(shipping_address=shipping_address, total=total_amount)
                for item in purchases:
                    order.purchase.add(item)
                # create Order class
            return render(request, "onLineStore/payment.html", {})

        else:
            # when if customer account has not yet been created.
            try:
                current_user = Customer.objects.get(name=user)
            except Customer.DoesNotExist:
                context = {
                    "totalItems": 0,
                    "amount_due": 0
                }
                return render(request, "onLineStore/check_out.html", context)
            # end
            else:
                customer = get_object_or_404(Customer, name=user)
                orders = customer.purchase_set.all()
                total_items = 0
                amount_due = 0

                if not orders:
                    context = {
                        "totalItems": total_items,
                        "amount_due": amount_due
                    }
                    return render(request, "onLineStore/cart.html", context)

                else:
                    for purchase in orders:
                        total_items += purchase.quantity
                        amount_due += purchase.quantity * purchase.product.price

                    user.customer.quantity_ordered = total_items
                    user.customer.save()

                    form = ShippingAddressForm()
                    context = {
                        "orders": orders,
                        "amount_due": amount_due,
                        "form": form,
                        "totalItems": total_items
                    }
                return render(request, "onLineStore/check_out.html", context)
    else:
        context = {
            "totalItems": 0,
            "amount_due": 0,
        }
    return render(request, "onLineStore/cart.html", context)

