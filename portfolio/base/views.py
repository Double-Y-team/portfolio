from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import *

class CountriesView(ListView):
    template_name = 'base/countries.html'
    context_object_name = 'list_of_countries'

    def get_queryset(self):
        return Countries.objects.all()


class CountryView(DetailView):
    model = Countries
    template_name = 'base/country.html'


class DishView(DetailView):
    model = Dish
    template_name = 'base/dish.html'
