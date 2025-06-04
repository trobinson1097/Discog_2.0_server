"""View module for handling requests about disc_user types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from discogapi.models import Discog, DiscUser, Genre, disc_user
from rest_framework.decorators import action


class DiscUserView(ViewSet):
    """Level up disc_user types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single disc_user type
        Returns:
            Response -- JSON serialized disc_user type
        """
        # db_cursor.execute("""
        # select id, label
        # from levelupapi_gametype
        # where id = ?""",(pk,) 
        # )
        disc_user = DiscUser.objects.get(pk=pk)
        serializer = DiscUserSerializer(disc_user)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all disc_user types

        Returns:
            Response -- JSON serialized list of disc_user types
        """
        # select *
        # from levelupapi_gametype
        disc_user = DiscUser.objects.all()
        serializer = DiscUserSerializer(disc_user, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def usersDiscogs(self, request):
        try:
            disc_user = DiscUser.objects.get(user=request.auth.user)
            serializer = DiscUserSerializer(disc_user)
            return Response(serializer.data)
        except DiscUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class DiscUserSerializer(serializers.ModelSerializer):
    """JSON serializer for discog types
    """
    class Meta:
        model = DiscUser
        fields = ('id', 'bio', 'user', 'discogs')
        depth = 2

