# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.db.models import Max
from .models import Movie

# def home(request):
#     return HttpResponse('<h1>Django</h1><h3>Bem vindo ao Grupy-SP</h3>')


def home(request):
    return render(request, 'index.html')


def movie_list_json(request):
    movies = Movie.objects.all()
    s = serializers.serialize("json", movies)
    return HttpResponse(s)


# def movie_list(request):
#     movies = Movie.objects.all()
#     context = {'movies': movies}
#     return render(request, 'core/movie_list.html', context)


class MovieList(ListView):
    template_name = 'core/movie_list.html'
    model = Movie
    context_object_name = 'movies'

    def get_queryset(self):
        m = Movie.objects.all()
        # Filme de maior bilheteria
        if self.request.GET.get('great_movie', False):
            q = Movie.objects.all().aggregate(Max('raised'))
            m = Movie.objects.filter(raised=q['raised__max'])
        return m


class MovieCreate(CreateView):
    template_name = 'core/movie_form4.html'
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movie_list')


class MovieDetail(DetailView):
    template_name = 'core/movie_detail.html'
    model = Movie
