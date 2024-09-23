from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "isbn",
        "title",
        "f_name",
        "l_name",
        "category",
        "year",
        "thumbnail",
        "quantity",
    )


admin.site.register(Book, BookAdmin)
