# Generated by Django 2.0.2 on 2018-02-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baslerbauer_main', '0010_auto_20180217_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]