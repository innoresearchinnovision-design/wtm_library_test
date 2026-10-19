from django.shortcuts import render
from author.models import Author
from book_app.models import Book,BookRequest
from genre_app.models import Genre
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_page(request):
    user=request.user
    books = Book.objects.all().prefetch_related('bookrequest_set')
    book_request=BookRequest.objects.all().order_by("-id").select_related('book')
    if user.is_superuser:
        borrowed_books=book_request.filter(book__status='br')
    else:
        borrowed_books=book_request.filter(customer=user,book__status='br')
    total_borrowed_books=borrowed_books.count()
    total_books = books.count()
    total_authors = Author.objects.count()
    total_genres = Genre.objects.count()
    liu ={
        "total_books":total_books,
        "total_authors":total_authors,
        "total_genres":total_genres,
        "total_borrowed_book":total_borrowed_books,
        "borrowed_books":borrowed_books
    }
    return render(request,"base/index.html",liu)
