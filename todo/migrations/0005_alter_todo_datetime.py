# Generated by Django 3.2.7 on 2021-09-19 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 10, 44, 41, 131236)),
        ),
    ]