from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from django.contrib.auth import get_user_model

from .models import Role


CustomUser = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'name',
            'surname',
            'phone_number',
            'role',
            'created_at',
            'is_active'
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'name',
            'surname',
            'phone_number',
            'role',
            'password'
        ]
        extra_kwargs = {
            'role': {'read_only': True} #Make role only-read durring registration
        }
    
    def create(self, validated_data):
        role, created = Role.objects.get_or_create(title='SimpleUser')
        validated_data['role'] = role
        user = CustomUser.objects.create(
            name = validated_data['name'],
            surname=validated_data['surname'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            password=validated_data['password'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
    
