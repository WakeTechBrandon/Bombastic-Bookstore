from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    year = models.IntegerField()
    thumbnail = models.FileField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title