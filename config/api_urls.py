from rest_framework import routers
from django.urls import path, include
from olympic.views import AthleteViewSet, GameViewSet

router = routers.DefaultRouter()
router.register("athletes", AthleteViewSet)
router.register("games", GameViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls")),
]
