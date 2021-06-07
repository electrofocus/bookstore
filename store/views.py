from rest_framework import generics, permissions

from store.serializers import BookSerializer
from store.models import Book


class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Book.objects.all()
