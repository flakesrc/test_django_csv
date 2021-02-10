import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
django.setup()

from olympic.models import Game, Team, Athlete


def populate():
    pass


if __name__ == "__main__":
    print(f"\n{'='*5} Populando campos a partir do csv... {'='*5}\n")

    populate()

    print(f"\n{'='*5} População concluída. {'='*5}\n")
