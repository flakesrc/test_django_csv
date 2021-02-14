# tempo para finalizar a população no teste local: 0:00:44
import os
import django
import pandas as pd
from datetime import datetime
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
django.setup()

from olympic.models import Game, Athlete, GameAthlete


def normalize_na(value):
    na_values = ["nan", "NaN", "NA"]

    return None if str(value) in na_values else value


def populate():
    athlete_list = pd.read_csv("assets/athlete_events.csv")

    df = pd.DataFrame(
        athlete_list,
        columns=[
            "ID",
            "Name",
            "Sex",
            "Age",
            "Height",
            "Weight",
            "Team",
            "NOC",
            "Games",
            "Year",
            "Season",
            "City",
            "Sport",
            "Event",
            "Medal",
        ],
    )

    athlete_objs = []
    game_objs = []

    for row in df.itertuples():

        athlete_instance = Athlete(
            athlete_id_ref=row.ID,
            name=row.Name,
            sex=row.Sex,
            age=normalize_na(row.Age),
            height=normalize_na(row.Height),
            weight=normalize_na(row.Weight),
            team=row.Team,
            noc=row.NOC,
        )
        athlete_objs.append(athlete_instance)

        game_instance = Game(
            athlete_id_ref=row.ID,
            name=row.Games,
            year=row.Year,
            season=row.Season,
            city=row.City,
            sport=row.Sport,
            event=row.Event,
            medal=normalize_na(row.Medal),
        )
        game_objs.append(game_instance)

    # adiciona as instancias no banco de dados
    # ignore_conflicts ativado para não haver erro
    # se o registro já existir, caso o script seja
    # interrompido e executado posteriormente
    print("Adicionando instâncias Athlete...")
    Athlete.objects.bulk_create(athlete_objs, ignore_conflicts=True)

    print("Adicionando instâncias Game...")
    Game.objects.bulk_create(game_objs, ignore_conflicts=True)

    game_athlete_objs = []
    # faz uma query para obter as instancias com o id
    games = Game.objects.all()
    athletes = Athlete.objects.all()

    for game in games:
        # adiciona relações
        athlete = athletes.get(athlete_id_ref=game.athlete_id_ref)
        game_athlete_instance = GameAthlete(athlete=athlete, game=game)
        game_athlete_objs.append(game_athlete_instance)

    print("Atualizando valores da relação Game & Athlete ...")
    GameAthlete.objects.bulk_create(game_athlete_objs, ignore_conflicts=True)


if __name__ == "__main__":
    startTime = datetime.now()
    print("\nPopulando campos a partir do csv...\n")

    populate()

    print(f"\nPopulação concluída. Total de registros: {Game.objects.count()}\n")
    print(f"Duração: {str(datetime.now() - startTime).split('.')[0]}")
