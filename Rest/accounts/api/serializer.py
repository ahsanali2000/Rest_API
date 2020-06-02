from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime
from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA
User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'url',
        ]

    def get_url(self, obj):
        return '/api/local/'+str(obj.id)+'/'


class UserRegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    massege = serializers.SerializerMethodField(read_only=True)

    # token_response = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires,'
            # 'token_response'
        ]
        # extra_kwargs={'password':{'write_only':True}}

    # username validation is done by default as well
    # def validate_username(self,value):
    #     qs=User.objects.filter(username__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('Username already exist')
    def get_massege(self, obj):
        return "Thank You, Verify your email."

    def get_token(self, obj):  # instance of model
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    # def get_token_response(self, obj):
    #     user = obj
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     context = self.context
    #     return jwt_response_payload_handler(token, user, request=context['request'])
    #     return response

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Email already exist')

    def validate(self, data):
        pw = data.get('password')
        pw1 = data.get('password2')
        if pw != pw1:
            raise serializers.ValidationError('Passwords must match')
        return data

    def create(self, validated_data):
        user_obj = User(
            username=validated_data.get('username'),
            email=validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        user_obj.is_active = False
        return user_obj
