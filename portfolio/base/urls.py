from django.conf.urls import url
from . import views

app_name = 'base'

urlpatterns = [

    url(r'^countries/$', views.CountriesView.as_view(), name='countries'),

    url(r'^countries/(?P<pk>[0-9]+)/$', views.CountryView.as_view(), name='country'),

    url(r'^dish/(?P<pk>[0-9]+)/$', views.DishView.as_view(), name='dish'),

    url(r'^auth/login/$', views.UserLoginFormView.as_view(), name='login'),

    url(r'^auth/logout/$', views.userlogout, name='logout'),

    url(r'^auth/create/$', views.UserCreateFormView.as_view(), name='create'),





]