from rest_framework import serializers
from .models import Athlete, Game


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ["-id"]
        model = Athlete
        fields = ["url", "id", "name", "sex", "age", "height", "weight", "team", "noc"]


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        ordering = ["-id"]
        model = Game
        fields = [
            "url",
            "name",
            "year",
            "season",
            "city",
            "sport",
            "event",
            "medal",
            "athlete",
        ]
        depth = 1
