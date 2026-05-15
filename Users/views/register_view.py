from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.register_serializer import RegisterSerializer
from Users.email_service import enviar_verificacion
import random

# Proyecto: Reelyx
# Autora: Samantha Sofía Parra Riera
# Descripción: Vista encargada del registro de usuarios y envío del código de verificación.

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # Generamos un code de 6 dígitos y lo enviamos por correo con Resend
            codigo = str(random.randint(100000, 999999))
            # Guardamos el código para poder comprobarlo después en la verificación
            user.verification_code = codigo
            user.save()
            # Enviamos el código de verificación con la API de Resend
            enviar_verificacion(user.email, codigo)

            return Response({
                "success": True,
                "message": "Usuario registrado. Revisa tu correo para verificar la cuenta."
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)