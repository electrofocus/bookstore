from rest_framework import serializers

from store.models import Author, Book, Order


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'full_name',
        )
        read_only_fields = ('id',)


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'price',
            'publication_date',
        )
        read_only_fields = ('id',)


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'price',
            'publication_date',
        )
        read_only_fields = ('id',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'book',
        )
        read_only_fields = ('id',)
