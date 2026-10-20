from django.urls import path
from .views import display_books, delete_book, update_book, make_book_request
from .serializer_views import book,update_book,delete_book

app_name="books_app"
urlpatterns =[
    path("display-books/",display_books,name="display_books"),
    path("delete-book/<str:book_id>/",delete_book,name="delete_book"),
    path("update-book/<str:book_request>/",update_book,name="update_book"),
    path("make-a-book-request/",make_book_request,name="book_request"),
    # API path
    path("book-api/",book,name="book_api"),
    path("update-book-api/<str:reference_id>/",update_book,name="update_book_api"),
    path("delete-book-api/<str:id>/",delete_book,name="delete_book_api"),
]