# Generated by Django 4.0.6 on 2022-10-09 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chore',
            old_name='assigned_to',
            new_name='assigned_tox',
        ),
    ]