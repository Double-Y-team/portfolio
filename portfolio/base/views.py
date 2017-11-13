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


class UserCreateFormView(View):
    form_class = UserCreateForm
    template_name = 'base/.html'

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
                    request.session.set_expiry(3600)
                    request.session['username'] = username
                    login(request, user)
                    return redirect('home:home')

        return render(request, temp, {'form': form})


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'base/login.html'

    def get(self, request, **kwargs):
        username = auth.get_user(request)
        form = self.form_class(None)
        return render(request, self.template_name, locals())

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and username not in request.session:
                login(request, user)
                request.session.set_expiry(3600)
                request.session['username'] = username
                return redirect('home:home')
        else:
            login_error = "User dose not exist"
            form = self.form_class(None)
            return render(request, self.template_name, locals())


def userlogout(request):
    auth.logout(request)
    return redirect('/')



