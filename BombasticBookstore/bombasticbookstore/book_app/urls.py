from django.urls import path
from . import views
from .views import (
    SearchResultsView,
    SearchView,
    HomepageView,
)

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("search/", SearchView.as_view(), name="search"),
    path("search-results/", SearchResultsView.as_view(), name="search_results"),
]
