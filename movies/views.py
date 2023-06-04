from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movies': data})

def home(request):
    return HttpResponse("Home page!")

def add(request):
    return render(request, 'movies/add.html', )