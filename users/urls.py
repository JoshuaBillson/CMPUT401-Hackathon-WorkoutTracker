from django.urls import include, path
from .views import register, logOut

urlpatterns = [
    path("register/", register),
    path("logout/", logOut),
]
