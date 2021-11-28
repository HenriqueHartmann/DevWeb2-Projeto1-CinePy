from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import MovieTime
from core.serializers import MovieTimeSerializer


class MovieTimeViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = MovieTime.objects.all()
    serializer_class = MovieTimeSerializer
