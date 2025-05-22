from django.contrib import admin
from discogapi.models import DiscUser, DiscogGenre, Discog, Genre, UserDiscog

admin.site.register(DiscUser)
admin.site.register(DiscogGenre)
admin.site.register(Discog)
admin.site.register(Genre)
admin.site.register(UserDiscog)
