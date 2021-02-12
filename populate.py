import os
import django
import pandas as pd
from datetime import datetime
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
django.setup()

from olympic.models import Game, Athlete


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

    for row in df.itertuples():

        # número da linha de registros de jogos
        # começa no index 2 do csv
        register_row_number = row.Index + 2

        athlete, _ = Athlete.objects.get_or_create(
            id=row.ID,
            defaults={
                "name": row.Name,
                "sex": row.Sex,
                "age": normalize_na(row.Age),
                "height": normalize_na(row.Height),
                "weight": normalize_na(row.Weight),
                "team": row.Team,
                "noc": row.NOC,
            },
        )

        game, _ = Game.objects.get_or_create(
            id=register_row_number,
            defaults={
                "name": row.Games,
                "year": row.Year,
                "season": row.Season,
                "city": row.City,
                "sport": row.Sport,
                "event": row.Event,
                "medal": normalize_na(row.Medal),
            },
        )

        if not game.athlete.exists():
            game.athlete.add(athlete)


if __name__ == "__main__":
    startTime = datetime.now()
    print("\nPopulando campos a partir do csv...\n")

    populate()

    print(f"\nPopulação concluída. Total de registros: {Game.objects.count()}\n")
    print(f"Duração: {str(datetime.now() - startTime).split('.')[0]}")
