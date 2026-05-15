from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from Users.models.users_models import CustomUser
# Proyecto: Reelyx
# Autora: Samantha Sofía Parra Riera
# Descripción: Vista encargada de verificar el código enviado al correo.

class VerifyCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        codigo = request.data.get('codigo')
        # Si el código coincide, activamos la cuenta y eliminamos el código usado
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"success": False, "error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Comprobamos que el código introducido coincida con el código guardado
        if user.verification_code == codigo:
            # Activamos la cuenta una vez verificado el código
            user.is_verified = True
            # Eliminamos el código para evitar que pueda reutilizarse
            user.verification_code = None
            user.save()
            return Response({"success": True}, status=status.HTTP_200_OK)


        return Response({"success": False, "error": "Código incorrecto"}, status=status.HTTP_400_BAD_REQUEST)