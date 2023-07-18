from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
