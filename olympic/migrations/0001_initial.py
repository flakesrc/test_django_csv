# Generated by Django 3.1.6 on 2021-02-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('noc', models.CharField(max_length=3)),
                ('athlete', models.ManyToManyField(to='olympic.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('sport', models.CharField(max_length=80)),
                ('event', models.CharField(max_length=80)),
                ('medal', models.IntegerField(choices=[(0, 'NA'), (1, 'Bronze'), (2, 'Silver'), (3, 'Gold')])),
                ('athele', models.ManyToManyField(to='olympic.Athlete')),
                ('team', models.ManyToManyField(to='olympic.Team')),
            ],
        ),
    ]
