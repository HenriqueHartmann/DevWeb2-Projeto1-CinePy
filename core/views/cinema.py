from rest_framework.viewsets import ModelViewSet
from core.models import Cinema
from core.serializers import CinemaSerializer


class CinemaViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
