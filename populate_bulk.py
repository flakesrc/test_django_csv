# SCRIPT NÃO ESTÁ FUNCIONANDO ATUALMENTE
# TODO: obter o id do atleta e inserir em um campo
#       do model Game
#       depois, fazer o bulk sem as relações
#       e após os dados serem inseridos, realizar
#       um loop somente para adicionar as relações

import os
import django
import pandas as pd
from django.conf import settings
from django.db.utils import IntegrityError

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

    athlete_objs = []
    game_objs = []

    for row in df.itertuples():

        # número da linha de registros de jogos
        # começa no index 2 do csv
        register_row_number = row.Index + 2

        athlete_instance = Athlete(
            id=row.ID,
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
            id=register_row_number,
            athlete_id_ref=athlete_instance.id,
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
    # ignore para ignorar se já existir um registro
    # caso o script seja pausado e executado posteriormente
    Athlete.objects.bulk_create(athlete_objs, ignore_conflicts=True)
    Game.objects.bulk_create(game_objs, ignore_conflicts=True)


if __name__ == "__main__":
    print("\nPopulando campos a partir do csv...\n")

    populate()

    print(f"\nPopulação concluída. Total de registros: {Game.objects.count()}\n")
