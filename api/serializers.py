
from django.contrib.auth import authenticate
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


class UserClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'id')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                data["user"] = user
            else:
                msg = 'Este usuario y contraseña no coinciden, intenta de nuevo.'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Se deben enviar el email y la contraseña.'
            raise exceptions.ValidationError(msg)
        return data


class PokemonSerializer(serializers.ModelSerializer):
    element_english   = serializers.ReadOnlyField(source='id_element.english')
    class Meta:
        model = Pokemon
        fields = ('id_pokedex', 'name', 'id_element','image', 'description', 'element_english')