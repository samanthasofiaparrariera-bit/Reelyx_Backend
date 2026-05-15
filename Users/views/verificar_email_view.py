from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Users.models.users_models import CustomUser


class VerifyEmailView(APIView):
    def get(self, request,uid, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(pk= user_id)
        except Exception:
            return Response({
                "error": "Enlace no válido"
            }, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_verified = True
            user.save()

            return Response({
                "success": True,
                "message": "Cuenta verificada correctamente"
            }, status=status.HTTP_200_OK)

        return Response({
            "error": "Token no válido o caducado"
        }, status= status.HTTP_400_BAD_REQUEST)