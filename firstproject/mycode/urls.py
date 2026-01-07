
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet, CategoryViewSet, ProductViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'customers',CustomerViewSet)
router.register(r'Categories',CategoryViewSet)
router.register(r'Products',ProductViewSet)
router.register(r'Subscriptions',SubscriptionViewSet)


urlpatterns = router.urls
