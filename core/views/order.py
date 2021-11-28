from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Order
from core.serializers import OrderSerializer, CreateEditOrderSerializer


class OrderViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return OrderSerializer
        return CreateEditOrderSerializer
