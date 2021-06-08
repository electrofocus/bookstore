from datetime import datetime, timedelta

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from store.serializers import AuthorSerializer, BookSerializer, OrderSerializer
from store.models import Author, Book, Order
from store.filters import BookFilter

from bookstore.tasks import send_email_task


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAdminUser,)


class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAdminUser,)


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

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        self.send_thanks(request)
        return response

    def send_thanks(self, request):
        book_id = request.data['book']
        utcnow = datetime.utcnow()
        book = get_object_or_404(Book, id=book_id)
        user = request.user

        message = '''
            Hello, {}!

            Thanks for ordering the book "{}" at {}

            Sincerely, Bookstore.
        '''.format(user.full_name, book, utcnow)

        send_date = utcnow + timedelta(seconds=30)
        send_email_task.apply_async((user.email, message), eta=send_date)
