from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task


class TaskTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.test_user)
        self.api_authentication()

        self.test_task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            category="Test Category",
            color="#8AA4FF",
            assigned_to_names="Test User",
            deadline="2023-07-31",
            priority="M",
            status="todo",
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_task(self):
        url = reverse("tasks-list")
        data = {
            "title": "New Task",
            "description": "This is a new task",
            "category": "New Category",
            "color": "#8AA4FF",
            "assigned_to_names": "New User",
            "deadline": "2023-07-31",
            "priority": "M",
            "status": "todo",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        url = reverse("tasks-detail", kwargs={"pk": self.test_task.id})
        data = {
            "title": "Updated Task",
            "description": "This task has been updated",
            "category": "Updated Category",
            "color": "#8AA4FF",
            "assigned_to_names": "Updated User",
            "deadline": "2023-07-31",
            "priority": "M",
            "status": "inProgress",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.test_task.refresh_from_db()
        self.assertEqual(self.test_task.title, data["title"])
        self.assertEqual(self.test_task.description, data["description"])
        self.assertEqual(self.test_task.category, data["category"])
        self.assertEqual(self.test_task.assigned_to_names, data["assigned_to_names"])
        self.assertEqual(self.test_task.status, data["status"])

    def test_delete_task(self):
        url = reverse("tasks-detail", kwargs={"pk": self.test_task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)
