from rest_framework.viewsets import ModelViewSet
from core.models import Genre
from core.serializers import GenreSerializer


class GenreViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
