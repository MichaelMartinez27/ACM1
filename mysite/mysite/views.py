from django.shortcuts import render
from .models import task


def mainPage(request):
    
    return render(request, "/main.html")