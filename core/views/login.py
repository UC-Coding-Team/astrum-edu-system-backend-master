from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['username', 'password'],
        ),
        responses={
            200: 'Successful login',
            401: 'Invalid credentials',
        }
    )
    def post(self, request):
        """
        Authenticates user and generates JWT tokens.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate refresh and access tokens
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        # Return error response for invalid credentials
        return Response({'error': 'Invalid credentials'}, status=401)
