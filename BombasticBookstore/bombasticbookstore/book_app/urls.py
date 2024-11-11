from django.urls import path
from . import views
from .views import (
    SearchResultsView,
    SearchView,
    HomepageView,
    delete_item,
    confirm_remove_item,
    BootstrapFilterView
)

urlpatterns = [
    path("", HomepageView.as_view(), name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("delete_item/", views.delete_item, name="delete_item"),
    path("adjust_qty/<int:id>", views.adjust_qty, name="adjust_qty"),
    path("adjust_qty/updaterecord/<int:id>", views.update_record, name="update_record"),
    path("search/", SearchView.as_view(), name="search"),
    path("search-results/", SearchResultsView.as_view(), name="search_results"),
    path("view_all/", BootstrapFilterView, name='bootstrap'),
    path('inventory/delete/<str:isbn>/', confirm_remove_item, name='confirm_remove_item'),  
    path('inventory/delete/confirm/<str:isbn>/', delete_item, name='delete_item'),  
    path('about/', views.about, name='about'),
    path('report/',views.report,name='report')
]
