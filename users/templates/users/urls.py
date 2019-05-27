from django.conf.urls import url
from . import views

app_name = 'artist'

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^index/$', views.index, name='index'),
    url(r'^catalogue/$', views.catalogue, name='catalogue'),
    url(r'^bug/$', views.bug, name='bug'),
    url(r'^feature/$', views.feature, name='feature'),
    url(r'^about/$', views.about, name='about'),
]
