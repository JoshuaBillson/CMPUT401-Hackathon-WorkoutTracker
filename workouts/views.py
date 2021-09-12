from django.shortcuts import render, reverse, redirect
from django.http import HttpRequest
from .forms import WorkoutLogForm
from .models import WorkoutLog


# Create your views here.
def view(request: HttpRequest):
    if request.user.is_authenticated:
        workouts = WorkoutLog.objects.filter(user=request.user.id).order_by("-date")
        return render(request, "workouts/view.html", {"workouts": workouts})
    return redirect(reverse("users:login"))


def submit(request: HttpRequest):
    if request.method == "GET" and request.user.is_authenticated:
        return render(request, "workouts/submit.html", {"user": request.user})
    elif request.method == "GET" and not request.user.is_authenticated:
        return redirect(reverse("users:login"))
    form = WorkoutLogForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("workouts:view"))
    return render(request, "workouts/submit.html", {"message": "Error!"})
