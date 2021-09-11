from django.urls import include, path
from .views import register, logOut

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("logout/", logOut),
]
