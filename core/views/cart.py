from rest_framework.viewsets import ModelViewSet
from core.models import Cart
from core.serializers import CartSerializer


class CartViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
