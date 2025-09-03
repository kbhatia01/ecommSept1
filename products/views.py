
# Create your views here.


from django.http import JsonResponse

from products.models import Product


def HelloView(request):
    print(request.headers)
    return JsonResponse({'hello': 'NAME'})


def HelloName(request, username):
    p = Product.objects.all()
    print(p[1].__dict__)
    return JsonResponse({'hello': username})