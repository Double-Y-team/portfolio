from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth import authenticate, login
from .forms import *

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


class UserFormView(View):
    form_class = UserForm
    template_name = 'base/login.html'

    def get(self, request):
        temp = self.template_name
        form = self.form_class(None)
        return render(request, temp, {'form': form})

    def post(self, request):
        temp = self.template_name
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('home:home')

        return render(request, temp, {'form': form})



