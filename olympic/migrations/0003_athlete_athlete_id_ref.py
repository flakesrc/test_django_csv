# Generated by Django 3.1.6 on 2021-02-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0002_game_athlete_id_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='athlete_id_ref',
            field=models.IntegerField(null=True),
        ),
    ]
