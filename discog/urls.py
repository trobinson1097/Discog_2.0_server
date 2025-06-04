from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from discogapi.views import register_user, login_user, DiscogView, GenreView
from discogapi.views.disc_user import DiscUserView

router = routers.DefaultRouter(trailing_slash=False) 
# ^ tells the router to accept /gametypes instead of /gametypes/
router.register(r'discogs', DiscogView, 'discog')
router.register(r'genres', GenreView, 'genre')
router.register(r'discusers', DiscUserView, 'discuser')



urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('', include('levelupreports.urls')),

]



