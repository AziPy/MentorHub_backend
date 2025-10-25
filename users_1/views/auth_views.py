from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiResponse
from users_1.serializers import RegisterSerializer, LoginSerializer, UserSerializer

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

class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    @extend_schema(
        tags=["Authentication"],
        summary="Login user",
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(response=UserSerializer, description="Login successful"),
            401: OpenApiResponse(description="Invalid credentials")
        },
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = get_tokens_for_user(user)

        user_data = UserSerializer(user).data
        return Response({
            **user_data,
            "access_token": tokens["access"]
        })

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Authentication"],
        summary="Logout user",
        responses={
            200: OpenApiResponse(description="Logout successful"),
            400: OpenApiResponse(description="Invalid token")
        },
    )
    def post(self, request):
        return Response({"detail": "Logout successful"}, status=status.HTTP_200_OK)