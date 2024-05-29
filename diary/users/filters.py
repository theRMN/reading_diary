from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    ...


class SearchUser(filters.FilterSet):
    username = CharFilterInFilter(field_name='username', lookup_expr='in')
    role = CharFilterInFilter(field_name='role')

    class Meta:
        model = get_user_model()
        fields = ('username', 'role')
