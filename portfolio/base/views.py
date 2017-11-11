from django.shortcuts import render, redirect
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['username'] = auth.get_user(request)
        return self.render_to_response(context)


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
    pass


class UserLogoutFormView(View):
    pass


