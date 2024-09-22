from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# test method--to delete.
def test(request, book_id):
    b = Book.objects.get(id=book_id)
    return HttpResponse("You're looking at book %s." % b.title)

def index(request):
    return render(request, 'index.html')