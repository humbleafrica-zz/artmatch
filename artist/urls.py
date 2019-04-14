from django.conf.urls import include, url
from . import views

urlpatterns = [
    # /artist/
    url(r'^$', views.index, name='index'),
    
    # /work/work_id
    url(r'^(?P<Work>[0-9]+)/$',views.detail, name='detail'),
    
]