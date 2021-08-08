from rest_framework import serializers
from rest_framework.authentication import authenticate
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class LoginSocialSerializer(serializers.Serializer):

    token_id = serializers.CharField(required=True)

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
            'password2',
            'is_active',
            'is_staff'
        ]
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            name = self.validated_data['name'],
            is_active = self.validated_data['is_active'],
            is_staff = self.validated_data['is_staff'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        print(password2)
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(password)
        user.save()

        return user

class AuthCustomTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField(style={'input_type':'password'})

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if validate_email(email_or_username):
                user_request = get_object_or_404(
                    User,
                    email=email_or_username,
                )

                email_or_username = user_request.username

            user = authenticate(username=email_or_username, password=password)

            if user:
                if not user.is_active:
                    raise ValidationError('User account is disabled.')
            else:
                raise ValidationError('Unable to log in with provided credentials.')
                
        else:
            raise ValidationError('Must include "email or username" and "password"')

        attrs['user'] = user
        return attrs