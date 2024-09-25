from django.urls import path
from .views import SearchResultsView, HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]
