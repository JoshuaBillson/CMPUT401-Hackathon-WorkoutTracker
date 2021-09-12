from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def passwordLengthValidator(form: dict):
    return len(form["password1"]) >= 8 and len(form["password2"]) >= 8


def passwordsMatchValidator(form: dict):
    return form["password1"] == form["password2"]


def uniqueUsernameValidator(form: dict):
    username = form["username"]
    return len(User.objects.filter(username=username)) == 0


validators = [(passwordLengthValidator, "Passwords Must Contain At Least 8 Characters!"),
              (passwordsMatchValidator, "Entered Passwords Do Not Match!"),
              (uniqueUsernameValidator, "This Username Is Already Taken!")]


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": UserCreationForm})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("workouts:view"))
        else:
            msgs = []
            for validator in validators:
                if not validator[0](request.POST):
                    msgs.append(validator[1])
            return render(request, "users/register.html", {"messages": msgs})


def loginPage(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("workouts:view"))
        else:
            msgs = ['Failed TO Log In', "Create An Account By Clicking \"Register\""]
            return render(request, "users/login.html", {"messages": msgs})


def logOut(request):
    logout(request)
    return redirect(reverse("home"))

