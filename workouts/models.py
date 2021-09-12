from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User


class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=150)
    duration = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


class DietPlan(models.Model):
    water = models.DecimalField(decimal_places=3 , max_digits=3)
    date = models.DateField(auto_now_add=True)
    protein = models.DecimalField(decimal_places=3 , max_digits=5)
    carbohydrate = models.DecimalField(decimal_places=3 , max_digits=5)
    fat = models.DecimalField(decimal_places=3, max_digits=5)
    vitamin = models.DecimalField(decimal_places=3 , max_digits=5)
    mineral = models.DecimalField(decimal_places=3 , max_digits=5)
    roughage = models.DecimalField(decimal_places=3, max_digits=5)