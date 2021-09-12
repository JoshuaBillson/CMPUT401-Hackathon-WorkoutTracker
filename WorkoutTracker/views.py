from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import F
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


# Create your views here.
def index(request: HttpRequest):
    return redirect(reverse("users:login"))
