from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from discogapi.models import Discog
from discogapi.serializers import DiscogSerializer
from rest_framework import serializers, status
from rest_framework.response import Response


class DiscogViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single discog

        Returns:
            Response -- JSON serialized discog
        """
        try:
            discog = Discog.objects.get(pk=pk)
            serializer = DiscogSerializer(discog)
            return Response(serializer.data)
        except Discog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all discogs

        Returns:
            Response -- JSON serialized list of discogs
        """
        discogs = Discog.objects.all()
        serializer = DiscogSerializer(discogs, many=True)
        return Response(serializer.data)
