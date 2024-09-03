from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from .views import RegisterView, CustomUserDetailView, RoleCreateView

router = routers.DefaultRouter()
router.register(r'users', RoleCreateView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
] + router.urls
