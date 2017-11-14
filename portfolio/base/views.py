from django.views.generic import View, DetailView
from django.shortcuts import render, redirect
from django.contrib import auth
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['form'] = self.form_class(None)
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.dish = Dish.objects.get(id=kwargs['pk'])
            comment.user = auth.get_user(request)
            comment.comment = form.cleaned_data['comment_area']
            comment.save()
        return redirect('/dish/'+str(kwargs['pk'])+'/')


class TypesOfDishesView(View):
    template_name = 'base/types_of_dishes.html'
    context_object_name = 'types'

    def get(self, request, **kwargs):
        types = TypesOfDishes.objects.all()
        return render(request, self.template_name, locals())


class DishesOfTypeView(DetailView):
    model = TypesOfDishes
    template_name = 'base/dishes_of_type.html'




