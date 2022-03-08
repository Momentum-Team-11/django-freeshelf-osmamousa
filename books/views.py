from django.shortcuts import render, redirect, get_object_or_404
from .models import books
from .forms import booksForm
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, World")

def list_books(request):
    books = books.objects.all()
    return render(request,"books/list_books.html",{"books": books})

# Create your views here.
