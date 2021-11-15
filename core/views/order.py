from rest_framework.viewsets import ModelViewSet
from core.models import Order
from core.serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Order.objects.all()
    #serializer_class = OrderSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return OrderDetailSerializer
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer
