from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField()
