from django.contrib import admin

from store.models import Book, Order, Author

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Author)
