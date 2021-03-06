from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    full_name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField()

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_notified = models.BooleanField(default=False)
