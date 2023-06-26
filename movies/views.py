from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie


# Create your views here.


def index(request):
    movie = Movie.objects.all()
    return render(request, "index.html", {"movies": movie})


def detail(request, movies_id):
    movie = get_object_or_404(Movie, pk=movies_id)
    return render(request, "details.html", {"movie": movie})
