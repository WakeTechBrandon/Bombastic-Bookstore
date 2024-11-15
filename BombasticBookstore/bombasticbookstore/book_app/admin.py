from django.contrib import admin
from .models import Book, BookQuantity

class BookQuantAdmin(admin.ModelAdmin):
    list_display = ['quantity']

class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn10', 'title', 'author_first', 'author_last', 'categories', 'published_year']

admin.site.register(Book, BookAdmin, )
admin.site.register(BookQuantity, BookQuantAdmin )
