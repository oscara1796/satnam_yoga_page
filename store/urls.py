from django.urls import path
from . import views as store_views


urlpatterns = [
    path('store/', store_views.store, name="store"),
    path('store/cart/', store_views.cart, name="cart"),
    path('store/checkout/', store_views.checkout, name="checkout"),
]
