from django.conf.urls import url
from . import views

app_name = 'access'

urlpatterns = [

    url(r'^access/login/$', views.UserLoginFormView.as_view(), name='login'),

    url(r'^access/logout/$', views.userlogout, name='logout'),

    url(r'^access/create/$', views.UserCreateFormView.as_view(), name='create'),





]