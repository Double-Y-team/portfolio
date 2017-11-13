from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required(login_url='base:login')
def home(request):
    return render(request, 'home/home.html', locals())

class NewsView(View): #LoginRequiredMixin
    template_name = 'home/news.html'
    context_object_name = 'all_news'
    #login_url = 'base:login'

    def get(self, request, **kwargs):
        all_news = News.objects.all()
        return render(request, self.template_name, locals())

    def get_queryset(self):
        return News.objects.all()


