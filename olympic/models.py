from django.db import models
from django.utils.translation import gettext_lazy as _


class Athlete(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    team = models.CharField(max_length=200)
    noc = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Game(models.Model):
    class Medal(models.TextChoices):
        NA = "NA", _("None")
        BRONZE = "Bronze", _("Bronze")
        SILVER = "Silver", _("Silver")
        GOLD = "Gold", _("Gold")

    athlete_id_ref = models.IntegerField(null=True)
    athlete = models.ManyToManyField(
        to=Athlete, through="GameAthlete", related_name="games"
    )

    name = models.CharField(max_length=200)
    year = models.IntegerField()
    season = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)
    event = models.CharField(max_length=200)
    medal = models.CharField(max_length=10, choices=Medal.choices, null=True)

    def __str__(self):
        return self.name


class GameAthlete(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        db_table = "olympic_game_athlete"
        unique_together = ("athlete", "game")

    def __str__(self):
        return f"{self.athlete} - {self.game}"
