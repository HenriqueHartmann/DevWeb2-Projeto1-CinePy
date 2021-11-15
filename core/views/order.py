from rest_framework.viewsets import ModelViewSet
from core.models import Order
from core.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
