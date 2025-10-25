from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiResponse
from users.serializers import RegisterSerializer
from users.models import User

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {"access": str(refresh.access_token)}

class RegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    @extend_schema(
        tags=["Authentication"],
        summary="Register a new user",
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(response=UserSerializer, description="User registered successfully"),
            400: OpenApiResponse(description="Validation error")
        },
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)

            user_data = UserSerializer(user).data
            return Response({
                **user_data,
                "access_token": tokens["access"]
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

