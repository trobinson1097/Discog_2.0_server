from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from discogapi.models import Genre
from discogapi.serializers import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]