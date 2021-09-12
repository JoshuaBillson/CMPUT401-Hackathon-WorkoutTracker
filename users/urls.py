from django.urls import path
from .views import register, logOut, loginPage

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", loginPage, name="login"),
    path("logout/", logOut, name="logout"),
]
