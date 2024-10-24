from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, BookForm,BookQtyForm
from .models import Book, BookQuantity
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
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


def adjust_qty(request, id):
    book = Book.objects.select_related("book_id").get(id=id)
    template = loader.get_template("adjust_qty.html")
    context = {
        "book": book,
    }
    return HttpResponse(template.render(context, request))


def update_record(request, id):
    try:
        qty = int(request.POST["qty"])
    except ValueError:
        return HttpResponse("Invalid input: Please go back and provide a valid number.")
    
    q = BookQuantity.objects.get(book_id=id)
    q.quantity = qty
    q.save()
    return HttpResponseRedirect(reverse("index"))


def view_all(request):

    books = Book.objects.select_related("book_id").all()
    return render(request, "view_all.html", {"books": books})


def confirm_remove_item(request, isbn):
    book = get_object_or_404(Book, isbn10=isbn)
    
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    
    return render(request, 'remove_confirmation.html', {'book': book})

def delete_item(request, isbn):
    book = get_object_or_404(Book, isbn10=isbn)
    book.delete()
    return redirect('search_results')


