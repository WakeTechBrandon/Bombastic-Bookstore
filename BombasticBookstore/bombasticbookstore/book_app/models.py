from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn10 = models.CharField(max_length=10, default='0000000000')
    title = models.CharField(max_length=200, default='Untitled')
    author_first = models.CharField(max_length=100, default='Unknown')
    author_last = models.CharField(max_length=100, default='Unknown')
    categories = models.CharField(max_length=200, default='Uncategorized')
    thumbnail = models.URLField(default='http://example.com/default-thumbnail.jpg')
    published_year = models.IntegerField(default=2000)
    num_pages = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class BookQuantity(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, primary_key=True, to_field='id', related_name='book_id')
    quantity = models.IntegerField(default=0)
