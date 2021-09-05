from .serializers import CartSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cart

class CartCreateAPIview(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class ItemDetailsAPIview(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
# Create your views here.
