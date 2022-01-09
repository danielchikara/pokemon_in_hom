from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from api.serializers import *
from api.models import *
# Create your views here.


class RegisterClientView(APIView):

    def post(self, request):
        serializer = ClientRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        success = False
        code = 400
        if user:
            success = True
            code = 201
        return Response({"success": success}, status=code)


# Inicio de sesion y creación de token
class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            token, created = Token.objects.get_or_create(user=user)
            serializer_user = UserClientSerializer(user)
            return Response({"token": token.key, "user": serializer_user.data}, status=200)


# eliminación de token
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


# Creación de pokemon
class CreatePokemonView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_class = (TokenAuthentication)
    serializer_class = PokemonSerializer


# Lista de pokemones
class ListPokemonView(generics.ListAPIView):
    serializer_class = PokemonSerializer
    
    def get_queryset(self):
        search = self.request.query_params.get('id_element', None)
        if search is not None:
            return Pokemon.objects.filter(id_element=search).order_by('id')
        return Pokemon.objects.all().order_by('id')


# Actualización de pokemon
class UpdatePokemonView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_class = (TokenAuthentication)
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


# Eliminación de pokemon
class DeletePokemonView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_class = (TokenAuthentication)
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()