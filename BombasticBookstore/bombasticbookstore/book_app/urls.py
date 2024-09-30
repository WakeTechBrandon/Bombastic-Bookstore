from django.urls import path
from .views import SearchResultsView, CustomLoginView, SearchView, HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    path("search/", SearchView.as_view(), name="search"),
    path("search-results/", SearchResultsView.as_view(), name="search_results"),
]
