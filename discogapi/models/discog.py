from django.db import models


class Discog(models.Model):

    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    paid = models.IntegerField(max_length=50)