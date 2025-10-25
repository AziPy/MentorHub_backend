from rest_framework import serializers
from users.models import Review, RequestsNew

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'student', 'mentor', 'text', 'rating', 'created_at']
        read_only_fields = ['student', 'created_at']

class RequestsNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestsNew
        fields = ['id', 'student', 'mentor', 'title', 'description', 'status', 'created_at']
        read_only_fields = ['student', 'created_at']