from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView, CreateView
from django.contrib.auth.views import LoginView, UserModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, BookForm, BookQtyForm
from .models import Book, BookQuantity
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Count, F


def report(request):
    """
    returns a log of all registered users with date joined and last login
    """
    all_users = User.objects.values()
    return render(request, "report.html", {"users": all_users})


class HomepageView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "index.html"

    def get_queryset(self):

        cat_list = (
            Book.objects.values(measure=F("categories"))
            .annotate(Count("id"))
            .order_by("-id__count")
        )
        author_list = (
            Book.objects.values(measure=F("author_last"))
            .annotate(Count("id"))
            .order_by("-id__count")
        )

        return cat_list


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
            | Book.objects.select_related("book_id").filter(
                author_first__icontains=query
            )
            | Book.objects.select_related("book_id").filter(
                author_last__icontains=query
            )
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
    """
    loads form page to allow qty edits
    """
    book = Book.objects.select_related("book_id").get(id=id)
    template = loader.get_template("adjust_qty.html")
    context = {
        "book": book,
    }
    return HttpResponse(template.render(context, request))


def update_record(request, id):
    """
    allows integer updates to book quantities and saves to db
    """
    try:
        qty = int(request.POST["qty"])
    except ValueError:
        return HttpResponse("Invalid input: Please go back and provide a valid number.")

    q = BookQuantity.objects.get(book_id=id)
    q.quantity = qty
    q.save()
    return HttpResponseRedirect(reverse("index"))


def is_valid_queryparam(param):
    return param != "" and param is not None


def filter(request):
    """
    allows the view all page to filter by author/category and whether quantity is > 0 (in stock)
    """
    qs = Book.objects.all()
    authors = request.GET.get("author")
    category = request.GET.get("category")
    instock = request.GET.get("in-stock")
    flag_cat = ""
    flag_auth = ""
    if is_valid_queryparam(category) and category != "Choose...":
        flag_cat = category
        qs = qs.filter(categories=category)
    if is_valid_queryparam(authors) and authors != "Choose...":
        flag_auth = authors
        qs = qs.filter(author_last=authors)
    if instock == "on":
        qs = qs.filter(book_id__quantity__gt=0)
        toggle = "in stock"
    else:
        toggle = " "

    return qs, flag_auth, flag_cat, toggle


def BootstrapFilterView(request):
    """
    view all page that populates optional filters with author last name and category.
    """
    qs, flag_auth, flag_cat, toggle = filter(request)
    cats = Book.objects.select_related("book_id").values("categories").distinct()
    authors = Book.objects.values("author_last").distinct()
    context = {
        "flagcat": flag_cat,
        "flagauth": flag_auth,
        "queryset": qs,
        "categories": cats,
        "authors": authors,
        "instock": toggle,
    }
    return render(request, "view_all.html", context)


def confirm_remove_item(request, isbn):
    """
    asks the user if they are sure they would like to delete the item, and deletes from the DB when confirmation is received
    """
    book = get_object_or_404(Book, isbn10=isbn)

    if request.method == "POST":
        book.delete()
        return redirect("index")

    return render(request, "remove_confirmation.html", {"book": book})


def delete_item(request, isbn):
    book = get_object_or_404(Book, isbn10=isbn)
    book.delete()
    return redirect("search_results")


def about(request):
    """
    allows the website to display an unordered list of group member names
    """
    team_members = [
        {"name": "Ryan Burres"},
        {"name": "Jaylan Chavis"},
        {"name": "Brandon Biggs"},
        {"name": "James Dove"},
        {"name": "Joshua Macy"},
        {"name": "Julia McDonald"},
    ]
    return render(request, "about.html", {"team_members": team_members})


def login(request):
    return render(request, "login.html")
