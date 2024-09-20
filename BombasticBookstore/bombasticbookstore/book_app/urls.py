from django.urls import path

from . import views

urlpatterns = [
    #testing -- to delete
    path("<int:book_id>/", views.test, name="test")
]