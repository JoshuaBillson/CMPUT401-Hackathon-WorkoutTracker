from django.urls import include, path
from .views import register

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
]
