from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import F
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


# Create your views here.
def index(request: HttpRequest):
    msgs=[]
    if request.method == "GET":
        return render( request, "home.html", {"form": AuthenticationForm} )
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
            # Redirect to a success page.
        else:
            msgs = ['fail to login']
            return render(request, "home.html", {"messages": msgs})
        # Return an 'invalid login' error message.
        
        # form = AuthenticationForm(request.POST)
        # if form.is_valid():
        #     user = form.get_user()
        #     login(request, user)
        #     return redirect(reverse("home"))
        # else:
        #     msgs = ['fail to login']
        #     return render(request, "home.html", {"messages": msgs})
