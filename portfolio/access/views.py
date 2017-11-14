from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import auth, sessions
from django.views.generic import View
from .forms import *


class UserCreateFormView(View):
    form_class = UserCreateForm
    template_name = 'access/create.html'

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
    template_name = 'access/login.html'

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



