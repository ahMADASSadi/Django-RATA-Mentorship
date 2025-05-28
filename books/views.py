from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book

# Create your views here.


class BookListView(ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"
    model = Book

    def get_queryset(self):
        return Book.objects.all().order_by("title")


class BookDetailView(DetailView):
    template_name = "books/book_detail.html"
    context_object_name = "book"
    model = Book

    def get_queryset(self):
        return Book.objects.all()
