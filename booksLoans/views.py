from django.shortcuts import render,HttpResponse,redirect
from .models import booksTable
from loansApp.models import loansTable
from libpanel import settings
from .forms import BookForm,BookLoanForm
from django.db.models import Q


# Create your views here.


# show books
def books_list(request):
    books_list = booksTable.objects.all()
    queryset = request.GET.get('buscar')
    if queryset:
        books_list = booksTable.objects.filter(
            Q(name__icontains= queryset) |
            Q(author__icontains= queryset)
        ).distinct()
    return render(request,'booksLoans/books.html', {'list':books_list})    

# add books
def book_add(request):
    if request.method== "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()             
        return redirect('/booksLoans/books')
    else:     
         form= BookForm()         
    return render(request,'booksLoans/addbook.html',{'form':form})    

# update books
def book_update(request, id):
    book= booksTable.objects.get(id=id)
    form = BookForm
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():
                form.save() 
        return redirect('/booksLoans/books')      
    else:
        form= BookForm(instance=book)
    return render(request,'booksLoans/addbook.html',{'form':form})  
    

# delete books
def book_delete(request,id):
    book = booksTable.objects.get(pk=id)
    book.delete()
    return redirect('/booksLoans/books')
