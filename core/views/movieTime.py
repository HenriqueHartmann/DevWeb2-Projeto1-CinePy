from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from core.models import MovieTime
from core.serializers import MovieTimeSerializer


class MovieTimeViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = MovieTime.objects.all()
    serializer_class = MovieTimeSerializer
