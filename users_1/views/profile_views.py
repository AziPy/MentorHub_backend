from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema
from users_1.serializers import UserSerializer, UserUpdateSerializer

@extend_schema_view(
    get=extend_schema(
        tags=['Profile'],
        summary='Get current user profile',
        description='Retrieves the authenticated user\'s profile.',
        responses={200: UserSerializer}
    ),
    put=extend_schema(
        tags=['Profile'],
        summary='Update current user profile',
        description='Updates the authenticated user\'s profile.',
        request=UserUpdateSerializer,
        responses={200: UserSerializer}
    )
)
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Get current user profile"""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        """Update current user profile"""
        serializer = UserUpdateSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(request.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)