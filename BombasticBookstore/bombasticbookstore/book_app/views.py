from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, BookForm
from .models import Book
from django.http import HttpResponse
from django.urls import reverse_lazy


class HomepageView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "index.html"


class SearchView(LoginRequiredMixin, FormView):
    template_name = "search.html"
    form_class = SearchForm


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET["q"]
        object_list = (
            Book.objects.filter(title__icontains=query)
            | Book.objects.filter(author_first__icontains=query)
            | Book.objects.filter(author_last__icontains=query)
            | Book.objects.filter(isbn10__icontains=query)
        )
        return object_list


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm()
    return render(request, "add_book/add_book.html", {"form": form})
