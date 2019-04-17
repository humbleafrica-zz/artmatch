from django.conf.urls import include, url
from . import views

app_name = 'artist'

urlpatterns = [
    # /artist/
    url(r'^$', views.index, name='index'),
    
    # /artist/craftid
    url(r'^(?P<craftid>[0-9]+)/$', views.detail, name='detail'),
    
    # /artist/featureid
    #url(r'^(?P<featureid>[0-9]+)/features/$', views.features, name='features'),
    
    # /artist/featureid
    #url(r'^(?P<bugid>[0-9]+)/bugs/$', views.features, name='bugs'),
    
    # /artist/craftid/favorite
    url(r'^(?P<craftid>[0-9]+)/favorite/$', views.detail, name='favorite'),

]