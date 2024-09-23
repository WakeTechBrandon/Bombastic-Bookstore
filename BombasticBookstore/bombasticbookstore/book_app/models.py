from django.db import models

# Create your models here.
<<<<<<< HEAD


class Book(models.Model):
    isbn = models.CharField(max_length=13, default="0000000000000")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
=======
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    year = models.IntegerField()
    thumbnail = models.FileField()
    quantity = models.IntegerField(default=0)
>>>>>>> main
