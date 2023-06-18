from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from tasks.views import TaskViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("dj_rest_auth.urls")),
    path("api/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/join/tasks/",
        TaskViewSet.as_view({"get": "list", "post": "create"}),
        name="tasks",
    ),
    path(
        "api/join/tasks/<int:pk>/",
        TaskViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="task-detail",
    ),
]
