from rest_framework.viewsets import ModelViewSet
from core.models import Movie
from core.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
