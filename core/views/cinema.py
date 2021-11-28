from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Cinema
from core.serializers import CinemaSerializer


class CinemaViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
