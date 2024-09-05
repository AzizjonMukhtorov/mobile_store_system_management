from django.urls import path

from rest_framework import routers

from .views import (MobileCreateView, BrandViewSet, 
                    MobileListView)


router = routers.DefaultRouter()

router.register(r'brand', BrandViewSet)

urlpatterns = [
    path('create-mobile/', MobileCreateView.as_view(), name='create-mobile'),
    path('list-mobile/', MobileListView.as_view(), name='list-mobile')
] + router.urls
