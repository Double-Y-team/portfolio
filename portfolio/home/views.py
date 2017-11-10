from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import *
from django.contrib import auth


def home(request):
    username = auth.get_user(request)
    return render(request, 'home/home.html', locals())


class NewsView(ListView):
    template_name = 'home/news.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        return News.objects.all()


