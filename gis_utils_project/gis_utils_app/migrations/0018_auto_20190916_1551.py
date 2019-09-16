# Generated by Django 2.2.5 on 2019-09-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0017_auto_20190911_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='average_age',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='employees',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='income',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='net_income',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ordinary_income',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sales',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='service_years',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]
