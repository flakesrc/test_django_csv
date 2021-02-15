from rest_framework import serializers
from .models import Athlete, Game


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ["-id"]
        model = Athlete
        fields = ["url", "id", "name", "sex", "age", "height", "weight", "team", "noc"]


class GameSerializer(serializers.HyperlinkedModelSerializer):
    athlete_qs = Athlete.objects.all()
    athlete = serializers.PrimaryKeyRelatedField(queryset=athlete_qs, many=True)

    class Meta:

        ordering = ["-id"]
        model = Game
        fields = [
            "url",
            "id",
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
