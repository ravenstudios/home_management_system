# Generated by Django 4.0.6 on 2022-07-25 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0011_alter_paycheck_ammount_in_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='money_in_bank',
        ),
    ]