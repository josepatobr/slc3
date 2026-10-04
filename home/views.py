from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Principal_Tasks, Stages
from django.contrib import messages

name = "Sd Pinto"


def home(request):
    tasks = Principal_Tasks.objects.all()

    if request.method == "POST":
        name_task = request.POST.get("name_task")
        description_task = request.POST.get("description_task")

        Principal_Tasks.objects.create(
            name_task=name_task,
            description_task=description_task,
        )
        messages.success(request, "Cadastro feito com sucesso!")
        return redirect("home")

    return render(request, "home.html", {"tasks": tasks})


def tasks(request, task_id):
    task = get_object_or_404(Principal_Tasks, id=task_id)
    stages = Stages.objects.all()

    if request.method == "POST":
        name_stages = request.POST.get("name_stages")

        Stages.objects.create(
            name_stages=name_stages,
            principal_task=task,
        )
        messages.success(request, "Cadastro feito com sucesso!")
        return redirect("tasks", task_id=task_id)

    context = {
        "task": task,
        "stages": stages,
    }
    return render(request, "tasks.html", context)


def conf(request):
    return HttpResponse("Hello world")
