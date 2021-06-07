from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from store.serializers import AuthorSerializer, BookSerializer, OrderSerializer
from store.models import Author, Book, Order
from store.filters import BookFilter


class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_class = BookFilter

    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (permissions.AllowAny,)


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
