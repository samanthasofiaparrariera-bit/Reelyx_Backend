from rest_framework import serializers
from Users.models.users_models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'nombre', 'email', 'bio', 'image')