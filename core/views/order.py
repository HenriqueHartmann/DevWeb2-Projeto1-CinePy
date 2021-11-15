from rest_framework.viewsets import ModelViewSet
from core.models import Order
from core.serializers import OrderSerializer, CreateEditOrderSerializer


class OrderViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return OrderSerializer
        return CreateEditOrderSerializer
