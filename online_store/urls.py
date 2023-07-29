from django.urls import path, include
from .import views

urlpatterns = [
    path('health', views.health),
    path('login', views.login),
    path('get_buyers', views.get_buyers),
    path('get_sellers', views.get_sellers),
    path('add_sellers', views.add_sellers),
    path('update_product', views.update_product),
    path('delete_product', views.delete_product)
]