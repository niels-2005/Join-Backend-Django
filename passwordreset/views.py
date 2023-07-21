from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.core.mail import EmailMessage
from .serializers import PasswordResetSerializer, PasswordResetConfirmSerializer

@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset(request):
    serializer = PasswordResetSerializer(data=request.data)
    if serializer.is_valid():
        reset_data = serializer.save()

        reset_link = f"https://niels-scholz.com/join-frontend/resetpassword/{reset_data['uid']}/{reset_data['token']}/"
        subject = "Password Reset"
        html_message = f'<p>Password reset link: <a href="{reset_link}">Click here to reset your password</a></p>'
        email = EmailMessage(subject, html_message, "mail@niels-scholz.com", [serializer.validated_data['email']])
        email.content_subtype = "html"
        email.send()

        return JsonResponse({"detail": "Password reset email has been sent."})
    else:
        return JsonResponse(serializer.errors, status=400)

@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset_confirm(request):
    serializer = PasswordResetConfirmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"detail": "Password reset successful."})
    else:
        return JsonResponse(serializer.errors, status=400)
