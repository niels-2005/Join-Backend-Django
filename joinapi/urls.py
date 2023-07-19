from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from contacts.views import ContactViewSet
from django.contrib import admin
from passwordreset.views import password_reset, password_reset_confirm

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"contacts", ContactViewSet, basename="contacts")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("dj_rest_auth.urls")),
    path("api/registration/", include("dj_rest_auth.registration.urls")),
    path("api/join/", include(router.urls)),
    path("api/reset/password/", password_reset, name="password_reset"),
    path(
        "api/reset/password/confirm",
        password_reset_confirm,
        name="password_reset_confirm",
    ),
]
