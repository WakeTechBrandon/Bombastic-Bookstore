from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView
from .forms import SearchForm
from .models import Book
from django.http import HttpResponse


class HomepageView(FormView):
    template_name = "home.html"
    form_class = SearchForm


class SearchResultsView(ListView):
    model = Book
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET["q"]
        object_list = (
            Book.objects.filter(title__icontains=query)
            | Book.objects.filter(f_name__icontains=query)
            | Book.objects.filter(l_name__icontains=query)
            | Book.objects.filter(isbn__icontains=query)
        )
        return object_list


def test(request, book_id):
    b = Book.objects.get(id=book_id)
    return HttpResponse("You're looking at book %s." % b.title)

def index(request):
    return render(request, 'index.html')

def delete_item(request, isbn):
    item = get_object_or_404(Book, id=isbn)
    
    item.delete()

    return redirect("home")
