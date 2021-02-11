import os
import django
import csv
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

try:
    django.setup()
    from olympic.models import Game, Athlete
except:
    pass


def populate():
    with open("assets/athlete_events.csv") as athlete_events:
        reader = csv.reader(athlete_events)

        # pular os nomes dos campos do csv
        next(reader)

        for rows in reader:
            pk = rows[0]
            name = rows[1]
            sex = rows[2]
            age = rows[3] if rows[3] != "NA" else None
            height = rows[4] if rows[4] != "NA" else None
            weight = rows[5] if rows[5] != "NA" else None
            team = rows[6]
            noc = rows[7]
            game_name = rows[8]
            year = rows[9]
            season = rows[10]
            city = rows[11]
            sport = rows[12]
            event = rows[13]
            medal = rows[14]

            athlete, _ = Athlete.objects.get_or_create(
                id=pk,
                defaults={
                    "name": name,
                    "sex": sex,
                    "age": age,
                    "height": height,
                    "weight": weight,
                    "team": team,
                    "noc": noc,
                },
            )

            game = Game.objects.create(
                name=game_name,
                year=year,
                season=season,
                city=city,
                sport=sport,
                event=event,
                medal=medal,
            )
            game.athlete.add(athlete)

            print(game)


if __name__ == "__main__":
    print(f"\n{'='*5} Populando campos a partir do csv... {'='*5}\n")

    populate()

    print(f"\n{'='*5} População concluída. {'='*5}\n")
