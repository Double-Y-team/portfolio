from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import *


def home(request):
    return render(request, 'home/home.html')


class NewsView(ListView):
    template_name = 'home/news.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        return News.objects.all()


