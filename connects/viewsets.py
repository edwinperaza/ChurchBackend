from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Connect
from .serializers import ConnectSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class ConnectViewSet(viewsets.ModelViewSet):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)