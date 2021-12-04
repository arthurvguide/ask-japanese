from django.shortcuts import render
from django.views import View


def get_menu(request):
    return render(request, 'menu.html')
