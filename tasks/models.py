from django.db import models
from django.contrib.auth.models import User


class AssignedTo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("U", "Urgent"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("inProgress", "In Progress"),
        ("awaitingFeedback", "Awaiting Feedback"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(default="Do your work")
    category = models.CharField(max_length=50, default="To Do")
    color = models.CharField(max_length=7, default="#8AA4FF")
    assigned_to_names = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="todo")

    def __str__(self):
        return self.title
