from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from discogapi.views import DiscUserViewSet, DiscogGenreViewSet, DiscogViewSet, GenreViewSet, UserDiscogViewSet

router = routers.DefaultRouter()
router.register(r'discusers', views.DiscUserViewSet)
router.register(r'discoggenres', views.DiscogGenreViewSet)
router.register(r'discogs', views.DiscogViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'userdiscogs', views.UserDiscogViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
