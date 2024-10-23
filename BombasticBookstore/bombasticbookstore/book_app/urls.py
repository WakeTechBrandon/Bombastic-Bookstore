from django.urls import path
from .views import SearchResultsView, HomepageView, delete_item, confirm_remove_item

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('inventory/delete/<str:isbn>/', confirm_remove_item, name='confirm_remove_item'),  
    path('inventory/delete/confirm/<str:isbn>/', delete_item, name='delete_item'),  
]


