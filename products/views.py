
# Create your views here.


from django.http import JsonResponse

def HelloView(request):
    print(request.headers)
    return JsonResponse({'hello': 'NAME'})


def HelloName(request, username):
    return JsonResponse({'hello': username})