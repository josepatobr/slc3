from django.db import models
from django.conf import settings


class Status_Tasks(models.TextChoices):
    not_started = "not_started", ("ainda não começou a fazer")
    in_progress = "in_progress", ("ainda esta fazendo")
    completed = "completed", ("task completada")


class Principal_Tasks(models.Model):
    name_task = models.CharField(max_length=50, unique=False, blank=False, null=False)
    description_task = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_task


class Stages(models.Model):
    principal_task = models.ForeignKey(Principal_Tasks, on_delete=models.CASCADE)

    name_stages = models.CharField(max_length=50, unique=False, blank=False, null=False)
    description_stages = models.TextField(blank=True, null=True)

    status_stages = models.CharField(
        choices=Status_Tasks, default=Status_Tasks.not_started, null=True, blank=True
    )
    project_manager = models.ManyToManyField(
        settings.AUTH_USER_MODEL, null=True, blank=True
    )
    end_date = models.DateField(blank=True, null=True)

    comment_stages = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name_stages
