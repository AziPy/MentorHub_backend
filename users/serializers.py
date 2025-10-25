from rest_framework import serializers
from .models import User
from .models import CartItem

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


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
class CartItemSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_price = serializers.DecimalField(source='course.price', max_digits=10, decimal_places=2, read_only=True)

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                data['user'] = user
                return data
        except User.DoesNotExist:
            pass

        raise serializers.ValidationError("Неверный email или пароль")
class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления профиля"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'bio']
        read_only_fields = ['email', 'role']  # email и роль нельзя менять

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
        model = CartItem
        fields = ['id', 'course', 'course_title', 'course_price', 'quantity', 'added_at']

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'first_name', 'last_name', 'role',
                  'avatar', 'bio', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_name(self, obj):
        full_name = f"{obj.first_name} {obj.last_name}".strip()
        return full_name if full_name else obj.email