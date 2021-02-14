# Generated by Django 3.1.6 on 2021-02-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('team', models.CharField(max_length=200)),
                ('noc', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete_id_ref', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=201)),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=202)),
                ('city', models.CharField(max_length=203)),
                ('sport', models.CharField(max_length=204)),
                ('event', models.CharField(max_length=205)),
                ('medal', models.CharField(choices=[('None', 'None'), ('NA', 'None'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameAthlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic.athlete')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='athlete',
            field=models.ManyToManyField(related_name='games', through='olympic.GameAthlete', to='olympic.Athlete'),
        ),
    ]
