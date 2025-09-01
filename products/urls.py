from django.urls import path

from products import views

urlpatterns = [
    path("hello/", views.HelloView),
    path("hello/<slug:username>", views.HelloName)
]