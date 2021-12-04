from django.shortcuts import render
from django.views import View
# Create your views here.

def get_book(request):
    return render(request, 'book.html')