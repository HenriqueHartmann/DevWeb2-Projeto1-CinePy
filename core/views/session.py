from rest_framework.viewsets import ModelViewSet
from core.models import Session
from core.serializers import SessionSerializer


class SessionViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
