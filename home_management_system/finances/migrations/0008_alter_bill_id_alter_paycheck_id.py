# Generated by Django 4.0.6 on 2022-07-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_alter_paycheck_bills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paycheck',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
