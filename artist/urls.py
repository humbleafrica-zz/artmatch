from django.conf.urls import include, url
from . import views

app_name = 'artist'

urlpatterns = [
    url('artist/templates/artist/index.html', views.IndexView),
    url('artist/templates/artist/detail.html', views.DetailView),

]