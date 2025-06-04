from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from discogapi.models import DiscogGenre
from discogapi.serializers import DiscogGenreSerializer

class DiscogGenreViewSet(viewsets.ModelViewSet):
    queryset = DiscogGenre.objects.all()
    serializer_class = DiscogGenreSerializer
    permission_classes = [IsAuthenticated]