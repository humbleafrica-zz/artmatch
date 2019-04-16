from django.conf.urls import include, url
from . import views

app_name = 'artist'

urlpatterns = [
    # /artist/
    url(r'^$', views.index, name='index'),
    
    # /work/work_id
    url(r'^(?P<work_id>[0-9]+)/$',views.detail, name='detail'),
    
    # /work/work_id/favorite
    #url(r'^(?P<work_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
    
]