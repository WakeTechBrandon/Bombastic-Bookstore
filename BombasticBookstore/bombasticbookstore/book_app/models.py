from django.db import models

# Create your models here.


class Book(models.Model):
    isbn = models.CharField(max_length=13, default="0000000000000")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
