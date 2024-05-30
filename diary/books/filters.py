from django_filters import rest_framework as filters

from .models import Book, Note


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    ...


class SearchBook(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    user = CharFilterInFilter(field_name='user__username', lookup_expr='in')

    class Meta:
        model = Book
        fields = ('name', 'user')


class SearchNote(filters.FilterSet):
    book = CharFilterInFilter(field_name='book__id', lookup_expr='in')
    date = filters.DateFromToRangeFilter(field_name='date')
    time = filters.TimeRangeFilter(field_name='time')

    class Meta:
        model = Note
        fields = ('book', 'date', 'time')
