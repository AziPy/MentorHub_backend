from rest_framework import serializers
from users.models import Review, RequestsNew

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'student', 'mentor', 'text', 'rating', 'created_at']
        read_only_fields = ['student', 'created_at']


