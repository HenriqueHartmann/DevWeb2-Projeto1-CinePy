from rest_framework.viewsets import ModelViewSet
from core.models import Movie
from core.serializers import MovieSerializer, MovieDetailSerializer


class MovieViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Movie.objects.all()
    # serializer_class = MovieSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return MovieDetailSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer
