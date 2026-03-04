from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from ..models.users_models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ('email','nombre' ,'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password2": "Las contraseñas no coinciden"})
        return data

    def validate_email(self,value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya existe")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser.objects.crear_usuario(password=password, **validated_data)
        return user