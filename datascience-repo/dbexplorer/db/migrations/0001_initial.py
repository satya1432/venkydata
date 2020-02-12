# Generated by Django 2.1.15 on 2020-02-03 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('port', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Database Config',
                'verbose_name_plural': 'Database Configs',
                'db_table': 'database_configs',
            },
        ),
        migrations.CreateModel(
            name='DatabaseEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('connection', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Database Engine',
                'verbose_name_plural': 'Database Engines',
                'db_table': 'database_engines',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('title', models.CharField(max_length=255)),
                ('sql', models.TextField()),
                ('description', models.TextField()),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.DatabaseEngine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queries',
                'db_table': 'queries',
            },
        ),
        migrations.AddField(
            model_name='databaseconfig',
            name='engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.DatabaseEngine'),
        ),
        migrations.AddField(
            model_name='databaseconfig',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]