# Generated by Django 4.0.6 on 2022-10-16 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0012_chore_day_assigned'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Day',
        ),
    ]
