"""View module for handling requests about discog types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from discogapi.models import Discog, DiscUser, Genre
from rest_framework.decorators import action


class DiscogView(ViewSet):
    """Level up discog types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single discog type
        Returns:
            Response -- JSON serialized discog type
        """
        # db_cursor.execute("""
        # select id, label
        # from levelupapi_gametype
        # where id = ?""",(pk,) 
        # )
        discog = Discog.objects.get(pk=pk)
        disc_user = DiscUser.objects.get(user=request.auth.user)
        discog.collected = disc_user in discog.user_discog.all()
        serializer = DiscogSerializer(discog)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all discog types

        Returns:
            Response -- JSON serialized list of discog types
        """
        # select *
        # from levelupapi_gametype
        discogs = Discog.objects.all()
        disc_user = DiscUser.objects.get(user=request.auth.user)
        for discog in discogs: 
            discog.collected = disc_user in discog.user_discog.all()
        serializer = DiscogSerializer(discogs, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized discog instance
        """
        # genres= Genre.objects.get(pk=request.data["genres"])
        # disc_user = DiscUser.objects.get(user=request.auth.user)

        discog = Discog.objects.create(
            artist=request.data["artist"],
            title=request.data["title"],
            condition=request.data["condition"],
            paid=request.data["paid"],
            image=request.data["image"]
        )
        discog.genres.set(request.data["genres"])
        serializer = DiscogSerializer(discog)
        return Response(serializer.data)



    def update(self, request, pk):
        """Handle PUT requests for a discog

        Returns:
            Response -- Empty body with 204 status code
        """

        discog = Discog.objects.get(pk=pk)
        discog.artist = request.data["artist"]
        discog.title = request.data["title"]
        discog.condition = request.data["condition"]
        discog.paid = request.data["paid"]
        discog.image = request.data["image"]
        

        # discog = Game.objects.get(pk=request.data["discog"])
        # discog.discog = discog
        discog.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        discog = Discog.objects.get(pk=pk)
        discog.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def saved(self, request, pk):
        """Post request for a user to sign up for an event"""

        disc_user = DiscUser.objects.get(user=request.auth.user)
        discog = Discog.objects.get(pk=pk)
        discog.user_discog.add(disc_user)
        return Response({'message': 'Discog added'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removed(self, request, pk):
        """Delete request for a user to leave an event"""
        disc_user = DiscUser.objects.get(user=request.auth.user)
        discog = Discog.objects.get(pk=pk)
        discog.user_discog.remove(disc_user)
        return Response({'message': 'Discog Removed'}, status=status.HTTP_204_NO_CONTENT)


class DiscogSerializer(serializers.ModelSerializer):
    """JSON serializer for discog types
    """
    class Meta:
        model = Discog
        fields = ('id', 'artist', 'title', 'condition', 'paid', 'image', 'genres', 'collected')
        depth = 1

