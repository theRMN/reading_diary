from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import UserViewSet, UserSettingsViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='UserViewSet')
router.register(r'usersettings', UserSettingsViewSet, basename='UserSettingsViewSet')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
