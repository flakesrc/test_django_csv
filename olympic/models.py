from django.db import models
from django.utils.translation import gettext_lazy as _


class Athlete(models.Model):
    name = models.CharField(max_length=199)
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
    athlete = models.ManyToManyField(Athlete)

    name = models.CharField(max_length=201)
    year = models.IntegerField()
    season = models.CharField(max_length=202)
    city = models.CharField(max_length=203)
    sport = models.CharField(max_length=204)
    event = models.CharField(max_length=205)
    medal = models.CharField(max_length=10, choices=Medal.choices)

    def __str__(self):
        return self.name
