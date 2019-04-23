from django.conf.urls import url
from . import views

app_name = 'artist'

urlpatterns = [
    #two views poiting to the same view with different names
    url('', views.index, name='starter'),
    url('artist', views.index, name='index')
]