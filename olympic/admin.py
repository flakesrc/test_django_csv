from django.contrib import admin
from .models import Game, Athlete, GameAthlete


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    fields = ("name", "sex", "age", "height", "weight", "team", "noc")
    list_display = ("name", "sex", "age", "noc")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "year",
        "season",
        "city",
        "sport",
        "event",
        "medal",
        "athlete_id_ref",
    )
    list_display = ("name", "city", "event", "medal")


@admin.register(GameAthlete)
class GameAthleteAdmin(admin.ModelAdmin):
    fields = ("game", "athlete")
