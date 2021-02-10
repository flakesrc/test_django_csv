from django.db import models


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
    NA = 0
    BRONZE = 1
    SILVER = 2
    GOLD = 3

    MEDAL_CHOICES = [
        (NA, "NA"),
        (BRONZE, "Bronze"),
        (SILVER, "Silver"),
        (GOLD, "Gold"),
    ]

    athlete = models.ManyToManyField(Athlete)
    team = models.ManyToManyField(Team)

    year = models.IntegerField()
    season = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    sport = models.CharField(max_length=80)
    event = models.CharField(max_length=80)
    medal = models.IntegerField(choices=MEDAL_CHOICES)

    def __str__(self):
        return self.season
