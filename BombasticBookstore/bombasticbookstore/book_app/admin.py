from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn10', 'title', 'author_first', 'author_last', 'categories', 'published_year']

admin.site.register(Book, BookAdmin)
