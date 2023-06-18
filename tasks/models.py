from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("U", "Urgent"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(default="Do your work")
    category = models.CharField(max_length=50, default="To Do")
    color = models.CharField(max_length=7, default="#FFFFFF")
    assigned_to = models.ManyToManyField(User, related_name="tasks")
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")

    def __str__(self):
        return self.title
