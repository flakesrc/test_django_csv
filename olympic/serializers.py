from rest_framework import serializers
from .models import Athlete, Game


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ["name", "sex", "age", "height", "weight", "team", "noc"]
