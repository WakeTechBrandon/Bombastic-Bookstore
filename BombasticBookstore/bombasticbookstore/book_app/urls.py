from django.urls import path
from .views import SearchResultsView, HomepageView, delete_item

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('inventory/delete/<int:item_id>/', delete_item.as_view(), name='delete_item'),
]
