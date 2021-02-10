from django.db import models
from django.utils.translation import gettext_lazy as _


class Athlete(models.Model):
    name = models.CharField(max_length=80)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=80)
    noc = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Game(models.Model):
    class Medal(models.TextChoices):

        NA = "NA", _("None")
        BRONZE = "Bronze", _("Bronze")
        SILVER = "Silver", _("Silver")
        GOLD = "Gold", _("Gold")

    athlete = models.ManyToManyField(Athlete)
    team = models.ManyToManyField(Team)

    year = models.IntegerField()
    season = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    sport = models.CharField(max_length=80)
    event = models.CharField(max_length=80)
    medal = models.IntegerField(choices=Medal.choices)

    def __str__(self):
        return self.season
