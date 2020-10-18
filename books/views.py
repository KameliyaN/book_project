from django.shortcuts import render, redirect

# Create your views here
#
from books.forms import BookForm
from books.models import Book


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)


def create(request):
    if request.method == 'GET':
        context = {
            'form': BookForm()
        }
        return render(request, 'books/create.html', context)
    form = BookForm(request.POST)
    if form.is_valid():
        book = form.save()
        book.save()
        return redirect('index')


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': BookForm(instance=book)
        }
        return render(request, 'books/edit.html', context)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        book = form.save()
        book.save()
        return redirect('index')
