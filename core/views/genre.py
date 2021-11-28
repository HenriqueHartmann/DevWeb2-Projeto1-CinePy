from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Genre
from core.serializers import GenreSerializer


class GenreViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
