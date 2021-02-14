from rest_framework import viewsets
from .models import Athlete, Game
from .serializers import AthleteSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
