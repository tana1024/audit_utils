# Generated by Django 2.2.5 on 2019-09-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0018_auto_20190916_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='net_income',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ordinary_income',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sales',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
