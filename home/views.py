from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Principal_Tasks, Stages
from django.contrib import messages



def home(request):
    #tasks = Principal_Tasks.objects.filter(user=request.user)
    tasks = Principal_Tasks.objects.all()
    
    if request.method == "POST":
        name_task = request.POST.get("name_task")
        description_task = request.POST.get("description_task")

        Principal_Tasks.objects.create(
                    name_task=name_task,
                    description_task=description_task,
                    user=request.user, 
                )
        messages.success(request, "Cadastro feito com sucesso!")
        return redirect("home")

    return render(request, "home.html", {"tasks": tasks})


def tasks(request, task_id):
    task = get_object_or_404(Principal_Tasks, id=task_id)
    stages = Stages.objects.filter(principal_task=task)

    if request.method == "POST":
        stage_id = request.POST.get("stage_id")

        if stage_id:
            stage_to_update = get_object_or_404(Stages, id=stage_id)
            
            name_stage_change = request.POST.get("name_stage_change")
            description_stage_change = request.POST.get("description_stage_change")
            comment_stage_change = request.POST.get("comment_stage_change")
            status_stage = request.POST.get("status_stage")
            project_manager_stage = request.POST.get("project_manager_stage")
            date_stage = request.POST.get("date_stage")

            if name_stage_change and name_stage_change.strip():
                stage_to_update.name_stages = name_stage_change

            if description_stage_change and description_stage_change.strip():
                stage_to_update.description_stages = description_stage_change

            if comment_stage_change and comment_stage_change.strip():
                stage_to_update.comment_stages = comment_stage_change

            if project_manager_stage:
                stage_to_update.project_manager.set([project_manager_stage])
        
            else:
                stage_to_update.project_manager.clear()
            
            if date_stage:
                stage_to_update.end_date = date_stage

            stage_to_update.save()
            messages.success(request, "Alterações salvas com sucesso!")
        else:
            name_stages = request.POST.get("name_stages")
            project_manager_stage = request.POST.get("project_manager_stage")

            if name_stages and name_stages.strip():
                new_stage = Stages.objects.create(
                    name_stages=name_stages,
                    principal_task=task,
                )
                
                if project_manager_stage:
                    new_stage.project_manager.set([project_manager_stage])

                messages.success(request, "Tarefa criada com sucesso!")
            else:
                messages.error(request, "O nome da tarefa não pode estar vazio.")
    context = {
        "task": task,
        "stages": stages,
    }
    return render(request, "tasks.html", context)



