from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Pokemon, User
from django.shortcuts import render
from api.serializers import *
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