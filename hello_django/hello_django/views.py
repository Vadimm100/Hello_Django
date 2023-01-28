from django.http import HttpResponse
from django.shortcuts import render


def about(request):  # Привязываем страницу about.html и передадим переменную
    a = 5 + 6
    return render(request, 'about.html', {'gretting': 'hello'})


# def about(request): # Привязываем страницу about.html
#     return render(request,'about.html')

def home(request):
    return render(request, 'home.html', {'gretting': 'Your_name'})
