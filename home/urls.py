from django.urls import path
from . import views


urlpatterns = [
    path("slc3/", views.home, name="home"),
    path("tasks/<int:task_id>", views.tasks, name="tasks"),
]
