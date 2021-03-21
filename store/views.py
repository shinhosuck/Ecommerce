from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product, Basket, Customer, Address, Order
from django.contrib.auth.models import User
from store.forms import OrderAddressForm
from users.models import Profile



def product(request):
    products = Product.objects.all()

    categories = {}
    sub_categories = []
    new_products = []

    for product in products:
        categories.setdefault(product.category, product)
        new_products.append(product)

    for new_product in new_products:
        if new_product.sub_category not in sub_categories:
            sub_categories.append(new_product.sub_category)
        elif new_product.sub_category in sub_categories:
            new_products.remove(new_product)

    context = {
        "categories": categories,
        "new_products": new_products
    }
    return  context


def category(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = product.category
    products = Product.objects.filter(category=category)
    for product in products:
        print(product.sub_category)
    context = {
        "category": category,
        "products": products
    }
    return  render(request, "store/category.html", context)


def sub_category(request, pk):
    return render(request, "store/sub_category.html", {})


def shop_by_brand(request):
    products = Product.objects.all()
    brands = {}
    for product in products:
        brands.setdefault(product.company, product)
    return render(request, "store/shop_by_brand.html", {"brands": brands})


def brand_name(request, pk):
    product = get_object_or_404(Product, pk=pk)
    brand_name = product.company
    products = Product.objects.filter(company=brand_name)
    return render(request, "store/brand_name.html", {"products": products, "brand_name": brand_name})


def home(request):
    all_products = Product.objects.all()
    user = request.user
    if user.is_authenticated:
        try:
            customer = Customer.objects.get(name=user)
        except Customer.DoesNotExist:
            Customer.objects.create(name=user, first_name=user.first_name, 
            last_name=user.last_name, email=user.email, total_items=0)
            return render(request, "store/home.html", {"all_products": all_products})
        else:
            customer = get_object_or_404(Customer, name=user)
            products = customer.basket_set.filter(open_basket=True)
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
    baskets = customer.basket_set.filter(open_basket=True)
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
    baskets = customer.basket_set.filter(open_basket=True)
    total_amount_due = 0
    for basket in baskets:
        total_amount_due += basket.quantity * basket.product.price
    context = {
        "total_amount_due": total_amount_due,
        "baskets": baskets
    }
    return render(request, "store/my_basket.html", context)


@login_required
def add_item(request, pk):
    user = request.user
    customer = get_object_or_404(Customer, name=user)
    basket = customer.basket_set.get(pk=pk)
    basket.quantity +=1
    basket.save()
    # update basket
    baskets = customer.basket_set.filter(open_basket=True)
    total_amount_due = 0
    totalItems = 0
    for basket in baskets:
        total_amount_due += basket.quantity * basket.product.price
        totalItems += basket.quantity
    user.customer.total_items = totalItems
    context = {
        "total_amount_due": total_amount_due,
        "baskets": baskets
    }
    return render(request, "store/my_basket.html", context)


@login_required
def delete_item(request, pk):
    user = request.user
    user = request.user
    customer = get_object_or_404(Customer, name=user)
    basket = customer.basket_set.get(pk=pk)
    if basket.quantity == 1:
        basket.delete()
    else:
        basket.quantity -=1
        basket.save()
    # update basket
    baskets = customer.basket_set.filter(open_basket=True)
    total_amount_due = 0
    totalItems = 0
    for basket in baskets:
        total_amount_due += basket.quantity * basket.product.price
        totalItems += basket.quantity
    user.customer.total_items = totalItems
    context = {
        "total_amount_due": total_amount_due,
        "baskets": baskets
    }
    return render(request, "store/my_basket.html", context)


def shipping_address(request):
    user = request.user
    if request.method == "POST":
        form = OrderAddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            address.customer = Customer.objects.get(name=user)
            address.save()
        # create order
        customer = get_object_or_404(Customer, name=user)
        baskets = customer.basket_set.filter(open_basket=True)
        for basket in baskets:
            Order.objects.create(customer=customer, basket=basket)
            basket.open_basket = False
            basket.save()
        return redirect("store:home")
    else:
        address = Address.objects.filter(customer__name=user).first()
        form = OrderAddressForm(instance=address)
    return render(request, "store/shipping_address.html", {"form": form})
