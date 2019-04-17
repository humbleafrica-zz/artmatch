from django.conf.urls import include, url
from . import views

app_name = 'artist'

urlpatterns = [
    # /artist/
    url(r'^$', views.index, name='index'),
    
    # /artist/craftid
    url(r'^(?P<craftid>[0-9]+)/$', views.detail, name='detail'),
    
    # /artist/craftid/favorite
    url(r'^(?P<craftid>[0-9]+)/favorite/$', views.detail, name='favorite'),

]