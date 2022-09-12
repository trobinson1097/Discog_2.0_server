from django.db import models


class UserDiscog(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    discog = models.ForeignKey("Discog", on_delete=models.CASCADE)
