from django.forms import ModelForm
from .models import WorkoutLog


class WorkoutLogForm(ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['exercise', 'duration', 'date', "user"]
