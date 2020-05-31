from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        # extra_kwargs={'password':{'write_only':True}}

    # username validation is done by default as well
    # def validate_username(self,value):
    #     qs=User.objects.filter(username__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('Username already exist')
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
        return user_obj
