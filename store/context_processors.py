from store.models import Product, Customer
from django.shortcuts import get_object_or_404



# context_processor for my_basket.html
# for total_amount_due
def update_basket(request):
    user = request.user
    if user.is_authenticated:
        customer = get_object_or_404(Customer, name=user)
        baskets = customer.basket_set.filter(open_basket=True)
        total_amount_due = 0
        totalItems = 0
        for basket in baskets:
            total_amount_due += basket.quantity * basket.product.price
            totalItems += basket.quantity
        user.customer.total_items = totalItems
        context = {
            "total_amount_due": total_amount_due,
        }
        return context
    else:
        return {}


# for base.html side categories
def side_categories(request):
    products = Product.objects.all()
    categories = {}
    sub_cat = {}

    for product in products:
        categories.setdefault(product.category, product.id)
        sub_cat.setdefault(product.sub_category, product)
    context = {
        "categories": categories,
        "sub_cat": sub_cat
    }
    return  context