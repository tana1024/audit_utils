# Generated by Django 2.2.6 on 2019-10-26 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0020_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUpdateStatus',
            fields=[
                ('api_id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('0', '未更新'), ('1', '更新開始'), ('2', '更新完了'), ('9', '異常終了')], default='0', max_length=1)),
                ('update_count', models.IntegerField(null=True)),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
