from django.shortcuts import render
from django.views.generic import FormView, ListView
from .forms import SearchForm
from .models import Book


# Create your views here.
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
            | Book.objects.filter(author__icontains=query)
            | Book.objects.filter(isbn__icontains=query)
        )
        return object_list
