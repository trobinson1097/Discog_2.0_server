from django.db import models
from django.contrib.auth.models import User


class UserDiscog(models.Model):

    disc_user = models.ForeignKey(User, on_delete=models.CASCADE)
    discog = models.ForeignKey("Discog", on_delete=models.CASCADE)
