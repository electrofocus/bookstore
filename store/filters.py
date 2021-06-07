from django_filters import (
    FilterSet,
    NumberFilter,
    DateFromToRangeFilter,
)

from store.models import Book


class BookFilter(FilterSet):
    publication_date = DateFromToRangeFilter()
    price_min = NumberFilter(field_name='price', lookup_expr='gt')
    price_max = NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Book
        fields = (
            'publication_date',
            'price_min',
            'price_max',
            'authors',
        )
