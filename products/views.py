import json
# Create your views here.


from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.create_product_serializer import createProductSerializer
from products.models import Product


def HelloView(request):
    print(request.headers)
    return JsonResponse({'hello': 'NAME'})


def HelloName(request, username):
    p = Product.objects.all()
    print(p[1].__dict__)
    return JsonResponse({'hello': username})

@api_view(['POST'])
def createProduct(request):
    serlizedData = createProductSerializer(data=request.data)
    print("a", serlizedData)
    if serlizedData.is_valid():
        prod = serlizedData.save()
        return Response(createProductSerializer(prod).data, status=status.HTTP_201_CREATED)

    return JsonResponse({'Error': serlizedData.errors})
