"""View module for handling requests about tags"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from discogapi.models import Genre


class GenreView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            disc_genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(disc_genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        tags = Genre.objects.all()
        serializer = GenreSerializer(tags, many=True)
        return Response(serializer.data)

class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Genre
        fields = ('id', 'name')

