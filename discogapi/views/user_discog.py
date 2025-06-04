from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from discogapi.models import UserDiscog
from discogapi.serializers import UserDiscogSerializer

class UserDiscogViewSet(viewsets.ModelViewSet):
    queryset = UserDiscog.objects.all()
    serializer_class = UserDiscogSerializer
    permission_classes = [IsAuthenticated]