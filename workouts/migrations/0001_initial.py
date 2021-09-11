# Generated by Django 3.2.7 on 2021-09-11 20:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.DecimalField(decimal_places=3, max_digits=3)),
                ('date', models.DateField(auto_now_add=True)),
                ('protein', models.DecimalField(decimal_places=3, max_digits=5)),
                ('carbohydrate', models.DecimalField(decimal_places=3, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=3, max_digits=5)),
                ('vitamin', models.DecimalField(decimal_places=3, max_digits=5)),
                ('mineral', models.DecimalField(decimal_places=3, max_digits=5)),
                ('roughage', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=100)),
                ('duration', models.IntegerField(max_length=3)),
                ('date', models.DateField(default=datetime.datetime(2021, 9, 11, 20, 15, 35, 798900, tzinfo=utc))),
            ],
        ),
    ]
