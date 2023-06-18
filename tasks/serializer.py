from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "category",
            "color",
            "assigned_to",
            "deadline",
            "priority",
        ]
