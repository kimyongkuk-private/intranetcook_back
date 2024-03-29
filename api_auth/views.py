from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import TokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class Login(APIView):
    """
    POST  /api/auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    def __init__(self):

        pass

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            #login(request, user)->어드민 세션로그인
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    """
    POST  /api/auth/logout/
    """
    def post(self, request, *args, **kwargs):
        #request.user.auth_token.delete()
        auth_token = request.data.get("token", "")
        auth_token.delete()
        return Response(status=status.HTTP_200_OK)
def put(self):

        pass

def delete(self):

        pass
    # def get(self, request, format=None):
