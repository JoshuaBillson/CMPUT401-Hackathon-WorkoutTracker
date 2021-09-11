from django.contrib.auth import login,logout
from django.shortcuts import redirect, render, Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render( request, "users/register.html", {"form": UserCreationForm} )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("workouts:view"))
        else:
            msgs = ["Invalid Password!"]
            return render(request, "users/register.html", {"messages": msgs})

def logOut(request):
    if request.method == "GET":
        # try:
        logout(request)#return None
        # except:
        #     pass
    return redirect('/home')
    # elif request.method == "POST":
        
    #     logout(request)#return None
    #     return redirect('/home')
    
