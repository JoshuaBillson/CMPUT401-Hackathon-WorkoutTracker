from django.urls import path
from . import views

app_name = "workouts"

urlpatterns = [
    path("view/", views.view, name="view"),
]
