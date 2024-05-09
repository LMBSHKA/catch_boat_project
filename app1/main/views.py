from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'contet': 'Главгая страница'
    }
    return render(request, 'main/index.html', context)
