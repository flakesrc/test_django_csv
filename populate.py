import os
import django
import csv
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
django.setup()


from olympic.models import Game, Team, Athlete


def populate():
    with open("assets/athlete_events.csv") as athlete_events:
        reader = csv.reader(athlete_events)

        # pular os nomes dos campos do csv
        next(reader)

        for rows in reader:
            pk = rows[0]
            name = rows[1]
            sex = rows[2]
            age = rows[3]
            height = rows[4]
            weight = rows[5]
            team_name = rows[6]
            noc = rows[7]
            game_name = rows[8]
            year = rows[9]
            season = rows[10]
            city = rows[11]
            sport = rows[12]
            event = rows[13]
            medal = rows[14]

            athlete, _ = Athlete.objects.get_or_create(
                id=pk, name=name, sex=sex, age=age, height=height, weight=weight
            )
            print(athlete)
            team, _ = Team.objects.get_or_create(name=team_name, noc=noc)
            print(team)
            game, _ = Game.objects.get_or_create(
                name=game_name,
                year=year,
                season=season,
                city=city,
                sport=sport,
                event=event,
                medal=medal,
                # models
                athlete=athlete,
                team=team,
            )
            print(game)


if __name__ == "__main__":
    print(f"\n{'='*5} Populando campos a partir do csv... {'='*5}\n")

    populate()

    print(f"\n{'='*5} População concluída. {'='*5}\n")
