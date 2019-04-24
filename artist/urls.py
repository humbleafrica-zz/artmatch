from django.conf.urls import url
from . import views
from django import forms

app_name = 'artist'

urlpatterns = [
    #two views poiting to the same view with different names
    url('', views.start, name='starter'),
    
    url('index', views.start, name='index'),
    
    url('artist', views.catalogue, name='artist'),
    
    url('login', views.login, name='login'),
    
    #url('signup', views.signup, name='signup')

]