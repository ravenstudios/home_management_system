# Generated by Django 4.0.6 on 2022-10-22 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_familymember'),
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompletedChores',
            new_name='ChoreLogs',
        ),
    ]