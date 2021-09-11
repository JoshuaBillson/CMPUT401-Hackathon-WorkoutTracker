from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import F


# Create your views here.
def index(request: HttpRequest):
    return render(request, "base.html", {"message": "This Is The Home Page!"})
