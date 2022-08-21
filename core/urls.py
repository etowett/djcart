from django.urls import path

from django.urls import re_path as url
from . import views

app_name = 'core'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('dashboard', views.dashboard, name='dashboard'),
]
