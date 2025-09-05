from django.urls import path

from products import views
from products.views import createProduct

urlpatterns = [
    path("hello/", views.HelloView),
    path("hello/<slug:username>", views.HelloName),
    path('createProduct/', createProduct)
]