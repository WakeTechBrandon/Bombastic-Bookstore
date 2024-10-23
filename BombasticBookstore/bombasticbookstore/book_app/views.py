
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, BookForm
from .models import Book
from django.http import HttpResponse


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
            | Book.objects.filter(f_name__icontains=query)
            | Book.objects.filter(l_name__icontains=query)
            | Book.objects.filter(isbn__icontains=query)
        )
        return object_list


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

def test(request, book_id):
    b = Book.objects.get(id=book_id)
    return HttpResponse("You're looking at book %s." % b.title)



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add_book/add_book.html', {'form': form})
  
def confirm_remove_item(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, 'remove.html', {'book': book})

def delete_item(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    book.delete()
    return redirect('search_results')


