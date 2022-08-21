from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Category


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products.html', {
        'products': products, 'category': category, 'categories': categories,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product_detail.html', {'product': product})
