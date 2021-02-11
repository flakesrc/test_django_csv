# SCRIPT NÃO ESTÁ FUNCIONANDO ATUALMENTE
import os
import django
import csv
from django.conf import settings
from django.db.utils import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
django.setup()

from olympic.models import Game, Athlete


def populate():
    with open("assets/athlete_events.csv") as athlete_events:
        reader = csv.reader(athlete_events)

        # pula a row com o nome dos campos csv
        next(reader)

        athlete_objs = []
        game_objs = []

        for i, rows in enumerate(reader):

            # número da linha do registro no csv
            # usado para identificar o game e usar como id
            register_row_number = i + 1

            pk = rows[0]
            name = rows[1]
            sex = rows[2]
            age = rows[3] if rows[3] != "NA" else None
            height = rows[4] if rows[4] != "NA" else None
            weight = float(rows[5]) if rows[5] != "NA" else None
            team = rows[6]
            noc = rows[7]
            game_name = rows[8]
            year = rows[9]
            season = rows[10]
            city = rows[11]
            sport = rows[12]
            event = rows[13]
            medal = rows[14]

            athlete_instance = Athlete(
                id=pk,
                name=name,
                sex=sex,
                age=age,
                height=height,
                weight=weight,
                team=team,
                noc=noc,
            )

            athlete_objs.append(athlete_instance)

            game_objs.append(
                Game(
                    id=register_row_number,
                    name=game_name,
                    year=year,
                    season=season,
                    city=city,
                    sport=sport,
                    event=event,
                    medal=medal,
                )
                .save()
                .athlete.add(athlete_instance)
            )

        Athlete.objects.bulk_create(athlete_objs, ignore_conflicts=True)
        Game.objects.bulk_create(game_objs, ignore_conflicts=True)


if __name__ == "__main__":
    print("\nPopulando campos a partir do csv...")

    populate()

    print(f"\nPopulação concluída. Total de registros: {Game.objects.count()}\n")
