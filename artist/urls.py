from django.conf.urls import url
from . import views
from django import forms

app_name = 'artist'

urlpatterns = [
    #two views poiting to the same view with different names
    url(r'^$', views.start, name='starter'),
    url(r'^index/$', views.start, name='index'),
    url(r'^catalogue/$', views.catalogue, name='catalogue'),
    url(r'^bugs/$', views.bug, name='bugs'),
    url(r'^features/$', views.feature, name='features'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

    #url('signup', views.signup, name='signup')

]