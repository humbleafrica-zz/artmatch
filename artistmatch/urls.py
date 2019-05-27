
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('signup/', user_views.signup, name='signup'),
    url('login/', auth_views.login, name='login'),
    url('logout/', auth_views.logout, name='logout'),
    url('profile/$', user_views.profile, name='profile'),
    url('', include('artist.urls')),
]