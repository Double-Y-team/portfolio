from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import *

class CountriesView(ListView):
    template_name = 'base/countries.html'
    context_object_name = 'list_of_countries'

    def get_queryset(self):
        return Countries.objects.all()
