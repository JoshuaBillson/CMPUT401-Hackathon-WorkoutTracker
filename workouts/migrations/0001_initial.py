# Generated by Django 3.2.7 on 2021-09-11 21:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('exercise', models.CharField(max_length=150)),
                ('duration', models.IntegerField(max_length=3)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 9, 11, 21, 5, 57, 924225, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
