# Generated by Django 3.1.6 on 2021-02-10 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='athele',
            new_name='athlete',
        ),
        migrations.RemoveField(
            model_name='team',
            name='athlete',
        ),
    ]
