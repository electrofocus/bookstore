from rest_framework import serializers

from store.models import Book


class BookSerializer(serializers.ModelSerializer):
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
