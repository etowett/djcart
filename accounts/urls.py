from django.urls import path

from django.urls import re_path as url
from . import views

app_name = 'accounts'


urlpatterns = [
    url('signup', views.signup, name='signup'),
    url('login', views.user_login, name='login'),
    url('logout', views.user_logout, name='logout'),
]
