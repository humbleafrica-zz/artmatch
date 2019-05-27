
from django.conf.urls import include, url
from django.contrib import admin
from artist import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('signup/', auth_views.signup, name='signup'),
    url('login/', auth_views.login, name='login'),
    url('logout/', auth_views.logout, name='logout'),
    url(r'^profile/$', auth_views.profile, name='profile'),
    url('', include('artist.urls')),

]