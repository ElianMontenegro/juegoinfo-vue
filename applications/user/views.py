from django.shortcuts import render
#
from firebase_admin import auth
# Create your views here.

from  rest_framework.views import  APIView
from rest_framework.generics import  CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
#

from .serializers import (
    LoginSocialSerializer , 
    RegisterUserSerializer ,
    AuthCustomTokenSerializer
)
#models
from .models import User

class LoginSocialAPIView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        #
        id_token = serializer.data.get('token_id')
        #decodificar token
        decoded_token = auth.verify_id_token(id_token)
        #
        email = decoded_token['email']
        name = decoded_token['name']
        avatar = decoded_token['picture']
        verified = decoded_token['email_verified']

        user, created = User.objects.get_or_create(
            email = email,
            defaults={
                'name':name,
                'email': email,
                'is_active': True
            }
        )
        #
        if created:
            token = Token.objects.create(user=user)
            
        else:
            token = Token.objects.get(user=user)

        userGet = {
            'id' :user.id,
            'email': user.email,
            'name': user.name,    
            'is_staff': user.is_staff , 
            'is_active': user.is_active 
        }

        return Response(
            {
                'token':token.key,
                'user': userGet
            }
        )


class LoginApi(CreateAPIView):
    serializer_class = RegisterUserSerializer

    



class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    

    def post(self, request):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        userGet = {
            'id' :user.id,
            'email': user.email,
            'name': user.name, 
            'is_staff': user.is_staff , 
            'is_active': user.is_active
        }


        return Response(
            {
                'token':token.key,
                'user': userGet
            }
        )