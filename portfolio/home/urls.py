from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news', views.NewsView.as_view(), name='news'),


]