from django.db import models


class DiscogGenre(models.Model):

    discog = models.ForeignKey("Discog", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
