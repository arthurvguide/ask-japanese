from django.shortcuts import render
from django.views import View
# Create your views here.


def get_contact(request):
    return render(request, 'contact.html')
