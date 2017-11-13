from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View, ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib import auth, sessions
from .forms import *


class CountriesView(View):
    template_name = 'base/countries.html'
    context_object_name = 'list_of_countries'

    def get(self, request, **kwargs):
        list_of_countries = Countries.objects.all()
        return render(request, self.template_name, locals())


class CountryView(DetailView):
    model = Countries
    template_name = 'base/country.html'


class DishView(DetailView):
    model = Dish
    template_name = 'base/dish.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, locals())


class TypesOfDishesView(View):
    template_name = 'base/types_of_dishes.html'
    context_object_name = 'types'

    def get(self, request, **kwargs):
        types = TypesOfDishes.objects.all()
        return render(request, self.template_name, locals())


class DishesOfTypeView(DetailView):
    model = TypesOfDishes
    template_name = 'base/dishes_of_type.html'




