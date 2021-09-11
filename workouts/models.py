from django.db import models
import django.utils.timezone as timezone
import datetime

class WorkoutLog(models.Model):
    exercise = models.CharField(max_length=100)
    duration = models.IntegerField(max_length=3)
    date = models.DateField(default=timezone.now())

class DietPlan(models.Model):
    water = models.DecimalField(decimal_places=3 , max_digits=3)
    date = models.DateField(auto_now_add=True)
    protein = models.DecimalField(decimal_places=3 , max_digits=5)
    carbohydrate = models.DecimalField(decimal_places=3 , max_digits=5)
    fat = models.DecimalField(decimal_places=3, max_digits=5)
    vitamin = models.DecimalField(decimal_places=3 , max_digits=5)
    mineral = models.DecimalField(decimal_places=3 , max_digits=5)
    roughage = models.DecimalField(decimal_places=3, max_digits=5)