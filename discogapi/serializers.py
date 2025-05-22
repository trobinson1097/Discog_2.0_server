from rest_framework import serializers
from discogapi.models import DiscUser, DiscogGenre, Discog, Genre, UserDiscog

class DiscUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscUser
        fields = '__all__'

class DiscogGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscogGenre
        fields = '__all__'

class DiscogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discog
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class UserDiscogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDiscog
        fields = '__all__'