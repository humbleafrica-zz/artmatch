from django.conf.urls import include, url
from . import views

urlpatterns = [
    # /artist/
    url(r'^$', views.index, name='index'),
    
    # /match all integers
    url(r'^(?P<craft_id>[0-9]+)/$',views.detail, name='detail'),
    
]