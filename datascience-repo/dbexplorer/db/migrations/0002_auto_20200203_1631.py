# Generated by Django 2.1.15 on 2020-02-03 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseconfig',
            name='user',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='databaseconfig',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
