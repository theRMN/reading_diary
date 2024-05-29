from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, mixins
# from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filters import SearchUser
from .models import UserSettings
from .serializers import UserSerializer, UserSettingsSerializer
from .permissions import IsAdminOrIsModer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SearchUser
    permission_classes = (IsAdminOrIsModer,)


class UserSettingsViewSet(GenericViewSet,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          ):

    serializer_class = UserSettingsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserSettings.objects.filter(user=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #
    #     return Response(serializer.data[0])
