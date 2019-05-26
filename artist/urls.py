from django.conf.urls import url
from . import views as artist_views

app_name = 'artist'

urlpatterns = [
    url(r'^index/$', artist_views.index, name='index'),
    url(r'^catalogue/$', artist_views.catalogue, name='catalogue'),
    url(r'^$', artist_views.start, name='start'),
    url(r'^bug/$', artist_views.bug, name='bug'),
    url(r'^feature/$', artist_views.feature, name='feature'),
    url(r'^profile/$', artist_views.profile, name='profile'),
    url(r'^about/$', artist_views.about, name='about'),
    #url(r'^profile/(?P<pk>[0-9]+)$', artist_views.profile, name='profile'),
]
