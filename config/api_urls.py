from rest_framework import routers
from django.urls import path, include
from olympic.views import AthleteViewSet

router = routers.DefaultRouter()
router.register("athletes", AthleteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls")),
]
