from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from store.models import Product

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)

    sort_by = request.GET.get('sort_by', '')
    if sort_by:
        products = sort(products, sort_by)

    products_list = list(products)

    return render(request, 'store/search.html', context={'products': products_list, 'query': query})

def sort(products, sort_by):
    if sort_by == 'name':
        return products.order_by('name')
    elif sort_by == 'low_to_high':
        return products.order_by('price')
    elif sort_by == 'high_to_low':
        return products.order_by('-price')

def catalog(request):
    query = request.GET.get('q', '')

    products = Product.objects.all()

    sort_by = request.GET.get('sort_by', '')
    if sort_by:
        products = sort(products, sort_by)

    products_list = list(products)

    return render(request, 'store/catalog.html', context={'products': products_list, 'query': query})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={'product': product})
