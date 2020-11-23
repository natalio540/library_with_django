from django.urls import path
from booksLoans import views


app_name = 'booksLoans'

urlpatterns = [
    path('books', views.books_list, name = 'books'),
    path('addbook', views.book_add, name='addbook'),
    path('delete/<int:id>', views.book_delete, name='book_delete'),
    path('addbook/<int:id>/',views.book_update, name = 'book_update'),
]