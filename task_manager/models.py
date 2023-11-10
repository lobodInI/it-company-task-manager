from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        to=Position,
        on_delete=models.CASCADE,
        related_name="workers"
    )

    def __str__(self) -> str:
        return f"{self.position} : {self.first_name} {self.last_name}"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    priority_choises = [
        ("UR", "Urgent"),
        ("HG", "High"),
        ("MD", "Medium"),
        ("LW", "Low")
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=2, choices=priority_choises)
    task_type = models.ForeignKey(
        to=TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        to=get_user_model(),
        related_name="tasks"
    )

    def __str__(self) -> str:
        return self.name
