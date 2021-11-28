from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Session
from core.serializers import SessionSerializer, SessionDetailSerializer


class SessionViewSet(ModelViewSet):
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    queryset = Session.objects.all()
    # serializer_class = SessionSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return SessionDetailSerializer
        if self.action == "retrieve":
            return SessionDetailSerializer
        return SessionSerializer
