from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Movie
from core.serializers import MovieSerializer, MovieDetailSerializer


class MovieViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    # serializer_class = MovieSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return MovieDetailSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer
