from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User, CartItem


# --- Регистрация ---
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
            role=validated_data.get('role', 'student')
        )
        return user


# --- Логин ---
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        data['user'] = user
        return data


# --- Обновление профиля ---
class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления профиля"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'bio']
        read_only_fields = ['email', 'role']


# --- Отображение пользователя ---
class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'email', 'name', 'first_name', 'last_name', 'role',
            'avatar', 'bio', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_name(self, obj):
        full_name = f"{obj.first_name} {obj.last_name}".strip()
        return full_name if full_name else obj.email


# --- Корзина ---
class CartItemSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_price = serializers.DecimalField(
        source='course.price',
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'course', 'course_title', 'course_price', 'quantity', 'added_at']
