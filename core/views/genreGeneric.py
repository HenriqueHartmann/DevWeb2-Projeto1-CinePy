from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Genre
from core.serializers import GenreSerializer


class GenreListGeneric(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
