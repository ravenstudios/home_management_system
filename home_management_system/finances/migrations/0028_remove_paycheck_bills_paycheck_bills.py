# Generated by Django 4.0.6 on 2022-08-08 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0027_bill_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paycheck',
            name='bills',
        ),
        migrations.AddField(
            model_name='paycheck',
            name='bills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finances.bill'),
        ),
    ]
