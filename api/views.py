from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from api.serializers import *
from django.views.decorators.csrf import csrf_exempt
from api.models import *
from django.utils.decorators import method_decorator


# Create your views here.



@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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
@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


# Creación de pokemon recibe todos  los parametros del modelo Pokemon

@method_decorator(csrf_exempt, name='dispatch')
class CreatePokemonView(generics.CreateAPIView):
    serializer_class = PokemonSerializer


# La lista de pokemon puede  recibir   un parametro de filtrado por elemento 

@method_decorator(csrf_exempt, name='dispatch')
class ListPokemonView(generics.ListAPIView):
    serializer_class = PokemonSerializer
    
    def get_queryset(self):
        search = self.request.query_params.get('id_element', None)
        if search is not None:
            return Pokemon.objects.filter(id_element=search).order_by('id')
        return Pokemon.objects.all().order_by('id')


# Actualización de pokemon recibe los mismo parametros de el create

@method_decorator(csrf_exempt, name='dispatch')
class UpdatePokemonView(generics.UpdateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


# Eliminación de pokemon  recibe el id del pokemon a eliminar

@method_decorator(csrf_exempt, name='dispatch')
class DeletePokemonView(generics.DestroyAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()