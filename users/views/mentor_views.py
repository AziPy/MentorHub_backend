from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from users.permissions import MentorPermission

class MentorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role='mentor')
    serializer_class = UserSerializer
    permission_classes = [MentorPermission]
