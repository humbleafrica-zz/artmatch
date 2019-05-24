from django.conf.urls import url
from . import views

app_name = 'artist'

urlpatterns = [
    #two views poiting to the same view with different names
    url('', views.index, name='index'),
    #url('login', views.login, name='login'),
]