from bookstore.celery import send_email_task
from datetime import datetime, timedelta

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from store.serializers import AuthorSerializer, BookSerializer, OrderSerializer
from store.models import Author, Book, Order
from store.filters import BookFilter


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
        send_date = datetime.utcnow() + timedelta(seconds=60)
        email = self.request.user.email
        message = "Thanks for ordering the book {} at {}".format(
            generics.get_object_or_404(Book, id=book_id),
            datetime.utcnow(),
        )
        send_email_task.apply_async((email, message), eta=send_date)
