from rest_framework.viewsets import ModelViewSet
from core.models import Director
from core.serializers import DirectorSerializer


class DirectorViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
