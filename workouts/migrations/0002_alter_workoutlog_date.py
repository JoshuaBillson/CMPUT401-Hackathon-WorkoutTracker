# Generated by Django 3.2.7 on 2021-09-11 21:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 11, 21, 6, 42, 247961, tzinfo=utc)),
        ),
    ]
