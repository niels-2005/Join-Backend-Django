from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "category",
            "color",
            "assigned_to_names",
            "deadline",
            "priority",
            "status",
        ]
