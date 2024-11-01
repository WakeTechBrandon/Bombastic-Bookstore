from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, BookForm,BookQtyForm
from .models import Book, BookQuantity
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F

class HomepageView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "index.html"


class SearchView(LoginRequiredMixin, FormView):
    template_name = "search.html"
    form_class = SearchForm


class SearchResultsView(LoginRequiredMixin, ListView):
    model = BookQuantity
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET["q"]
        object_list = (
            Book.objects.select_related("book_id").filter(title__icontains=query)
            | Book.objects.select_related("book_id").filter(author_first__icontains=query)
            | Book.objects.select_related("book_id").filter(author_last__icontains=query)
            | Book.objects.select_related("book_id").filter(isbn10__icontains=query)
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

#
#def view_all(request):

    #books = Book.objects.select_related("book_id").all()
    #title_contains_query = request.GET.get('title_contains')
    #myFilter = BookFilter(request.GET, queryset=books)
    #books = myFilter.qs
    #context = {"books": books, "myFilter": myFilter}
    #context = {'queryset':books}
    #return render(request, "view_all.html", context)

def is_valid_queryparam(param):
    return param != '' and param is not None
    
def filter(request):
    qs= Book.objects.all()
    authors = request.GET.get('author')
    category = request.GET.get('category')
    instock = request.GET.get('in-stock')
    flag_cat=""
    flag_auth=""
    if is_valid_queryparam(category) and category != 'Choose...':
        flag_cat=category
        qs = qs.filter(categories=category)
    if is_valid_queryparam(authors) and authors != 'Choose...':
        flag_auth=authors
        qs = qs.filter(author_last=authors)
    if instock == 'on':
        qs = qs.filter(book_id__quantity__gt=0)
        toggle="in stock"
    else: toggle =" "
        #qs = Book.objects.raw("Select a.id,a.categories, a.author_last, a.title, b.quantity from book_app_book a, book_app_bookquantity b where b.quantity >0")
     
    return qs,flag_auth,flag_cat, toggle

def BootstrapFilterView(request):
    qs,flag_auth,flag_cat, toggle = filter(request)
    cats = Book.objects.select_related('book_id').values('categories').distinct()
    authors = Book.objects.values('author_last').distinct()
    #count= BookQuantity.objects.values('quantity')
    context = {
        'flagcat':flag_cat,
        'flagauth':flag_auth,
        'queryset': qs,
        'categories': cats,
        'authors' :authors,
        'instock':toggle
    }
    return render(request, "view_all.html", context) 

def confirm_remove_item(request, isbn):
    book = get_object_or_404(Book, isbn10=isbn)
    
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    
    return render(request, 'remove_confirmation.html', {'book': book})

def delete_item(request, isbn):
    book = get_object_or_404(Book, isbn10=isbn)
    book.delete()
    return redirect('search_results')

def about(request):
    team_members = [
        {'name': 'Ryan Burres'},
        {'name': 'Jaylan Chavis'},
        {'name': 'Brandon Biggs'},
        {'name': 'James Dove'},
        {'name': 'Joshua Macy'},
        {'name': 'Julia McDonald'},
    ]
    return render(request, 'about.html', {'team_members': team_members})

def login(request): 
    return render(request, 'login.html')