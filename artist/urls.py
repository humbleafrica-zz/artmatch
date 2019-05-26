from django.conf.urls import url
from . import views

app_name = 'artist'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^catalogue/$', views.catalogue, name='catalogue'),
    url(r'^/$', views.start, name='start'),
    url(r'^bug/$', views.bug, name='bug'),
    url(r'^feature/$', views.feature, name='feature'),
    #url('login', views.login, name='login'),
]
