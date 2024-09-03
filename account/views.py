from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, 
                                        AllowAny, IsAdminUser, 
                                        IsAuthenticated)
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model


from .serializers import CustomUserSerializer, RegisterSerializer, RoleSerializer
from .models import Role


CustomUser = get_user_model()

class RoleCreateView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"detail": "Logout failed."}, status=status.HTTP_400_BAD_REQUEST)
        


class CustomUserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # You can change this to IsAuthenticated for more security

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
                           
