from django.db import models


class Discog(models.Model):

    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    paid = models.IntegerField()
    image = models.URLField(max_length=200)
    genres = models.ManyToManyField("Genre", through="DiscogGenre", related_name="discogs")
    user_discog = models.ManyToManyField("DiscUser", through="UserDiscog", related_name="discogs")

    @property
    def collected(self):
        return self.__collected

    @collected.setter
    def collected(self, value):
        self.__collected = value