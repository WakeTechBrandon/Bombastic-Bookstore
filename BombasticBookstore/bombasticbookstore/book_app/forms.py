from django import forms
from .models import Book, BookQuantity

class SearchForm(forms.Form):
    q = forms.CharField(label="Search", max_length=100)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn10', 'title', 'author_first', 'author_last', 'categories', 'thumbnail', 'published_year', 'num_pages']
        labels = {
            'isbn10': 'ISBN-10',
            'title': 'Title',
            'author_first': 'Author First Name',
            'author_last': 'Author Last Name',
            'categories': 'Categories',
            'thumbnail': 'Thumbnail URL',
            'published_year': 'Published Year',
            'num_pages': 'Number of Pages',
        }

class BookQtyForm(forms.ModelForm):
    title =  forms.CharField(label="title", max_length=100)
    quantity = forms.IntegerField(label="qty")