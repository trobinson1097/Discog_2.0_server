from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from discogapi.models import DiscUser
from discogapi.serializers import DiscUserSerializer

class DiscUserViewSet(viewsets.ModelViewSet):
    queryset = DiscUser.objects.all()
    serializer_class = DiscUserSerializer
    permission_classes = [IsAuthenticated]