from django.http import HttpResponse

from .models import Products


def index(request):
    latest_products_list = Products.objects.order_by('-created_at')[:5]
    print(f'latest_products_list: {latest_products_list}')
    output = ", ".join([q.name for q in latest_products_list])
    return HttpResponse(output)


def detail(request, product_id):
    return HttpResponse("You're looking at inventario %s." % product_id)


def results(request, product_id):
    response = "You're looking at the results of inventario %s."
    return HttpResponse(response % product_id)
