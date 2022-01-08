
from rest_framework import serializers
from api.models import Pokemon, User
from django.core import exceptions
from api.utils import get_or_none


class ClientRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True)

    # Función que valida que el usario no exista y las contraseñas sean iguales
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        password_confirmation = data.get("password_confirmation", None)
        user = get_or_none(User, email=email)
        if user:
            msg = "Este correo electrónico ya está en uso."
            raise exceptions.ValidationError(msg)
        if password != password_confirmation:
            msg = "Las contraseñas no coinciden"

        else:
            user = User.objects.create_user(email=email, password=password)
            user.save()
            data["user"] = user
        return data
