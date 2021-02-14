from rest_framework import serializers
from .models import Athlete, Game


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ["url", "name", "sex", "age", "height", "weight", "team", "noc"]
