# Generated by Django 3.1.6 on 2021-02-14 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0004_auto_20210214_1642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gameathlete',
            unique_together={('athlete', 'game')},
        ),
    ]
