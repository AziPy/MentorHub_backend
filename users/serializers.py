from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('email', 'password', 'role')

    def create(self, validated_data):
        username = validated_data['email'].split('@')[0]

        user = User.objects.create_user(
            email=validated_data['email'],
            username=username,
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления профиля"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'bio']
        read_only_fields = ['email', 'role']  # email и роль нельзя менять

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'first_name', 'last_name', 'role',
                  'avatar', 'bio', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_name(self, obj):
        full_name = f"{obj.first_name} {obj.last_name}".strip()
        return full_name if full_name else obj.email