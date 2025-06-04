from django.db import models



class UserDiscog(models.Model):

    disc_user = models.ForeignKey("DiscUser", on_delete=models.CASCADE)
    discog = models.ForeignKey("Discog", on_delete=models.CASCADE)
