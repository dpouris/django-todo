# Generated by Django 3.2.7 on 2021-09-19 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 10, 34, 55, 293668)),
        ),
    ]
