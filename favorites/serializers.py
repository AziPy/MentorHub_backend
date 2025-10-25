from rest_framework import serializers

from courses_category.models import Course
from courses_category.serializers import CourseSerializer
from favorites.models import Favorite
from users.models import User
from users.serializers import UserSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'item_type', 'item_id', 'item', 'added_at']
        validators = []

    def validate(self, data):
        if 'item_id' not in data:
            raise serializers.ValidationError("item_id is required")
        return data

    def get_item(self, obj):
        if obj.item_type == 'course':
            return CourseSerializer(Course.objects.get(id=obj.item_id)).data
        return UserSerializer(User.objects.get(id=obj.item_id)).data

