from django.shortcuts import reverse, redirect
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(reverse("workouts:view"))
    return redirect(reverse("users:login"))
