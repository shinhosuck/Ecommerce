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


def side_categories(request):
    # for base.html side categories
    products = Product.objects.all()
    categories = {}
    new_products = {}

    for product in products:
        categories.setdefault(product.category, product.id)
        new_products.setdefault(product.sub_category, product)
    context = {
        "categories": categories,
        "new_products": new_products
    }
    return  context