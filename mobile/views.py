from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Mobile, Brand
from .serializers import MobileSerializer, BrandSerializer
from account.permissions import IsSaler



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = (IsSaler, IsAdminUser)
    permission_classes = (AllowAny, )


class MobileCreateView(generics.CreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    # permission_classes = (IsSaler, IsAdminUser, )
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers =   self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
class MobileListView(generics.ListAPIView):
    queryset = Mobile.objects.all().order_by('created_at')
    serializer_class = MobileSerializer
    permission_classes = (IsAuthenticated, )
