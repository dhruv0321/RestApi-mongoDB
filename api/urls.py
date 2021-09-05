from django.urls import path,include
from django.utils.regex_helper import normalize

from .views import CartCreateAPIview,ItemDetailsAPIview

urlpatterns = [
    path('cart/', CartCreateAPIview.as_view(), name='API-CART-LIST'),
    path('cart/<pk>', ItemDetailsAPIview.as_view(), name='api-cart-details'),
]