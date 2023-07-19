from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.utils.encoding import force_text
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset(request):
    email = request.data.get("email")

    if not email:
        return JsonResponse({"detail": "No email provided."}, status=400)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse(
            {"detail": "User with this email does not exist."}, status=400
        )

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    reset_link = f"http://localhost:4200/resetpassword/{uid}/{token}/"

    subject = "Password Reset"
    html_message = f'<p>Password reset link: <a href="{reset_link}">Click here to reset your password</a></p>'

    email = EmailMessage(subject, html_message, "mail@niels-scholz.com", [email])
    email.content_subtype = "html"  # This is the crucial line
    email.send()

    return JsonResponse({"detail": "Password reset email has been sent."})


@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset_confirm(request):
    uidb64 = request.data.get("uid")
    token = request.data.get("token")
    password1 = request.data.get("password1")
    password2 = request.data.get("password2")

    if not uidb64 or not token:
        return JsonResponse({"detail": "Invalid uid or token."}, status=400)

    if password1 != password2:
        return JsonResponse({"detail": "Passwords do not match."}, status=400)

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.set_password(password1)
            user.save()
            return JsonResponse({"detail": "Password reset successful."})
        else:
            return JsonResponse({"detail": "Invalid token."}, status=400)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return JsonResponse({"detail": "Invalid uid."}, status=400)
