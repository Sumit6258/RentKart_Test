
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'customers',CustomerViewSet)


urlpatterns = router.urls
