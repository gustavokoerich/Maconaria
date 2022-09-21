from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'maconaria/index.html')


def simbolos(request):
    return render(request, 'maconaria/simbolos.html')


def conhecimento(request):
    return render(request, 'maconaria/conhecimentos.html')


def historia(request):
    return render(request, 'maconaria/historia.html')