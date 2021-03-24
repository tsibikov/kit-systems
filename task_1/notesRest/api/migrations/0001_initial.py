# Generated by Django 3.1.5 on 2021-03-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('note', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1024)),
            ],
        ),
    ]