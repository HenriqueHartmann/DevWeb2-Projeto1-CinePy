from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Director
from core.serializers import DirectorSerializer


class DirectorViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
