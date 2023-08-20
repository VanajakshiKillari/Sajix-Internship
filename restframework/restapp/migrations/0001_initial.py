# Generated by Django 3.2.19 on 2023-06-03 11:15

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cruddb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, unique=True)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]