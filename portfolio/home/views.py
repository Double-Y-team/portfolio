from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.contrib import auth
from django.views.generic.detail import SingleObjectMixin


def home(request):
    username = auth.get_user(request)
    return render(request, 'home/home.html', locals())


class NewsView(View):
    template_name = 'home/news.html'
    context_object_name = 'all_news'

    def get(self, request, **kwargs):
        username = auth.get_user(request)
        all_news = News.objects.all()
        return render(request, self.template_name, locals())

    def get_queryset(self):
        return News.objects.all()


