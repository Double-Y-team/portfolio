from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View, ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib import auth
from .forms import *


class CountriesView(View):
    template_name = 'base/countries.html'
    context_object_name = 'list_of_countries'

    def get(self, request, **kwargs):
        username = auth.get_user(request)
        list_of_countries = Countries.objects.all()
        return render(request, self.template_name, locals())

    def get_queryset(self):
        return Countries.objects.all()


class CountryView(DetailView):
    model = Countries
    template_name = 'base/country.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['username'] = auth.get_user(request)
        return self.render_to_response(context)


class DishView(DetailView):
    model = Dish
    template_name = 'base/dish.html'
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['username'] = auth.get_user(request)
        context['form'] = self.form_class(None)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, locals())


class UserCreateFormView(View):
    form_class = UserCreateForm
    template_name = 'base/create.html'

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
            if user.is_active:
                login(request, user)
                return redirect('home:home')
        else:
            login_error = "User dose not exist"
            form = self.form_class(None)
            return render(request, self.template_name, locals())


def userlogout(request):
    auth.logout(request)
    return redirect('/')



