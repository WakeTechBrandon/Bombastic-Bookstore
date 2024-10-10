
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, BookForm
from .models import Book, BookQuantity
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


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

def adjust_qty(request, id):
  book = Book.objects.select_related('book_id').get(id=id)
  template = loader.get_template('adjust_qty.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))

def update_record(request, id):
  qty = request.POST['qty']
  title=request.POST['title']
  book = Book.objects.select_related('book_id').get(id=id)
  q = BookQuantity.objects.get(book_id=id)
  q.quantity = qty
  book.title = title
  book.save()
  q.save()
  return HttpResponseRedirect(reverse('index'))

def view_all(request):
    
    books = Book.objects.select_related('book_id').all()
    return render(request,'view_all.html',{'books':books})

  
def delete_item(request, isbn):
    item = get_object_or_404(Book, id=isbn)
    
    item.delete()

    return redirect("home")


