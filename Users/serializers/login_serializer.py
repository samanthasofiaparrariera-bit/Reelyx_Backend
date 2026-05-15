from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Proyecto: Reelyx
# Autora: Samantha Sofía Parra Riera
# Descripción: Serializer encargado de validar el inicio de sesión.

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False, min_length=5)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email is None or password is None:
            raise serializers.ValidationError("Tienes que enviar el email y la contraseña")

        # Comprobamos las credenciales que ha introducido el usuario
        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Email o contraseña incorrecta")

        # No se permite iniciar sesión hasta verificar el correo
        if not user.is_verified:
            raise serializers.ValidationError("Debes verificar tu correo antes de iniciar sesión")

        # Generamos los tokens JWT para mantener la sesión iniciada
        refresh = RefreshToken.for_user(user)

        return {
            "success": True,
            "data": {
                "email": user.email,
                "nombre": user.nombre,
                "token": str(refresh.access_token),
                "refreshToken": str(refresh),
            }
        }