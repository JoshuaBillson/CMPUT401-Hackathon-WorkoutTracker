from django.contrib import admin
from django.urls import include, path
from .views import index

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path("workouts/", include("workouts.urls")),
    path("users/", include("users.urls")),
    path('admin/', admin.site.urls),
]
