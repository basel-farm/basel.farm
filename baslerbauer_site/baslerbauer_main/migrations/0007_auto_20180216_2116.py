# Generated by Django 2.0.2 on 2018-02-16 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baslerbauer_main', '0006_auto_20180216_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
