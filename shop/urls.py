from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="shop"),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("checkout/", views.checkout,name="checkout"),
    path("search/", views.search,name="search"),
    path("tracker/", views.tracker,name="tracker"),
    path("products/<int:myid>", views.productView, name="ProductView")
    
    
]
