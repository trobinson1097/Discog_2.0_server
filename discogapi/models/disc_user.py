from django.db import models
from django.contrib.auth.models import User


class DiscUser(models.Model):

    full_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)